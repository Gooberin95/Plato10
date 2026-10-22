"""Unknown paths, still on the painting."""

import reflex as rx

from portfolio.components.blocks import panel, site_footer
from portfolio.components.shell import shell


def not_found() -> rx.Component:
    return shell(
        panel(
            rx.el.p("404", class_name="kicker"),
            rx.el.h1("That path is not in the tree.", class_name="h1"),
            rx.el.p(
                "The shell can list what exists. From the overview, try ls.",
                class_name="lede",
            ),
            rx.el.div(
                rx.el.a("Overview", href="/", class_name="btn btn-primary"),
                rx.el.a("Resume", href="/resume", class_name="btn btn-ghost"),
                class_name="hero-actions",
            ),
            anchor="top",
        ),
        site_footer(),
    )
