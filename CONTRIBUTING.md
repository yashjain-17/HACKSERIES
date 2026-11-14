# Contributing to HACKSERIES

This repository contains separate frontend projects and a Flask learning API.

## Choose the correct project

- React application: work inside `react/`.
- Props application: work inside `Props/`.
- Flask API exercise: work inside `hackseries-flask/`.

Install dependencies and run commands from the selected project folder. Do not combine package manifests or lockfiles across the two Vite applications.

## Frontend quality

- Run `npm run build` and `npm run lint` in the folder changed.
- Check responsive layouts, navigation, forms, and external links.
- Keep event dates, registration details, and contact information accurate.

## Flask quality

- Use route decorators correctly and validate request bodies.
- Do not use Flask debug mode in public deployments.
- Add tests for successful and invalid requests.

## Pull requests

State which subproject changed, include test results, and add screenshots for user-interface changes.
