# Base image
FROM python:3.10-slim

# Install bash
RUN apt-get update && apt-get install -y bash && apt-get clean

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY django_project /app

# Expose port for Django
EXPOSE 8000

# Start Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
