# Use an official Python runtime as a base image  
FROM python:3.10-slim  
  
# Set the working directory inside the container  
WORKDIR /app  
  
# Copy requirements file first (for faster builds if dependencies don't change)  
COPY requirements.txt .  
  
# Install dependencies  
RUN pip install --no-cache-dir -r requirements.txt  
  
# Copy the rest of your application code  
COPY . .  
  
# Command to run the Python application  
CMD ["python", "app.py"]  
