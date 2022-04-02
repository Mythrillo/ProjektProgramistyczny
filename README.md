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
# API
API docs can be found at `/docs` endpoint, e.g.: https://fastapi-project-f3cnqnjvta-ew.a.run.app/docs for the live demo
