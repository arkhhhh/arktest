# Use Python official image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the Python script into the container
COPY deploy_job.py /app/

# Command to run the script
CMD ["python", "deploy_job.py"]

