"""Home page sections."""

from __future__ import annotations

import reflex as rx

from portfolio.components.blocks import (
    field_note,
    heading,
    job_item,
    panel,
    project_card,
    skill_group,
)
from portfolio.data import EXPERIENCE, PROJECTS, QUICK_COMMANDS, SKILLS, TAGS
from portfolio.state import State


def _window_bar(title: str) -> rx.Component:
    return rx.el.div(
        rx.el.span(class_name="dot r"),
        rx.el.span(class_name="dot y"),
        rx.el.span(class_name="dot g"),
        rx.el.span(title, class_name="code-title"),
        class_name="window-bar",
    )


def _identity_card() -> rx.Component:
    return rx.el.div(
        _window_bar("identity.py"),
        rx.el.pre(
            rx.el.span("class ", class_name="tok-k"),
            rx.el.span("Kai", class_name="tok-n"),
            ":\n    role = ",
            rx.el.span('"Python developer"', class_name="tok-s"),
            "\n    base = ",
            rx.el.span('"Portland, OR"', class_name="tok-s"),
            "\n    booking = ",
            rx.el.span('"winter 2026"', class_name="tok-s"),
            "\n\n    def focus(self):\n        return ",
            rx.el.span('["streams", "tools", "internal apps"]', class_name="tok-s"),
            "\n\n",
            rx.el.span("# previously staff engineer, Northline", class_name="tok-c"),
            "\n",
            class_name="code-pre",
        ),
        class_name="code-card",
        aria_label="Short Python sketch of Kai",
    )


def hero() -> rx.Component:
    return panel(
        rx.el.div(
            rx.el.div(
                rx.el.p("portfolio · 01", class_name="kicker"),
                rx.el.h1("Kai Mercer", class_name="h1"),
                rx.el.p(
                    "Python developer for streams, tools, and internal apps. Previously staff engineer at Northline. Now independent in Portland.",
                    class_name="lede",
                ),
                rx.el.p("kai@mercer:~$ cat now.txt", class_name="prompt-line"),
                rx.el.p(
                    State.typed,
                    rx.el.span(class_name="caret", aria_hidden="true"),
                    class_name="typed",
                ),
                rx.el.div(
                    rx.el.button(
                        "View the work",
                        type="button",
                        class_name="btn btn-primary",
                        on_click=State.goto("work"),
                    ),
                    rx.el.button(
                        "Open the shell",
                        type="button",
                        class_name="btn btn-ghost",
                        on_click=State.goto("terminal"),
                    ),
                    rx.el.a("Read the resume", href="/resume", class_name="btn btn-ghost"),
                    class_name="hero-actions",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.p("writing Python", class_name="stat-label"),
                        rx.el.p("8 yrs", class_name="stat-value"),
                        class_name="stat",
                    ),
                    rx.el.div(
                        rx.el.p("tools in the write-up", class_name="stat-label"),
                        rx.el.p("6", class_name="stat-value"),
                        class_name="stat",
                    ),
                    rx.el.div(
                        rx.el.p("remote-friendly", class_name="stat-label"),
                        rx.el.p("PDX", class_name="stat-value"),
                        class_name="stat",
                    ),
                    class_name="stats",
                ),
            ),
            _identity_card(),
            class_name="hero-grid",
        ),
        anchor="top",
    )


def projects() -> rx.Component:
    return panel(
        heading(
            "02  ·  work",
            "Tools with a point of view",
            rx.el.p(State.visible_count, " of 6", class_name="hint"),
        ),
        rx.el.p(
            "Filter by stack, then open a card for the brief.",
            class_name="section-copy",
        ),
        rx.el.div(
            *[
                rx.el.button(
                    tag,
                    type="button",
                    class_name=rx.cond(State.active_tag == tag, "chip chip-on", "chip"),
                    on_click=State.set_active_tag(tag),
                    aria_pressed=State.active_tag == tag,
                )
                for tag in TAGS
            ],
            class_name="filters",
            role="toolbar",
            aria_label="Filter projects by tag",
        ),
        rx.cond(
            State.visible_count == 0,
            rx.el.p("Nothing under that tag.", class_name="section-copy"),
            rx.el.div(
                *[project_card(project) for project in PROJECTS],
                class_name="cards",
            ),
        ),
        anchor="work",
    )


def skills() -> rx.Component:
    groups = ("Core", "Platform", "Interface")
    return panel(
        heading("03  ·  skills", "Working levels"),
        rx.el.p(
            "Not a leaderboard. A map of what I reach for.",
            class_name="section-copy",
        ),
        rx.el.div(
            *[
                skill_group(
                    group,
                    [skill for skill in SKILLS if skill["group"] == group],
                )
                for group in groups
            ],
            class_name="skill-grid",
        ),
        anchor="skills",
    )


def timeline() -> rx.Component:
    return panel(
        heading("04  ·  timeline", "Eight years, four chapters"),
        rx.el.div(*[job_item(job) for job in EXPERIENCE], class_name="timeline"),
        anchor="timeline",
    )


def terminal_section() -> rx.Component:
    return panel(
        heading("05  ·  shell", "mercer-sh"),
        rx.el.p(
            "A small interpreter. It knows this site and not much else.",
            class_name="section-copy",
        ),
        rx.el.div(
            _window_bar("kai@mercer:~"),
            rx.el.pre(State.terminal_log, id="term-log", class_name="term-log"),
            rx.el.form(
                rx.el.span("kai@mercer:~$", class_name="prompt"),
                rx.el.input(
                    name="cmd",
                    placeholder="help",
                    class_name="term-input",
                    aria_label="Terminal command",
                    auto_complete="off",
                    spell_check=False,
                ),
                on_submit=State.exec_terminal,
                reset_on_submit=True,
                class_name="term-form",
            ),
            class_name="term",
        ),
        rx.el.div(
            *[
                rx.el.button(
                    command,
                    type="button",
                    class_name="quick-btn",
                    on_click=State.run_command(command),
                )
                for command in QUICK_COMMANDS
            ],
            class_name="quick",
        ),
        anchor="terminal",
    )


def _labeled_field(
    label: str,
    field_id: str,
    control: rx.Component,
    note: rx.Component,
    required: bool = False,
) -> rx.Component:
    star = rx.el.span(" *", class_name="req", aria_hidden="true") if required else rx.fragment()
    return rx.el.div(
        rx.el.label(label, star, html_for=field_id, class_name="label"),
        control,
        note,
    )


def contact() -> rx.Component:
    form = rx.el.form(
        rx.el.div(
            rx.el.div(
                _labeled_field(
                    "Name",
                    "contact-name",
                    rx.el.input(
                        id="contact-name",
                        name="name",
                        on_change=State.set_contact_name,
                        auto_complete="name",
                        class_name="field",
                        max_length=80,
                    ),
                    field_note(State.error_name, State.name_ok, "At least 2 characters."),
                    required=True,
                ),
                _labeled_field(
                    "Email",
                    "contact-email",
                    rx.el.input(
                        id="contact-email",
                        name="email",
                        type="email",
                        on_change=State.set_contact_email,
                        auto_complete="email",
                        class_name="field",
                        max_length=120,
                    ),
                    field_note(State.error_email, State.email_ok, "name@domain."),
                    required=True,
                ),
                class_name="form-row",
            ),
            _labeled_field(
                "Company",
                "contact-company",
                rx.el.input(
                    id="contact-company",
                    name="company",
                    on_change=State.set_contact_company,
                    auto_complete="organization",
                    class_name="field",
                    max_length=80,
                ),
                rx.cond(
                    State.error_company != "",
                    rx.el.p(State.error_company, class_name="err"),
                    rx.el.p("Optional.", class_name="hint"),
                ),
            ),
            _labeled_field(
                "Message",
                "contact-message",
                rx.el.textarea(
                    id="contact-message",
                    name="message",
                    on_change=State.set_contact_message,
                    class_name="field",
                    rows="6",
                    max_length=2000,
                ),
                rx.el.div(
                    field_note(
                        State.error_message,
                        State.message_ok,
                        "At least 20 characters. Say what you want to build.",
                    ),
                    rx.el.p(State.contact_message.length(), " / 2000", class_name="hint"),
                ),
                required=True,
            ),
            class_name="form-grid",
        ),
        rx.el.div(
            rx.el.button("Send message", type="submit", class_name="btn btn-primary"),
            class_name="hero-actions",
        ),
        on_submit=State.submit_contact,
        no_validate=True,
    )
    receipt = rx.el.div(
        rx.el.pre(State.contact_receipt, class_name="receipt"),
        rx.el.div(
            rx.el.button(
                "Write another",
                type="button",
                class_name="btn btn-ghost",
                on_click=State.reset_contact,
            ),
            class_name="receipt-actions",
        ),
    )
    return panel(
        heading("06  ·  contact", "Send a note"),
        rx.el.p(
            "The form checks the note in this session. It does not send email.",
            class_name="section-copy",
        ),
        rx.cond(State.contact_sent, receipt, form),
        anchor="contact",
    )
