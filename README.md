# Project info
This project is a simple API written with FASTAPI framework. The api itself counts cars in a given `.mp4` video.

For creating and managing migrations Alembic is used. For connecting with the database SQLAlchemy is used.
# Live Demo
Live demo is available at: https://fastapi-project-f3cnqnjvta-ew.a.run.app/
# Development
This project was written with `python 3.10.2`. To start developing make sure to have Docker and Docker Compose installed.

To run the development version run the command:
```
docker compose up
```
This will run a Postgres database as well as the application.
The application will be running on `127.0.0.1:80`.

# Code Quality
Tool called `pre-commit` is used to help with making sure the quality of the code is good. To use it create an environment with:
```
python -m venv .venv
```
Then access the created environment (exact command depends on your operating system, check python documentation):
```
source .venv/bin/activate
```
and install requirements:
```
pip install -r requirements.txt
```
Lastly install the `pre-commit` hooks:
```
pre-commit install
```
Make sure to commit with the environment active in case some of the hooks will use installed libraries.
# API
API docs can be found at `/docs` endpoint, e.g.: https://fastapi-project-f3cnqnjvta-ew.a.run.app/docs for the live demo
