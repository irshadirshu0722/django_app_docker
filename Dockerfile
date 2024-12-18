# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the entire Django project into the container's /app directory
COPY . /app/

# Expose the necessary port for the Django application
EXPOSE 8000

# Run migrations, collect static files, and start the Gunicorn server
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn django_app.wsgi:application --bind 0.0.0.0:8000"]
