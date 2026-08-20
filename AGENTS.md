# AGENTS.md

## Project overview

This repository is a small Python library named `picklejar`. Its purpose is to store multiple pickled Python objects inside a single file (a "jar") and read them back in order.

The implementation resides in a single module:
- `picklejar.py`

The test suite lives in:
- `tests/test_picklejar.py`

The package metadata and tool configuration live in:
- `pyproject.toml`
- `Makefile`

## Core guidance for agents

- Keep changes minimal and focused on the library behavior in `picklejar.py`.
- Prefer preserving the public API of the `Jar` class unless a change explicitly requires a breaking update.
- Maintain compatibility with Python 3.10+ as declared in `pyproject.toml`.
- Treat the project as a library, not an application or service. There is no web app, backend server, or UI layer to update.
- Prefer adding or updating tests in `tests/test_picklejar.py` for any behavior change.
- Always use the repository-local `.venv` environment for Python package installation, dependency setup, and running unit tests. Do not install modules or execute Python commands with the system interpreter when `.venv` is available.
- When invoking Python directly, prefer `.venv/bin/python` or `.venv/bin/pytest` rather than bare `python` or `pytest`.

## Repository conventions

### Python version and packaging
- The project targets Python `>3.10,<4.0`.
- Packaging uses `hatchling` and the source distribution includes only `picklejar.py`.
- Dependencies are managed via `uv` and Python dependency groups in `pyproject.toml`.
- This repository expects a local virtual environment at `.venv`; use it consistently for package installs and test execution.

### Dependency groups
- `test`: pytest, coverage, ruff, ty, mock, discover
- `docs`: sphinx

### Lint and quality checks
The project defines the following workflow in `Makefile`:

- `make install` installs the package.
- `make test` runs the test suite.
- `make lint` runs `ruff check picklejar.py` and `ty check picklejar.py`.
- `make docs` builds Sphinx docs.
- `make coverage` runs tests and writes HTML coverage.

## Standard validation commands

Run the most relevant checks before finishing a change. Prefer using the `.venv` environment; for example:

```bash
. .venv/bin/activate
make test
make lint
```

If you are making a packaging or documentation change, also consider:

```bash
. .venv/bin/activate
make docs
```

If a command needs to invoke Python explicitly, use `.venv/bin/python` rather than the system `python`.

## Test expectations

- Tests are written with `unittest` and executed under `pytest`.
- The suite is intentionally small and focused around jar read/write behavior.
- New behavior should usually be covered by a corresponding unit test.
- Keep tests deterministic and avoid using external services or environment-specific assumptions.

## Implementation notes

- The main API is the `Jar` class defined in `picklejar.py`.
- `Jar.dump()` writes pickles to a file; `new_jar=True` overwrites the jar, while the default appends.
- `Jar.load()` reads pickles until end-of-file and returns either:
  - a single object when only one pickle exists, or
  - a list of objects when multiple pickles exist,
  - with `always_list=True` forcing a list return even for single-object jars.
- `collapse=True` is a special-case behavior where a list is pickled as a single object instead of one pickle per element.

## Working style

- Keep comments concise and useful.
- Preserve compatibility with the module’s current semantics unless a bug fix requires a compatible change.
- Avoid introducing heavy dependencies or new architecture layers.
- Favor straightforward Python code over abstraction for a single-file library.

## Contribution expectations

- The project’s README states that contributions should target the `develop` branch.
- When fixing bugs or adding features, include a focused regression test in the existing suite.
- Prefer surgical changes that match the current style of the project.

## Quick sanity checklist

Before considering work complete, verify:

1. The change is limited to the relevant library behavior.
2. Tests still pass with `make test`.
3. Linting still passes with `make lint`.
4. Any new behavior has test coverage.
5. No unrelated files or broad refactors were introduced.
