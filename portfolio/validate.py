"""Contact form checks. Pure functions, no Reflex state."""

from __future__ import annotations

import hashlib
import re

EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


def name_error(value: str) -> str:
    text = value.strip()
    if len(text) < 2:
        return "Name needs at least 2 characters."
    if len(text) > 80:
        return "Name should be under 80 characters."
    return ""


def email_error(value: str) -> str:
    text = value.strip()
    if not text:
        return "Email is required."
    if len(text) > 120 or EMAIL_RE.fullmatch(text) is None:
        return "That email doesn't look quite right."
    return ""


def company_error(value: str) -> str:
    if len(value.strip()) > 80:
        return "Company should be under 80 characters."
    return ""


def message_error(value: str) -> str:
    text = value.strip()
    if len(text) < 20:
        return "Message should be at least 20 characters."
    if len(text) > 2000:
        return "Message should be under 2000 characters."
    return ""


def build_receipt(name: str, email: str, company: str, message: str) -> str:
    token = hashlib.sha1(f"{name}|{email}|{message}".encode()).hexdigest()[:4].upper()
    company_line = f"company    {company}\n" if company else ""
    preview = message if len(message) <= 180 else message[:177] + "..."
    return (
        "queued locally\n"
        f"ref        KM-{token}\n"
        "to         kai@kaimercer.dev\n"
        f"from       {name} <{email}>\n"
        f"{company_line}"
        f"note       {preview}\n"
        "status     checked, not sent\n"
        "\n"
        "This demo validates the note and keeps it in your session.\n"
        "No mail is sent."
    )
