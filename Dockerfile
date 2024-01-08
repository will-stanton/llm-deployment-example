from python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /code/app
COPY ./chatbot.py /code/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]


