FROM python:3.11.9-slim-bullseye

WORKDIR app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY moulmahal /app

# Set environment variables for superuser details
ENV SUPERUSER_USERNAME=myadmin
ENV SUPERUSER_EMAIL=admin@example.com
ENV SUPERUSER_PASSWORD=password123

# RUN chmod +x ./run_server.sh


ENTRYPOINT python manage.py runserver