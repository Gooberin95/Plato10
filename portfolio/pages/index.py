"""Portfolio home."""

import reflex as rx

from portfolio.components.blocks import site_footer
from portfolio.components.home import (
    contact,
    hero,
    projects,
    skills,
    terminal_section,
    timeline,
)
from portfolio.components.shell import shell


def index() -> rx.Component:
    return shell(
        hero(),
        projects(),
        skills(),
        timeline(),
        terminal_section(),
        contact(),
        site_footer(),
    )
