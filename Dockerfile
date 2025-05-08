FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY app/requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/ .

# Expose the port
EXPOSE 8000

# Run the command to start the development server
CMD ["uvicorn", "crud_api_template:app", "--host", "0.0.0.0", "--port", "8000"]
