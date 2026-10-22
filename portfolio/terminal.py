"""Command replies for the mercer-sh toy shell."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from zoneinfo import ZoneInfo

from portfolio.data import EXPERIENCE, PROFILE, PROJECTS, SKILLS, SUMMARY, TERMINAL_BANNER

HELP = """\
commands
  help                 show this list
  about                who Kai is
  projects             list the work
  skills               print the bars
  experience           career, one line each
  contact              how to reach Kai
  resume               open the resume page
  neofetch             a small identity card
  ls                   what this site contains
  open <place>         jump to work, skills, timeline,
                       terminal, contact, or resume
  echo <text>          repeat yourself
  date                 time in Portland
  history              commands you have run
  clear                wipe the scrollback
  whoami, pwd, theme   the short ones
  github, email        handles
  sudo <anything>      a polite no"""

ABOUT = (
    SUMMARY
    + "\n\nCurrently booking contract work for winter 2026.\n"
    + "Favorite bug: the one the status command explains."
)

PLACES = {
    "work": "work",
    "projects": "work",
    "skills": "skills",
    "timeline": "timeline",
    "experience": "timeline",
    "terminal": "terminal",
    "shell": "terminal",
    "contact": "contact",
    "top": "top",
    "overview": "top",
    "home": "top",
    "resume": "resume",
}


@dataclass(frozen=True)
class Reply:
    output: str
    clear: bool = False
    go: str = ""


def _bar(level: int) -> str:
    filled = max(0, min(10, round(level / 10)))
    return "█" * filled + "░" * (10 - filled)


def _now() -> str:
    try:
        moment = datetime.now(ZoneInfo("America/Los_Angeles"))
    except Exception:
        moment = datetime.now()
    return moment.strftime("%a %b %d %H:%M:%S %Z %Y").strip()


def answer(raw: str, history: list[str]) -> Reply:
    text = raw.strip()
    if not text:
        return Reply("")
    parts = text.split(maxsplit=1)
    cmd = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else ""

    if cmd in {"help", "man", "commands", "?"}:
        return Reply(HELP)
    if cmd == "about":
        return Reply(ABOUT)
    if cmd == "projects":
        lines = [
            f"{str(project['name']):<14}{project['year']}  {project['blurb']}"
            for project in PROJECTS
        ]
        lines.append("\nopen work   to see the cards. click one for the brief.")
        return Reply("\n".join(lines))
    if cmd == "skills":
        lines = [
            f"{str(skill['name']):<14}{_bar(int(skill['level']))}  {skill['level']}"
            for skill in SKILLS
        ]
        return Reply("\n".join(lines))
    if cmd in {"experience", "jobs", "timeline"}:
        lines = [
            f"{str(job['years']):<16}{job['title']} · {job['org']}" for job in EXPERIENCE
        ]
        return Reply("\n".join(lines), go="timeline" if cmd == "timeline" else "")
    if cmd == "contact":
        return Reply(
            f"{PROFILE['email']}\nThe form checks the note and keeps it in this session.",
            go="contact",
        )
    if cmd == "resume":
        return Reply("opening resume.", go="resume")
    if cmd in {"open", "cd", "goto"}:
        if not arg:
            return Reply("usage: open work|skills|timeline|terminal|contact|resume")
        key = arg.split()[0].lower().strip("/")
        target = PLACES.get(key)
        if target == "resume":
            return Reply("opening resume.", go="resume")
        if target:
            return Reply(f"opening {key}.", go=target)
        return Reply("unknown place. try work, skills, timeline, terminal, contact, resume")
    if cmd == "neofetch":
        return Reply(
            "\n".join(
                [
                    "       .-.      kai mercer",
                    "      (py)      ----------",
                    "      |14|      role    python developer",
                    "       '-'      base    portland, oregon",
                    "                book    winter 2026",
                    "                stack   python · postgres · reflex",
                    "                shell   mercer-sh",
                    "                py      3.14.4",
                ]
            )
        )
    if cmd == "ls":
        return Reply("work/   skills/   timeline/   terminal/   contact/   resume/")
    if cmd == "echo":
        return Reply(arg if arg else "")
    if cmd == "date":
        return Reply(_now())
    if cmd == "history":
        if not history:
            return Reply("no history yet")
        lines = [f"{index:>3}  {item}" for index, item in enumerate(history, start=1)]
        return Reply("\n".join(lines))
    if cmd == "clear":
        return Reply("", clear=True)
    if cmd == "whoami":
        return Reply("kai mercer")
    if cmd == "pwd":
        return Reply("/home/kai/portfolio")
    if cmd == "theme":
        return Reply("accent  #3dff9a  electric mint\ncanvas  the painting, fixed while you scroll")
    if cmd == "github":
        return Reply("github.com/kaimercer\n(fictional handle — there is no account)")
    if cmd == "email":
        return Reply(f"{PROFILE['email']}\n(fictional address — use the contact form)")
    if cmd in {"python", "python3", "python3.14"}:
        return Reply(
            "Python 3.14.4 (portfolio)\n>>> Kai.role\n'python developer'\n>>> "
        )
    if cmd == "pip":
        return Reply("requirements.txt pins reflex==0.10.0. this shell does not install packages.")
    if cmd == "banner":
        return Reply(TERMINAL_BANNER.rstrip("\n"))
    if cmd in {"exit", "quit", "logout"}:
        return Reply("no logout here. clear wipes the scrollback.")
    if cmd in {"sudo", "rm", "shutdown", "reboot", "poweroff"}:
        return Reply("denied. the painting is load-bearing.")
    return Reply(f"{cmd}: command not found. type help.")
