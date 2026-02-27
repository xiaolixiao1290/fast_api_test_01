# AGENTS.md

## Cursor Cloud specific instructions

This is a minimal single-file FastAPI project (`main.py`) with no database or external service dependencies.

### Services

| Service | Command | Port |
|---|---|---|
| FastAPI (uvicorn) | `python main.py` | 8000 |

### Key notes

- **Run/dev**: `python main.py` or `uvicorn main:app --reload` (hot-reload). See `README.md` for details.
- **Lint**: `ruff check main.py` (ruff is installed in the VM snapshot).
- **No automated tests** exist in the repo. Use `httpx` or `curl` to verify endpoints (`/`, `/current_time`, `/docs`).
- **PATH**: uvicorn installs to `~/.local/bin`; ensure `export PATH="$HOME/.local/bin:$PATH"` is set if commands are not found.
- **No `.env` or secrets** are required to run this project.
