# CRUD API Template using FASTAPI with PostgreSQL Database and Docker

**IMPORTANT NOTE: This repo has been generated using the new Llama API from Meta using the `Llama-4-Maverick-17B-128E-Instruct-FP8` model to test functionality. Your mileage may vary.**

This is a base CRUD API template using FASTAPI with a PostgreSQL database, dockerized using Docker Compose. The template includes a separate service for running database migrations using Alembic.

## Getting Started

1. Clone the repository to your local machine.
2. Create a virtual environment and install the required dependencies:
   ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r app/requirements.txt
    ```
3. Initialize Alembic by running the following command in the app directory:
   ```bash
   cd app
   alembic init alembic
   ```
   Replace the generated `alembic.ini` file with the following configuration:
   ```
   sqlalchemy.url = postgresql://postgres:password@localhost/crud_api_template
   ```
   Update the `target_metadata` variable in `alembic/env.py` to point to your SQLAlchemy metadata:
   ```python
   from crud_api_template import metadata
   target_metadata = metadata
   ```
4. Create the initial migration script:
   ```bash
   alembic revision --autogenerate
   ```
5. Build and start the containers using `docker-compose up --build`.
6. Access the API documentation at `http://localhost:8000/docs`.

## Extending the Template

To extend this template for a new project, follow these steps:
1. Modify the `crud_api_template.py` file to include your own data models and API endpoints.
2. Update the `init.sql` file to include any initial data required for your application.
3. Create new migration scripts using `alembic revision --autogenerate` in the app directory.
4. Update the `docker-compose.yaml` file to include any additional services required for your application.

## Running Migrations

The migrations are run automatically when the migrations service starts. To run the migrations manually, you can use the following command:
```bash
docker-compose run migrations sh -c "alembic upgrade head"
```

## Alembic Configuration

Alembic is used to manage database schema migrations. To use Alembic, you'll need to initialize it and configure it to point to your database.

## API Documentation

The API documentation is available at `http://localhost:8000/docs`. You can use this documentation to explore the available API endpoints and test them using the built-in Swagger UI.
