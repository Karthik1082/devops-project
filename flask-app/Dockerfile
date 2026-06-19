FROM python:3.11-slim

WORKDIR /app

COPY app.py /app/

RUN pip install flask gunicorn

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
