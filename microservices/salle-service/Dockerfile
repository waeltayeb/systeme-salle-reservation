FROM python:3.10-slim


RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app


COPY . .


RUN pip install --upgrade pip && pip install -r requirements.txt


ENV FLASK_APP=app.py
ENV FLASK_ENV=development

EXPOSE 5002


CMD ["flask", "run", "--host=0.0.0.0", "--port=5002"]
