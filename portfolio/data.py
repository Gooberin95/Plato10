"""Fictional portfolio content for Kai Mercer."""

from __future__ import annotations

PROFILE = {
    "name": "Kai Mercer",
    "role": "Python developer",
    "location": "Portland, Oregon",
    "email": "kai@kaimercer.dev",
    "github": "github.com/kaimercer",
    "availability": "Booking contracts for winter 2026",
    "years": "8",
}

INTRO_LINE = "I build Python that stays calm when the data does not."

SUMMARY = (
    "Kai Mercer is a Python developer who has spent eight years on data "
    "platforms and the tools around them. He started at Fieldnote, moved to "
    "Harbor Labs, and was a staff engineer on Northline's ingest team. He now "
    "works independently from Portland, building streaming jobs, CLIs that "
    "explain themselves, and the occasional Reflex console."
)

TERMINAL_BANNER = (
    "mercer-sh  ·  Kai Mercer\n"
    "type help    try: about, projects, neofetch, open work\n"
)

SECTIONS = ("top", "work", "skills", "timeline", "terminal", "contact")

TAGS = [
    "All",
    "Python",
    "asyncio",
    "PostgreSQL",
    "Reflex",
    "CLI",
    "Testing",
    "Tooling",
    "Pydantic",
    "Slack",
    "UI",
]

PROJECTS: list[dict[str, object]] = [
    {
        "id": "riverbed",
        "name": "Riverbed",
        "year": "2025",
        "role": "Author",
        "status": "Active",
        "blurb": "Streaming ETL that backpressures instead of falling over.",
        "summary": (
            "Riverbed is a small library for moving data through async workers "
            "without an unbounded queue. Each stage pulls, checkpoints, and can "
            "explain its lag in one sentence."
        ),
        "highlights": [
            "Bounded memory on multi-gigabyte feeds",
            "Postgres sink with idempotency keys",
            "A status command that names the slow stage",
        ],
        "tags": ["Python", "asyncio", "PostgreSQL"],
    },
    {
        "id": "flint",
        "name": "Flint",
        "year": "2024",
        "role": "Author",
        "status": "Maintained",
        "blurb": "Snapshot tests for CLIs. Run the tool, read the diff, accept it.",
        "summary": (
            "Flint records what a command prints and fails the build when the "
            "text changes. It started as a script on the Northline on-call "
            "tooling and stayed because the reviews were faster."
        ),
        "highlights": [
            "Works with argparse and click entry points",
            "Diffs stdout, stderr, and the exit code",
            "Used on every operational CLI at Northline",
        ],
        "tags": ["Python", "CLI", "Testing"],
    },
    {
        "id": "lumen",
        "name": "Lumen Desk",
        "year": "2025",
        "role": "Builder",
        "status": "Active",
        "blurb": "An ops console in Reflex for people who live in the ticket queue.",
        "summary": (
            "Lumen Desk is an internal console: failed jobs, queue depth, and a "
            "replay button that asks before it retries. It replaced a spreadsheet "
            "that had become load-bearing."
        ),
        "highlights": [
            "One screen for failures, lag, and the last good run",
            "SSO that matches the company's existing login",
            "Replay with a typed reason, stored next to the job",
        ],
        "tags": ["Reflex", "Python", "UI"],
    },
    {
        "id": "keel",
        "name": "Keel",
        "year": "2023",
        "role": "Author",
        "status": "Maintained",
        "blurb": "Schema migrations that say what they will lock before they lock it.",
        "summary": (
            "Keel plans a migration, estimates the lock, and refuses a table "
            "rewrite over a size threshold unless you pass a flag you have to "
            "type out. The point is to make the dangerous path feel heavy."
        ),
        "highlights": [
            "Dry-run prints lock risk in plain language",
            "Splits unsafe alters into expand and contract",
            "Stops a rewrite on a large table without --i-mean-it",
        ],
        "tags": ["Python", "PostgreSQL", "Tooling"],
    },
    {
        "id": "nightwatch",
        "name": "Nightwatch",
        "year": "2024",
        "role": "Author",
        "status": "Shipped",
        "blurb": "A Slack digest that pages a human only when the graphs would.",
        "summary": (
            "Nightwatch rolls noisy alerts into one overnight note and links the "
            "runbook, not just the stack trace. It is a single asyncio process "
            "on purpose."
        ),
        "highlights": [
            "Quiet hours from 22:00 to 07:00 local",
            "Groups repeats of the same failure",
            "The page includes the last successful checkpoint",
        ],
        "tags": ["Python", "Slack", "asyncio"],
    },
    {
        "id": "parcel",
        "name": "Parcel",
        "year": "2022",
        "role": "Author",
        "status": "Maintained",
        "blurb": "Typed config. One file, pydantic models, and a loader that names the bad key.",
        "summary": (
            "Parcel loads layered configuration and fails with the key it "
            "disliked. Secrets stay in the environment. A explain command shows "
            "which file won."
        ),
        "highlights": [
            "Environment overlays without mystery precedence",
            "Errors cite the file, the key, and the expected type",
            "parcel explain answers why this value is here",
        ],
        "tags": ["Python", "Pydantic", "Tooling"],
    },
]

SKILLS: list[dict[str, object]] = [
    {
        "name": "Python",
        "level": 96,
        "group": "Core",
        "note": "Daily driver since the Fieldnote years.",
    },
    {
        "name": "asyncio",
        "level": 86,
        "group": "Core",
        "note": "Streams, small networked tools, and one patient bot.",
    },
    {
        "name": "Testing",
        "level": 91,
        "group": "Core",
        "note": "pytest, snapshots, and contracts at the edges.",
    },
    {
        "name": "Pydantic",
        "level": 85,
        "group": "Core",
        "note": "The boundary of the program, written down.",
    },
    {
        "name": "PostgreSQL",
        "level": 88,
        "group": "Platform",
        "note": "Schemas, locks, and explain plans.",
    },
    {
        "name": "Linux",
        "level": 84,
        "group": "Platform",
        "note": "Deploys, systemd, and logs without panic.",
    },
    {
        "name": "Docker",
        "level": 78,
        "group": "Platform",
        "note": "Packaging. Not a personality.",
    },
    {
        "name": "Reflex",
        "level": 80,
        "group": "Interface",
        "note": "Internal tools with a real UI.",
    },
    {
        "name": "CLI design",
        "level": 83,
        "group": "Interface",
        "note": "Help text is a feature.",
    },
    {
        "name": "TypeScript",
        "level": 62,
        "group": "Interface",
        "note": "Enough to review a frontend. Not enough to pretend.",
    },
]

EXPERIENCE: list[dict[str, object]] = [
    {
        "years": "2024 — now",
        "title": "Independent",
        "org": "Mercer Studio",
        "place": "Portland · remote",
        "points": [
            "Contract Python for data platforms and the consoles beside them.",
            "Kept Riverbed's checkpoint format small enough to document on one page.",
            "Shipped Lumen Desk for an ops team that had outgrown its spreadsheet.",
        ],
    },
    {
        "years": "2021 — 2024",
        "title": "Staff engineer",
        "org": "Northline",
        "place": "Remote",
        "points": [
            "Led the streaming ingest group, six engineers, one billing feed.",
            "Cut lag on that feed from minutes to seconds by pulling, not queuing.",
            "Put snapshot tests on every operational CLI before the next incident.",
        ],
    },
    {
        "years": "2018 — 2021",
        "title": "Backend engineer",
        "org": "Harbor Labs",
        "place": "Seattle",
        "points": [
            "Python services for a research data portal used by two labs.",
            "Owned the Postgres schema, the workers, and a calmer auth path.",
            "Mentored two new grads through their first on-call rotation.",
        ],
    },
    {
        "years": "2016 — 2018",
        "title": "Junior developer",
        "org": "Fieldnote",
        "place": "Portland",
        "points": [
            "First job: Django internals, then a split into smaller services.",
            "Learned to like boring deploys and readable migrations.",
            "Wrote the team's first command that explained its own failure.",
        ],
    },
]

EDUCATION = {
    "school": "Portland State University",
    "credential": "B.S. Computer Science",
    "years": "2012 — 2016",
    "note": "Capstone on a queue that shed load instead of falling over. The interest stuck.",
}

NOW = [
    "Booking contract work for winter 2026.",
    "Keeping Riverbed's checkpoint format boring and written down.",
    "Building small Reflex consoles for teams that outgrew a spreadsheet.",
]

QUICK_COMMANDS = ("help", "about", "projects", "neofetch", "skills")
