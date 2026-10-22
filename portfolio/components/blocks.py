"""Shared panels, project dialog, skills, and timeline."""

from __future__ import annotations

import reflex as rx

from portfolio.data import PROJECTS
from portfolio.state import State


def panel(*children, anchor: str = "", extra: str = "") -> rx.Component:
    props: dict = {"class_name": f"panel {extra}".strip()}
    if anchor:
        props["id"] = anchor
    return rx.el.section(*children, **props)


def heading(kicker: str, title: str, aside: rx.Component | None = None) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(kicker, class_name="kicker"),
            rx.el.h2(title, class_name="h2"),
        ),
        aside if aside is not None else rx.fragment(),
        class_name="section-head",
    )


def site_footer() -> rx.Component:
    return rx.el.footer(
        rx.el.p("Kai Mercer · Portland, Oregon · winter 2026"),
        rx.el.p(
            "Fictional portfolio. The employers, projects, and addresses are invented. Built with Reflex."
        ),
        class_name="footer",
    )


def field_note(error, ok, hint: str) -> rx.Component:
    return rx.cond(
        error != "",
        rx.el.p(error, class_name="err"),
        rx.cond(
            ok,
            rx.el.p("Looks good.", class_name="hint ok"),
            rx.el.p(hint, class_name="hint"),
        ),
    )


def _tag_match(project: dict):
    show = State.active_tag == "All"
    for tag in project["tags"]:
        show = show | (State.active_tag == tag)
    return show


def project_card(project: dict) -> rx.Component:
    tags = " · ".join(str(tag) for tag in project["tags"])
    return rx.cond(
        _tag_match(project),
        rx.el.article(
            rx.el.button(
                rx.el.span(
                    rx.el.span(project["name"], class_name="card-name"),
                    rx.el.span(project["year"], class_name="card-year"),
                    class_name="card-top",
                ),
                rx.el.span(project["status"], class_name="card-status"),
                rx.el.span(project["blurb"], class_name="card-blurb"),
                rx.el.span(tags, class_name="card-tags"),
                rx.el.span("Open brief →", class_name="card-open"),
                type="button",
                class_name="card-btn",
                on_click=State.open_project(project["id"]),
            )
        ),
    )


def project_row(project: dict) -> rx.Component:
    tags = " · ".join(str(tag) for tag in project["tags"])
    return rx.el.button(
        rx.el.span(
            rx.el.span(str(project["name"]), class_name="row-name"),
            rx.el.span(str(project["year"]), class_name="row-year"),
            class_name="row-top",
        ),
        rx.el.span(str(project["blurb"]), class_name="row-blurb"),
        rx.el.span(tags, class_name="card-tags"),
        type="button",
        class_name="project-row",
        on_click=State.open_project(str(project["id"])),
    )


def _project_detail(project: dict) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            f"{project['year']}  ·  {project['role']}  ·  {project['status']}",
            class_name="modal-meta",
        ),
        rx.el.p(str(project["summary"]), class_name="modal-summary"),
        rx.el.h3("What it does", class_name="group-title"),
        rx.el.ul(
            *[rx.el.li(str(point)) for point in project["highlights"]],
            class_name="hls",
        ),
        rx.el.div(
            *[rx.el.span(str(tag), class_name="chip") for tag in project["tags"]],
            class_name="filters",
        ),
        rx.el.p("Invented for this portfolio.", class_name="hint"),
        class_name="modal-body",
    )


def project_dialog() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title(State.selected_name, class_name="modal-title"),
            rx.dialog.description(State.selected_blurb, class_name="section-copy"),
            *[
                rx.cond(State.selected_id == str(project["id"]), _project_detail(project))
                for project in PROJECTS
            ],
            rx.el.div(
                rx.dialog.close(
                    rx.el.button("Close", type="button", class_name="btn btn-ghost")
                ),
                class_name="modal-actions",
            ),
            class_name="modal",
            style={
                "background": "rgba(7, 12, 20, 0.94)",
                "backdrop_filter": "blur(18px)",
                "border": "1px solid rgba(61, 255, 154, 0.35)",
                "border_radius": "18px",
                "color": "#e9fff4",
                "max_width": "640px",
            },
        ),
        open=State.modal_open,
        on_open_change=State.on_modal_change,
    )


def skill_row(skill: dict) -> rx.Component:
    level = int(skill["level"])
    return rx.el.div(
        rx.el.div(
            rx.el.span(str(skill["name"]), class_name="skill-name"),
            rx.el.span(str(level), class_name="skill-level"),
            class_name="skill-top",
        ),
        rx.el.div(
            rx.el.div(
                class_name="bar-fill",
                style={"width": f"{level}%", "--level": f"{level}%"},
            ),
            class_name="bar",
            role="img",
            aria_label=f"{skill['name']} {level} out of 100",
        ),
        rx.el.p(str(skill["note"]), class_name="skill-note"),
        class_name="skill-row",
    )


def skill_group(title: str, skills: list[dict]) -> rx.Component:
    return rx.el.div(
        rx.el.h3(title, class_name="group-title"),
        *[skill_row(skill) for skill in skills],
        class_name="skill-group",
    )


def job_item(job: dict) -> rx.Component:
    return rx.el.article(
        rx.el.p(str(job["years"]), class_name="tl-years"),
        rx.el.div(
            rx.el.h3(str(job["title"]), class_name="tl-title"),
            rx.el.p(f"{job['org']} · {job['place']}", class_name="tl-org"),
            rx.el.ul(
                *[rx.el.li(str(point)) for point in job["points"]],
                class_name="tls",
            ),
            class_name="tl-body",
        ),
        class_name="tl-item",
    )
