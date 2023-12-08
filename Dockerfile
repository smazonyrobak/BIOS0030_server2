# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the start script and make it executable
COPY start.sh .
RUN chmod +x start.sh

# Make ports 8000 and 8866 available to the world outside this container
EXPOSE 8000 8866

# Define environment variable
ENV NAME World

# Run start.sh when the container launches
CMD ["./start.sh"]
