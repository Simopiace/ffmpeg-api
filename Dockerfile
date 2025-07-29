FROM python:3.10-slim

RUN apt-get update && apt-get install -y ffmpeg

WORKDIR /app
COPY . .

RUN pip install flask

EXPOSE 8080

CMD ["python", "main.py"]
