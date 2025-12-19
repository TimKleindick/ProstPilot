# ProstPilot Agent Guidelines

The highlights below are the minimum bar for
agents executing tasks in this repository.

## Commit and Branch Discipline

- Use conventional commit messages (`feat:`, `fix:`, `docs:`, `test:`,
  `refactor:`).
- Keep pull requests focused; open a new branch per topic (e.g.
  `feature/short-description`).

## Environment and Tooling

- Target Python 3.12+ for backend work and install dependencies via
  `pip install -r backend/requirements/base.txt`.
- Install and respect `pre-commit` hooks; run `pre-commit run --all-files` when
  touching any files.
- Frontend lives in `frontend/` and uses Node 20+, Vite, React 19, Redux Toolkit,
  Vitest, and Storybook. Run `npm install` inside `frontend/` before any JS work.
- Use the existing workspace layout (`src/app`, `src/features`, `src/ui`, `src/shared`)
  and keep shared UI in `src/shared/components` while feature-specific components
  stay inside `src/features/<feature>/components`.

## Coding Standards

- Prefer clear, explicit code to clever abstractions. When intent is not
  immediately obvious, add concise English comments or docstrings.
- Backend: run `ruff check`, `ruff format`, and `mypy` before opening a PR. Fix
  warnings instead of silencing them unless absolutely necessary.
- Frontend: respect the TypeScript configs (`tsconfig.base.json`, `tsconfig.json`)
  and ESLint flat config (`eslint.config.mjs`). Do not add ad-hoc configs in
  feature folders.
- Use the provided npm scripts from `frontend/package.json`:  
  `npm run format`, `npm run lint`, `npm run typecheck`, `npm run test`, and
  `npm run storybook`. Prettier is the source of truth for formatting.
- Keep new dependencies rare and document why they are required.

## Testing Expectations

- Backend: add or extend tests in `tests/` for every behavioral change and run
  `python -m pytest` locally.
- Frontend: unit tests live under `frontend/tests/` and component stories under
  `frontend/src/stories/`. Use Vitest (`npm run test`) for logic and the
  Storybook playground for UI verification. Keep Redux slices/components covered
  where behavior changes.
- Exercise edge cases, async behavior, and Django or React integrations when
  relevant.

## Documentation Duties

- Update `docs/`, README, or changelog entries whenever user-facing behavior
  changes. Ensure examples remain accurate.
- Use clear language and formatting consistent with existing documentation.

## Issue and Release Hygiene

- Reference existing GitHub issues or create one before starting significant
  work to avoid duplication.
- Do not modify version numbers manually; semantic-release handles tagging and
  PyPI publishing based on your commit history.
