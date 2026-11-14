# HACKSERIES

A multi-part learning and event-web workspace containing React/Vite projects and a small Flask API exercise.

## Repository layout

- `react/` — React + Vite application
- `Props/` — separate React + Vite application
- `hackseries-flask/` — Flask API practice application
- `.gitignore` — repository ignore rules

Each frontend folder has its own `package.json`. Install dependencies from the folder you intend to run, not from the repository root.

## Run the React application

Choose one frontend:

```bash
cd react
npm install
npm run dev
```

Or:

```bash
cd Props
npm install
npm run dev
```

Both frontend projects define `dev`, `build`, `lint`, and `preview` scripts. Run checks from the selected folder:

```bash
npm run build
npm run lint
```

## Run the Flask practice API

```bash
cd hackseries-flask
python -m venv .venv
```

Activate the environment, then install Flask:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
python app.py
```

The API binds to localhost by default. Available routes include `/`, `/test`, `/user`, `/notes`, and `/addnote`. Note data is stored in memory and is cleared when the process restarts.

## Flask API regression tests

Run the API tests from the repository root:

```bash
python -m unittest discover -s hackseries-flask -p "test_*.py" -v
```

The tests cover route registration, note creation, reading, updating, deletion, and invalid request handling. The Flask API is a learning exercise with in-memory storage, not a production persistence layer.

## Development checklist

- Confirm which of the two frontend folders is the intended event site before deploying.
- Test responsive behavior and navigation.
- Verify event dates, registration links, and contact details.
- Keep API behavior and frontend integration documented.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).
