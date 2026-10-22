"""UI state: filters, the shell, the typewriter, and the contact form."""

from __future__ import annotations

import asyncio

import reflex as rx

from portfolio.data import INTRO_LINE, PROJECTS, SECTIONS, TERMINAL_BANNER
from portfolio.terminal import Reply, answer
from portfolio.validate import (
    build_receipt,
    company_error,
    email_error,
    message_error,
    name_error,
)

_SCROLL_LOG = (
    "setTimeout(() => {"
    "const el = document.getElementById('term-log');"
    "if (el) el.scrollTop = el.scrollHeight;"
    "}, 70)"
)


class State(rx.State):
    """Session state for one visitor."""

    active_tag: str = "All"
    active_section: str = "top"
    nav_open: bool = False

    selected_id: str = ""
    modal_open: bool = False

    typed: str = ""
    intro_played: bool = False

    terminal_log: str = TERMINAL_BANNER
    command_history: list[str] = []

    contact_name: str = ""
    contact_email: str = ""
    contact_company: str = ""
    contact_message: str = ""
    contact_attempted: bool = False
    contact_sent: bool = False
    contact_receipt: str = ""
    error_name: str = ""
    error_email: str = ""
    error_company: str = ""
    error_message: str = ""

    @rx.var
    def visible_count(self) -> int:
        tag = self.active_tag
        if tag == "All":
            return len(PROJECTS)
        return sum(1 for project in PROJECTS if tag in project["tags"])

    @rx.var
    def selected_name(self) -> str:
        selected = self.selected_id
        for project in PROJECTS:
            if project["id"] == selected:
                return str(project["name"])
        return ""

    @rx.var
    def selected_blurb(self) -> str:
        selected = self.selected_id
        for project in PROJECTS:
            if project["id"] == selected:
                return str(project["blurb"])
        return ""

    @rx.var
    def name_ok(self) -> bool:
        return name_error(self.contact_name) == ""

    @rx.var
    def email_ok(self) -> bool:
        return email_error(self.contact_email) == ""

    @rx.var
    def message_ok(self) -> bool:
        return message_error(self.contact_message) == ""

    def set_active_tag(self, tag: str):
        self.active_tag = tag

    def toggle_nav(self):
        self.nav_open = not self.nav_open

    def close_nav(self):
        self.nav_open = False

    def goto(self, section: str):
        if section not in SECTIONS:
            return None
        self.active_section = section
        self.nav_open = False
        path = self.router.url.path or "/"
        if path not in ("/", ""):
            return rx.redirect(f"/#{section}")
        return rx.scroll_to(section)

    def focus_hash(self):
        fragment = str(self.router.url.fragment or "").lstrip("#")
        if fragment in SECTIONS:
            self.active_section = fragment
            self.nav_open = False
            return rx.scroll_to(fragment)
        return None

    def open_project(self, project_id: str):
        self.selected_id = project_id
        self.modal_open = True

    def on_modal_change(self, is_open: bool):
        self.modal_open = is_open

    def set_contact_name(self, value: str):
        self.contact_name = value
        if self.contact_attempted:
            self.error_name = name_error(value)

    def set_contact_email(self, value: str):
        self.contact_email = value
        if self.contact_attempted:
            self.error_email = email_error(value)

    def set_contact_company(self, value: str):
        self.contact_company = value
        if self.contact_attempted:
            self.error_company = company_error(value)

    def set_contact_message(self, value: str):
        self.contact_message = value
        if self.contact_attempted:
            self.error_message = message_error(value)

    def submit_contact(self, form_data: dict):
        self.contact_name = str(form_data.get("name", "")).strip()
        self.contact_email = str(form_data.get("email", "")).strip()
        self.contact_company = str(form_data.get("company", "")).strip()
        self.contact_message = str(form_data.get("message", "")).strip()
        self.contact_attempted = True
        self.error_name = name_error(self.contact_name)
        self.error_email = email_error(self.contact_email)
        self.error_company = company_error(self.contact_company)
        self.error_message = message_error(self.contact_message)
        if self.error_name or self.error_email or self.error_company or self.error_message:
            self.contact_sent = False
            return
        self.contact_sent = True
        self.contact_receipt = build_receipt(
            self.contact_name,
            self.contact_email,
            self.contact_company,
            self.contact_message,
        )

    def reset_contact(self):
        self.contact_name = ""
        self.contact_email = ""
        self.contact_company = ""
        self.contact_message = ""
        self.contact_attempted = False
        self.contact_sent = False
        self.contact_receipt = ""
        self.error_name = ""
        self.error_email = ""
        self.error_company = ""
        self.error_message = ""

    def run_command(self, command: str):
        return self._apply(command)

    def exec_terminal(self, form_data: dict):
        return self._apply(str(form_data.get("cmd", "")))

    def _apply(self, raw: str):
        text = raw.strip()
        if not text:
            return None
        history = [*self.command_history, text][-50:]
        reply: Reply = answer(text, history)
        self.command_history = history
        if reply.clear:
            self.terminal_log = "cleared. type help.\n"
        else:
            block = f"\nkai@mercer:~$ {text}\n{reply.output}\n"
            combined = self.terminal_log + block
            if len(combined) > 12000:
                combined = combined[-12000:]
                newline = combined.find("\n")
                if newline != -1:
                    combined = combined[newline + 1 :]
            self.terminal_log = combined
        events = [rx.call_script(_SCROLL_LOG)]
        if reply.go == "resume":
            self.nav_open = False
            events.append(rx.redirect("/resume"))
        elif reply.go:
            navigation = self.goto(reply.go)
            if navigation is not None:
                events.append(navigation)
        return events

    @rx.event(background=True)
    async def play_intro(self):
        async with self:
            if self.intro_played:
                return
            self.intro_played = True
            self.typed = ""
        for char in INTRO_LINE:
            await asyncio.sleep(0.028)
            async with self:
                self.typed += char
