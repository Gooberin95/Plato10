"""Printable-feeling resume on the same shell."""

import reflex as rx

from portfolio.components.blocks import (
    heading,
    job_item,
    panel,
    project_row,
    site_footer,
    skill_group,
)
from portfolio.data import EDUCATION, EXPERIENCE, NOW, PROJECTS, SKILLS, SUMMARY
from portfolio.components.shell import shell


def resume() -> rx.Component:
    groups = ("Core", "Platform", "Interface")
    return shell(
        panel(
            rx.el.p("resume", class_name="kicker"),
            rx.el.h1("Kai Mercer", class_name="h1"),
            rx.el.p("Python developer", class_name="lede"),
            rx.el.ul(
                rx.el.li("Portland, Oregon"),
                rx.el.li("kai@kaimercer.dev"),
                rx.el.li("github.com/kaimercer"),
                rx.el.li("Booking contracts for winter 2026"),
                class_name="meta-list",
            ),
            rx.el.p(SUMMARY, class_name="section-copy"),
            rx.el.div(
                rx.el.a("← Overview", href="/", class_name="btn btn-ghost"),
                class_name="hero-actions",
            ),
            anchor="top",
        ),
        panel(
            heading("Experience", "Where the years went"),
            rx.el.div(*[job_item(job) for job in EXPERIENCE], class_name="timeline"),
        ),
        panel(
            heading("Selected work", "Open a row for the brief"),
            rx.el.div(
                *[project_row(project) for project in PROJECTS],
                class_name="project-list",
            ),
        ),
        panel(
            heading("Skills", "Working levels"),
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
        ),
        panel(
            heading("Also", "School and right now"),
            rx.el.h3(EDUCATION["credential"], class_name="tl-title"),
            rx.el.p(
                f"{EDUCATION['school']} · {EDUCATION['years']}",
                class_name="tl-org",
            ),
            rx.el.p(EDUCATION["note"], class_name="section-copy"),
            rx.el.h3("Currently", class_name="group-title"),
            rx.el.ul(*[rx.el.li(item) for item in NOW], class_name="now-list"),
        ),
        site_footer(),
    )
