FROM python:3.7-slim
ADD app.py app.py
ADD requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
COPY static/ /static
COPY templates/ /templates

EXPOSE 8000

CMD ["gunicorn", "--bind=0.0.0.0:8000", "app:app"]