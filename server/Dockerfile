# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory to /app
WORKDIR /src

ENV PYTHONUNBUFFERED=1

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]