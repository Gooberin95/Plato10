# Kai Mercer

A personal portfolio and resume for **Kai Mercer**, a fictional Python developer in Portland. The site is a [Reflex](https://reflex.dev) app: filters, the shell, the typewriter, and the contact form are Python state.

The whole page sits on one abstract painting. It is applied once, on the page root, with `background_size="cover"`, `background_position="center"`, and `background_attachment="fixed"`, so it stays put while the sections scroll. Panels use a dark translucent background and a backdrop blur so the type stays readable and the painting still shows through.

## Python version

This project targets **Python 3.14.4**.

Reflex **0.10.0** (pinned in `requirements.txt`) requires Python `>=3.11, <4`. Python 3.14 support landed in Reflex 0.8.15 and is still supported in 0.10.0, so 3.14.4 is the version to use. It is also recorded in `.python-version`.

## Run it on Ubuntu

These steps assume a normal Ubuntu machine with `curl` and `ca-certificates`. Ubuntu 24.04 does not ship CPython 3.14, so install **3.14.4** first. [uv](https://docs.astral.sh/uv/) places a `python3.14` command on your PATH.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"
uv python install 3.14.4
python3.14 --version
```

`python3.14 --version` should print `Python 3.14.4`.

Clone the repo and start the app:

```bash
git clone https://github.com/Gooberin95/Plato10.git
cd Plato10
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
reflex run
```

Open **http://localhost:3000**.

The resume is at **http://localhost:3000/resume**. Reflex also starts an API on port 8000; the page you want is port 3000. The first `reflex run` downloads the frontend toolchain and can take a few minutes. Stop the server with Ctrl+C.

### `reflex init`

You do not need `reflex init` for this repo. `rxconfig.py`, the `portfolio` package, and `assets/` are already here.

Run `reflex init` only if you have deleted those files and want Reflex to scaffold a blank app. It can overwrite this portfolio, so skip it when you just want to run the site.

## What is on the site

- A terminal-style hero. One line types itself out.
- Projects you can filter by tech tag, with a detail dialog for each one.
- Skill bars, an experience timeline, and a resume page that uses the same shell.
- `mercer-sh`, a small shell. Try `help`, `about`, `projects`, `skills`, `neofetch`, and `open work`.
- A contact form that checks the name, email, and message and tells you when something is wrong. It does not send mail. Kai, the employers, and the projects are fictional.

The painting is `assets/background.jpg`. Outfit and JetBrains Mono live in `assets/fonts/` so the page does not depend on a font CDN.

## Layout

```
rxconfig.py
requirements.txt
.python-version
assets/
portfolio/
  portfolio.py    # app entry
  state.py
  data.py
  pages/
  components/
```
