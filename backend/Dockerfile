# Use Python 3.10 slim image
FROM python:3.10.12-slim

# Set environment variables to prevent .pyc files and buffered output
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Update and upgrade system packages, install curl
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends gcc curl && \
    apt-get upgrade -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN python -m pip install --upgrade pip

# Set the working directory
WORKDIR /work

# Copy the src directory
COPY src ./src

# Copy application files
COPY requirements/build.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Create a user for running the application
RUN useradd appuser && chown -R appuser /work
USER appuser

# Expose the correct port
EXPOSE 8000

# Command to run the FastAPI app with uvicorn
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]

