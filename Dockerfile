# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from your project folder into the container
COPY . .

# Run the Python application
CMD ["python", "calendar_app.py"]