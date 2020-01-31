# Select environment
FROM python:3.7

# Copy the files needed into the /app DIR in the docker container
COPY . /app

# Set /app as to WD
WORKDIR /app

# Install the requirements using pip
RUN pip install -r requirements.txt

# Opens up port 5000 to the network
EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]