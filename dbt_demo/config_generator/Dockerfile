FROM python:3.9.16-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY config_generator.py config_generator.py

CMD ["python", "config_generator.py"]