# Use an official Python runtime as a parent images
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 9001

# Define environment variable
ENV NAME FlaskApp

# Run app.py when the container launches
CMD ["sh", "-c", "cd /app && python app.py"]
