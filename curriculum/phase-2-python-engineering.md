# Phase 2: Python Engineering

**Days 11–20 · Outcome:** turn scripts into a typed, tested, installable Python package that behaves predictably when data, networks, or configuration are imperfect.

Create a `phase-2` branch. The milestone is the first real component of Grounded: its document-ingestion package.

## Day 11: Reproducible Python projects

**Learn:** Python interpreters, virtual environments, packages, dependency resolution, `pyproject.toml`, lockfiles, application versus library dependencies, and semantic version constraints.

**Build:** Initialize `packages/ingestion` using one modern workflow such as `uv` or standard `venv` plus `pip`. Declare runtime and development dependencies separately. Pin the Python version and commit the resolved lockfile when your chosen tool produces one.

**Ship:** Document four commands: create the environment, install dependencies, run the program, and run checks.

**Check:** Delete only the disposable virtual environment, recreate it from declared files, and get the same result.

**Resources:** [Python virtual environments](https://docs.python.org/3/tutorial/venv.html) · [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/) · [uv projects](https://docs.astral.sh/uv/guides/projects/)

## Day 12: Data, functions, and comprehensions

**Learn:** Mutability, strings, bytes, lists, tuples, dictionaries, sets, slicing, iteration, comprehensions, functions, scope, iterators, and generators. Prefer explicit readable code over clever one-liners.

**Build:** Implement pure functions that normalize whitespace, count words, extract simple metadata, and split text into bounded chunks. Use generators when processing many files so memory use does not grow with the full collection.

**Ship:** A `text.py` module with docstrings and examples covering empty text, Unicode, and large input.

**Check:** Run the functions twice on the same input and confirm they do not depend on global state.

**Resources:** [The Python tutorial](https://docs.python.org/3/tutorial/) · [Python data structures](https://docs.python.org/3/tutorial/datastructures.html) · [Python glossary: iterator](https://docs.python.org/3/glossary.html#term-iterator)

## Day 13: Modules, errors, and logging

**Learn:** Modules and imports, public interfaces, exception types, exception chaining, cleanup with context managers, and structured logging. Errors should carry useful context without exposing secrets.

**Build:** Organize ingestion into `readers`, `models`, and `pipeline` modules. Define meaningful exceptions for unsupported format and invalid content. Replace debug `print` calls with standard logging and include stable event names, file identifiers, and durations.

**Ship:** A failure demonstration that produces an actionable log and preserves the original exception as its cause.

**Check:** Normal command output and diagnostic logs use separate streams; a malformed file does not crash the entire batch unless fail-fast is requested.

**Resources:** [Python errors and exceptions](https://docs.python.org/3/tutorial/errors.html) · [Python logging HOWTO](https://docs.python.org/3/howto/logging.html) · [Python context managers](https://docs.python.org/3/reference/datamodel.html#context-managers)

## Day 14: Files, JSON, and HTTP clients

**Learn:** Text encodings, `pathlib`, context-managed I/O, JSON serialization, HTTP clients, explicit timeouts, retries with backoff, status handling, pagination, and idempotency.

**Build:** Add local text/Markdown readers and a command that fetches a document from an allow-listed URL. Set connect/read timeouts, cap response size, validate content type, identify the client, and handle non-success status codes. Save normalized metadata as JSON.

**Ship:** Tests using temporary directories and a mocked HTTP transport; tests must not depend on the public internet.

**Check:** Simulate a timeout, `404`, invalid UTF-8, oversized response, and malformed JSON.

**Resources:** [Python `pathlib`](https://docs.python.org/3/library/pathlib.html) · [HTTPX quickstart](https://www.python-httpx.org/quickstart/) · [MDN HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

## Day 15: Types, models, and validation

**Learn:** Type hints, unions, protocols, generics at a practical level, dataclasses, schema validation, serialization, and the rule that external input is untrusted until validated.

**Build:** Define a `Document` model with stable ID, title, source, media type, content, timestamps, and metadata. Validate URL schemes, empty content, timestamp formats, and metadata size. Separate the external input schema from the internal domain type when their guarantees differ.

**Ship:** Generate a JSON Schema or equivalent contract and include valid and invalid examples.

**Check:** Static analysis understands your main pipeline without broad `Any` types or blanket ignore comments.

**Resources:** [Python typing](https://docs.python.org/3/library/typing.html) · [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) · [mypy getting started](https://mypy.readthedocs.io/en/stable/getting_started.html)

## Day 16: Tests and test-driven debugging

**Learn:** Test boundaries, arrange/act/assert, unit versus integration tests, parametrization, fixtures, mocks, coverage as a signal rather than a target, and regression tests.

**Build:** Write tests for chunking boundaries, validation, duplicate files, error handling, and the complete local ingestion path. Introduce one bug deliberately, reproduce it with a failing test, fix it, and retain the regression test.

**Ship:** A test suite runnable with one command and free from time, network, execution-order, or local-machine dependencies.

**Check:** A new contributor can read each test name and understand the behavior promised by the package.

**Resources:** [pytest getting started](https://docs.pytest.org/en/stable/getting-started.html) · [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) · [Test doubles from *Architecture Patterns with Python*](https://www.cosmicpython.com/book/chapter_03_abstractions.html)

## Day 17: Quality automation

**Learn:** Formatting, linting, import checks, static type checking, test coverage, pre-commit hooks, and why automated style frees reviews to focus on design and correctness.

**Build:** Configure Ruff for formatting and linting, mypy or Pyright for types, and pytest for tests. Add a `make check`, task-runner command, or script that runs every quality gate in the same order locally and in CI.

**Ship:** Run the checks across the repository, fix findings intentionally, and document the rare rule exception next to its configuration.

**Check:** One malformed file or type error makes the quality command fail with a non-zero exit code.

**Resources:** [Ruff documentation](https://docs.astral.sh/ruff/) · [mypy documentation](https://mypy.readthedocs.io/en/stable/) · [pre-commit](https://pre-commit.com/)

## Day 18: Configuration, secrets, and architecture

**Learn:** Separation of config from code, dependency inversion, composition roots, environment-specific settings, secret handling, and the difference between domain, application, and infrastructure code.

**Build:** Load configuration once at startup into a validated settings object. Add `.env.example` containing names and safe placeholders only. Pass file readers and output stores into the ingestion service rather than constructing them deep inside business logic.

**Ship:** Write an ADR explaining the package boundaries and configuration choice using the [ADR template](../templates/adr.md).

**Check:** Searching Git history finds no credential; a missing required setting causes a clear startup error.

**Resources:** [The Twelve-Factor App: config](https://12factor.net/config) · [OWASP secrets management cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) · [Cosmic Python: dependency inversion](https://www.cosmicpython.com/book/chapter_04_service_layer.html)

## Day 19: CLI design and packaging

**Learn:** Command interfaces, arguments versus options, stdin/stdout/stderr, exit codes, discoverable help, entry points, package builds, and versioning.

**Build:** Expose `grounded-ingest` with `ingest`, `validate`, and `stats` commands. Add `--help`, `--version`, machine-readable JSON output, a quiet mode, and useful exit codes. Ensure user errors are concise while debug mode preserves diagnostics.

**Ship:** Build a wheel and install it into a clean virtual environment. Run it from outside the source directory.

**Check:** Pipe JSON output into another program and confirm logs do not corrupt it.

**Resources:** [Python Packaging User Guide](https://packaging.python.org/) · [Typer documentation](https://typer.tiangolo.com/) · [Command Line Interface Guidelines](https://clig.dev/)

## Day 20: Milestone document ingestion package

**Build:** Finish an ingestion package that reads local Markdown/text and one safe HTTP source, normalizes metadata, chunks content deterministically, detects duplicates, and writes newline-delimited JSON. It must continue past a bad input by default and summarize successes and failures.

**Required quality:** Typed public interfaces, schema validation, structured logs, deterministic tests, no network in unit tests, locked dependencies, a CLI, useful exit codes, and a documented configuration surface.

**Ship:** Open a milestone PR with test/coverage output, sample input and output, the architecture decision, and known limitations. Build the package from a clean checkout, merge, and tag `day-20`.

**Demo:** Ingest a small mixed collection twice. The second run should not create duplicate logical documents, and one malformed item should produce an understandable failure record.

**Resources:** [JSON Lines format](https://jsonlines.org/) · [Semantic Versioning](https://semver.org/) · [Python package metadata](https://packaging.python.org/en/latest/specifications/pyproject-toml/)

## Phase 2 exit ticket

Explain where validation happens, how a failure crosses module boundaries, which tests are isolated, how dependencies are reproduced, and why a secret cannot enter Git. Then install and run the package from a clean environment.
