# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app
COPY . /app/

# Expose the port the app runs on
EXPOSE 5010

# Command to run the app
CMD ["gunicorn", "--config", "gunicorn_config.py", "wsgi:app"]

