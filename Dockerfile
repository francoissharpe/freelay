FROM python:3.9

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 80

COPY freelay freelay

CMD ["uvicorn", "freelay:app", "--host", "0.0.0.0", "--port", "80"]
