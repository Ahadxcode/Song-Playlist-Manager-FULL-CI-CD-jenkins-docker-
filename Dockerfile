# syntax=docker/dockerfile:1
FROM python:3.12-slim AS base


ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1


# Create non-root user
RUN useradd -ms /bin/bash appuser
WORKDIR /app


# Install runtime deps (none required for stdlib-only app)
# If you later add packages, list them in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copy source
COPY . .


# Ensure files owned by non-root user
RUN chown -R appuser:appuser /app
USER appuser


# Default command runs the CLI app
CMD ["python", "playlist_manager.py
