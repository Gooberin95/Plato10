"""Reflex entrypoint for the Kai Mercer portfolio."""

import reflex as rx

from portfolio.pages import index, not_found, resume
from portfolio.state import State

app = rx.App(
    stylesheets=["/portfolio.css"],
    style={
        "font_family": '"Outfit", "Avenir Next", "Segoe UI", sans-serif',
        "color": "#e9fff4",
    },
)

_META = [{"name": "theme-color", "content": "#07110c"}]

app.add_page(
    index,
    route="/",
    title="Kai Mercer · Python developer",
    description="Portfolio of Kai Mercer, a Python developer in Portland. Tools, streams, and internal apps.",
    on_load=[State.focus_hash, State.play_intro],
    meta=_META,
)
app.add_page(
    resume,
    route="/resume",
    title="Resume · Kai Mercer",
    description="Resume for Kai Mercer, Python developer. Experience, tools, and skills.",
    meta=_META,
)
app.add_page(
    not_found,
    route="/404",
    title="Not found · Kai Mercer",
    description="That path is not on Kai Mercer's site.",
)
