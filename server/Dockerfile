# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /src

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]