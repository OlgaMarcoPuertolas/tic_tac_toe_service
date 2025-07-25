# Using a lightweight Python image
FROM python:3.10-slim

# Create and define the working directory
WORKDIR /app

# Copy all project contents
COPY . .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose port 5000 
EXPOSE 5000

# Run the app
CMD ["python", "run.py"]