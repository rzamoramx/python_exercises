# Use an appropriate base image
FROM python:3.11-alpine

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY .. .

# Install application dependencies
RUN pip install -r requirements.txt

# Specify the command to run the Flask server
CMD ["python", "consumer_oauth2.py"]
