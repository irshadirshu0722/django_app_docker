# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app
COPY ./django_app ./

# Install system dependencies
RUN pip install --upgrade pip --no-cache-dir

# Install Python dependencies
RUN pip install -r requirements.txt

# Run migrations, collect static files, and start the Gunicorn server
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn django_app.wsgi:application --bind 0.0.0.0:8000"]
