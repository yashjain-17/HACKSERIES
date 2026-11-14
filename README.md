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
pip install Flask
python app.py
```

The API is configured to run locally on Flask's default development port. The current routes include `/`, `/test`, `/notes`, and `/addnote`.

## Known issue in Flask exercise

The `/user` function currently uses `app.route("/user")` without the decorator marker `@`. It is therefore not registered as a Flask route. Also, `debug=True` is for local development only and must not be used in a public deployment.

## Development checklist

- Confirm which of the two frontend folders is the intended event site before deploying.
- Test responsive behavior and navigation.
- Verify event dates, registration links, and contact details.
- Keep API behavior and frontend integration documented.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).
