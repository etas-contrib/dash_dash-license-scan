# dash-licenses-cli

[![PyPI](https://img.shields.io/pypi/v/dash-licenses-cli.svg)](https://pypi.org/project/dash-licenses-cli/)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

A thin Python CLI wrapper for [eclipse-dash/dash-licenses](https://github.com/eclipse-dash/dash-licenses).  
It makes the official JAR easier to use via modern Python workflows (`pipx`, `uvx`) and adds helpers for lockfile conversion.

---

## State

Proof of Concept. Do not use in production environments.

---

## Features

- 🔧 Bundles `dash-licenses` JAR, behaves as one tool
- 🚀 Run the JAR via a simple CLI (`uvx dash-license-scan`)  
- 📦 Convert lock files into `dash-licenses` input:
  - `requirements.txt`
  - `Cargo.lock`
- ⚡ Works with [`pipx`](https://pypa.github.io/pipx/) or [`uvx`](https://docs.astral.sh/uv/concepts/tools/)  

---

## Installation

System Requirements:
* you have uvx or pipx installed.
* you jave Java >= 11 installed (e.g. openjdk-21-jre-headless)

Commands you need to run. NO FURTHER INSTALLATION.

* To scan a python lockfile run: `uvx dash-license-scan --pypi path/to/requirements.txt`
* To scan a cargo lockfile run: `uvx dash-license-scan --crate path/to/Cargo.lock`

* To submit a clearance append your token: `uvx dash-license-scan --pypi path/to/requirements.txt --token=...`


---

## Why a python wrapper?

Sounds rather stupid, doesn't it? I could have extended the Java Code instead?

Well there are reasons, but you may not like them:

* Last time I wrote Java is 20 years ago
* I wanted to finally write a proper python executable
* I wanted one-line usability, as with uvx / pipx. Or versioning via pip / uv, which most projects probably do anyway.

So basically this is not for everyone!
But if it helps me, it might help you.

---

## Design Decisions

### 1) No external dependencies
Version pinning is simplified considerably, when there are no 3rd party dependencies.
