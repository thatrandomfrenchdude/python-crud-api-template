# CRUD API Template using FASTAPI with PostgreSQL Database and Docker

This is a base CRUD API template using FASTAPI with a PostgreSQL database, dockerized using Docker Compose. The template includes a separate service for running database migrations using Alembic.

## Getting Started

1. Clone the repository to your local machine.
2. Build and start the containers using `docker-compose up --build`.
3. Access the API documentation at `http://localhost:8000/docs`.

## Extending the Template

To extend this template for a new project, follow these steps:

1. Modify the `crud_api_template.py` file to include your own data models and API endpoints.
2. Update the `init.sql` file to include any initial data required for your application.
3. Create new migration scripts using Alembic by running `alembic revision --autogenerate` in the `app` directory.
4. Update the `docker-compose.yml` file to include any additional services required for your application.

## Running Migrations

The migrations are run automatically when the `migrations` service starts. To run the migrations manually, you can use the following command:

```bash
docker-compose run migrations sh -c "alembic upgrade head"
```

## API Documentation

The API documentation is available at `http://localhost:8000/docs`. You can use this documentation to explore the available API endpoints and test them using the built-in Swagger UI.
