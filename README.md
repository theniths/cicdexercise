# cicdexercise

A small Python project with password-strength checks, wired for CI/CD with CircleCI.

## Repo setup

### Prerequisites

- **Python 3.11** (or compatible 3.x)
- **Git**

### Local setup

1. **Clone the repo** (if you don’t have it yet):

   ```bash
   git clone <your-repo-url>
   cd cicdexercise
   ```

2. **Create and activate a virtual environment** (recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   # or:  .venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the linter** (same as CircleCI):

   ```bash
   flake8 src
   ```

5. **Run tests**:

   ```bash
   pytest tests
   ```

### Project layout

- `src/` — application code (e.g. `password-strength.py`)
- `tests/` — unit tests
- `requirements.txt` — Python dependencies (pytest, flake8)
- `.circleci/config.yml` — CircleCI pipeline definition

---

## GitHub setup

1. **Create a new repository** on [GitHub](https://github.com/new).  
   - Choose a name (e.g. `cicdexercise`).  

2. **Connect your local repo** (if it isn’t already):

   ```bash
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   ```

3. **Push your branch**:

   ```bash
   git push -u origin main
   ```

4. **Use GitHub as the source of truth** for branches and pull requests; CircleCI will run on pushes and PRs once the project is enabled in CircleCI.

---

## CircleCI rules and pipeline

- **Config file:** `.circleci/config.yml`  
- **Orb / config version:** CircleCI 2.1

### When it runs

- The pipeline runs on **every push** and **every pull request** to the default branch (and any branch you’ve enabled in the project settings).

### Pipeline: `test_pipeline`

Single workflow that runs one job: **`build`**.

### Job: `build`

Runs in a **Docker** environment:

- **Image:** `cimg/python:3.11`

**Steps (in order):**

1. **Checkout** — clone the repo.
2. **Install dependencies** — `pip install -r requirements.txt`.
3. **Run linter** — `flake8 src` (must pass; same as local).
4. **Run unit tests** — `pytest tests`.

### Rules to keep CI green

- **Linting:** All code under `src/` must pass `flake8` (PEP 8 style). Fix any flake8 errors before pushing.
- **Tests:** All tests in `tests/` must pass. Add or update tests when changing behavior.
- **Config:** Do not remove or rename `.circleci/config.yml`; changing steps (e.g. extra jobs or commands) is fine as long as the project still runs `flake8 src` and `pytest tests` in a compatible way.

### Enabling CircleCI for this repo

1. Sign in at [CircleCI](https://circleci.com) (with your GitHub account).
2. Go to **Projects** and **Set Up Project** for this GitHub repo.
3. Choose the option that uses the existing `.circleci/config.yml` (no need to add a new config).
4. Push a commit; the first pipeline will run automatically.
