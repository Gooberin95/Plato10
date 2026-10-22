"""Fixed painting, vertical nav, and the page shell."""

from __future__ import annotations

import reflex as rx

from portfolio.components.blocks import project_dialog
from portfolio.state import State

NAV = (
    ("top", "overview", "compass"),
    ("work", "work", "folder-git-2"),
    ("skills", "skills", "gauge"),
    ("timeline", "timeline", "milestone"),
    ("terminal", "shell", "terminal"),
    ("contact", "contact", "mail"),
)


def _section_class(section: str):
    return rx.cond(
        (State.router.url.path == "/") & (State.active_section == section),
        "nav-btn active",
        "nav-btn",
    )


def _sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.button(
            rx.icon("x", size=16, color="currentColor"),
            "Close",
            type="button",
            class_name="sidebar-close",
            on_click=State.close_nav,
        ),
        rx.el.a(
            rx.el.span("KM", class_name="brand-mark"),
            rx.el.span(
                rx.el.span("Kai Mercer", class_name="brand-name"),
                rx.el.span("python developer", class_name="brand-role"),
                class_name="brand-text",
            ),
            href="/",
            class_name="brand",
        ),
        rx.el.nav(
            *[
                rx.el.button(
                    rx.icon(icon, size=16, color="currentColor"),
                    label,
                    type="button",
                    class_name=_section_class(section),
                    on_click=State.goto(section),
                )
                for section, label, icon in NAV
            ],
            rx.el.a(
                rx.icon("file-text", size=16, color="currentColor"),
                "resume",
                href="/resume",
                class_name=rx.cond(
                    State.router.url.path == "/resume",
                    "nav-btn active",
                    "nav-btn",
                ),
            ),
            aria_label="Sections",
            class_name="nav",
            id="site-nav",
        ),
        rx.el.div(
            rx.el.p(
                rx.el.span(class_name="status-dot", aria_hidden="true"),
                "open for contracts",
                class_name="status",
            ),
            rx.el.p("winter 2026 · portland", class_name="side-meta"),
            class_name="side-foot",
        ),
        class_name=rx.cond(State.nav_open, "sidebar open", "sidebar"),
    )


def _topbar() -> rx.Component:
    return rx.el.header(
        rx.el.button(
            rx.icon("menu", size=18, color="currentColor"),
            "Menu",
            type="button",
            class_name="menu-btn",
            on_click=State.toggle_nav,
            aria_expanded=State.nav_open,
            aria_controls="site-nav",
        ),
        rx.el.a("Kai Mercer", href="/", class_name="topbar-name"),
        rx.el.span("py 3.14", class_name="topbar-meta"),
        class_name="topbar",
    )


def shell(*children) -> rx.Component:
    """Root frame. The painting is applied once, here, and stays fixed."""
    return rx.box(
        rx.el.a("Skip to content", href="#top", class_name="skip"),
        _sidebar(),
        rx.cond(
            State.nav_open,
            rx.el.button(
                aria_label="Close menu",
                class_name="scrim",
                type="button",
                on_click=State.close_nav,
            ),
        ),
        _topbar(),
        rx.el.main(
            rx.el.div(*children, class_name="column"),
            class_name="main",
            id="content",
        ),
        project_dialog(),
        class_name="page-root",
        background_color="#070b14",
        background_image="url('/background.jpg')",
        background_size="cover",
        background_position="center",
        background_attachment="fixed",
        background_repeat="no-repeat",
        min_height="100vh",
        width="100%",
    )
