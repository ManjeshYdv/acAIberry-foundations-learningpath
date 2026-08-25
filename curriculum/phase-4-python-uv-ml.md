# Phase 4: Python, uv, and ML Basics

**Days 31–40 · Result:** you can create a reproducible Python project, read and validate small data, test code, train a basic text classifier, and expose one prediction endpoint.

The goal is not advanced machine learning. It is understanding the simplest complete path from data to a running model.

## Day 31: Create a Python project with uv

**Goal:** Let the project declare and reproduce its Python version and dependencies.

**Commands:** `cd ticket-classifier`, `uv init --package .`, `uv python pin`, `uv run`, `uv sync`.

**Task:** Enter `ticket-classifier`, initialize it as a packaged `uv` project, pin a supported Python version, and run Python through `uv`. Commit `pyproject.toml`, `.python-version`, `src/ticket_classifier/__init__.py`, and `uv.lock` when present; do not commit `.venv`.

**Done when:** Another clean environment can run `cd ticket-classifier`, `uv sync`, and `uv run python -c "import ticket_classifier"`.

**Resource:** [uv project guide](https://docs.astral.sh/uv/guides/projects/)

## Day 32: Practice Python values and functions

**Goal:** Use strings, numbers, booleans, conditionals, and functions clearly.

**Commands:** `uv run python`, `python -m`.

**Task:** Create `src/ticket_classifier/text.py` with functions that clean whitespace, reject empty text, and count words. Open Python through `uv run python`, import the functions, and call them with three sample tickets.

**Done when:** You can explain each argument, return value, condition, and type without the assistant.

**Resource:** [Python tutorial: an informal introduction](https://docs.python.org/3/tutorial/introduction.html)

## Day 33: Use lists, dictionaries, and loops

**Goal:** Store several tickets and summarize them.

**Commands:** Python through `uv run`.

**Task:** Create `src/ticket_classifier/data.py`. Represent each ticket as a dictionary with `text` and `label`, store several dictionaries in a list, loop over them, and count labels in a dictionary.

**Done when:** `uv run python -m ticket_classifier.data` prints the total ticket count and count for each label.

**Resource:** [Python data structures](https://docs.python.org/3/tutorial/datastructures.html)

## Day 34: Read CSV and JSON data

**Goal:** Load structured data and check its shape before using it.

**Commands:** `uv add pandas`, `head`, `wc -l`, `uv run python`.

**Task:** Create `data/tickets.csv` with at least 30 synthetic tickets divided among `billing`, `account`, and `technical`. Extend `data.py` to read it with pandas, validate required columns, and show missing values, duplicates, and label counts. Export the summary as JSON.

**Done when:** The script rejects missing required columns and your note explains rows, columns, labels, missing values, and duplicates.

**Resources:** [pandas getting started](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html) · [Python JSON](https://docs.python.org/3/library/json.html)

## Day 35: Add useful errors and logs

**Goal:** Fail clearly and log useful context without exposing ticket text unnecessarily.

**Commands:** Python `logging`, `try`, `except`, `raise`.

**Task:** Add logs for data load start, row count, label counts, and completion. Raise a clear error for a missing file, missing column, or empty dataset. Trigger each error once and read the traceback and logs.

**Done when:** `logs/training.log` helps locate the failure and does not dump secrets or complete user text.

**Resource:** [Python logging HOWTO](https://docs.python.org/3/howto/logging.html)

## Day 36: Write basic tests with pytest

**Goal:** Turn expected behavior and fixed bugs into repeatable checks.

**Commands:** `uv add --dev pytest`, `uv run pytest`, `uv run pytest -q`.

**Task:** Test text cleanup, empty-text rejection, word count, valid CSV loading, and one invalid CSV. Use temporary files rather than editing real project data during a test.

**Done when:** All tests pass, and intentionally breaking one function makes the related test fail for the right reason.

**Resource:** [pytest getting started](https://docs.pytest.org/en/stable/getting-started.html)

## Day 37: Learn features, labels, and data splits

**Goal:** Understand input features, target labels, training data, and test data.

**Commands:** `uv add scikit-learn`, Python through `uv run`.

**Task:** Use ticket text as the input and category as the label. Split the dataset into training and test sets with a fixed random seed and stratification. Print only counts and label distributions.

**Done when:** `notes/ml-basics.md` explains feature, label, training set, test set, leakage, and why the test set is kept separate.

**Resource:** [scikit-learn: train/test split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

## Day 38: Train and evaluate a text classifier

**Goal:** Build a simple baseline and inspect mistakes rather than chase a perfect score.

**Commands:** scikit-learn `Pipeline`, `TfidfVectorizer`, `LogisticRegression`, `classification_report`.

**Task:** Train a TF-IDF plus logistic-regression pipeline. Evaluate it on the held-out test data and print accuracy, precision, recall, and the misclassified examples.

**Done when:** `notes/model-results.md` records the data size, split, metrics, at least one error, and why results from this tiny synthetic dataset are not production proof.

**Resource:** [scikit-learn text-classification example](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html)

## Day 39: Save the model and predict from the CLI

**Goal:** Separate training from inference and keep model/code versions together.

**Commands:** `uv add joblib`, `uv run python -m ticket_classifier.train`, `uv run python -m ticket_classifier.predict`.

**Task:** Save the fitted pipeline to an ignored `artifacts/` directory. Create a CLI that loads it and predicts one supplied ticket. Add a clear error when the model file is missing.

**Done when:** Training once and running three separate predictions works, and the model artifact is not accidentally committed.

**Resource:** [scikit-learn: model persistence](https://scikit-learn.org/stable/model_persistence.html)

## Day 40: Checkpoint serve predictions with FastAPI

**Goal:** Put a small HTTP boundary around the same tested prediction function.

**Commands:** `uv add fastapi uvicorn`, `uv add --dev httpx`, `uv run uvicorn ticket_classifier.api:app`, `curl`.

**Task:** Create `src/ticket_classifier/api.py` with `GET /health` and `POST /predict`. Validate that text is present and bounded, call the saved classifier, and return the category. Add API tests using FastAPI's test client.

**Done when:** `curl` receives `200` for a valid prediction, invalid input receives a useful `4xx`, tests pass, and the terminal shows a request log.

**Resources:** [FastAPI first steps](https://fastapi.tiangolo.com/tutorial/first-steps/) · [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/)

### Phase checkpoint

From a clean environment, run `uv sync`, test the code, train the model, start the API, and request a prediction. Explain the data path from CSV row to HTTP response.
