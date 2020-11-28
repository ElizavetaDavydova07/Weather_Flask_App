FROM python:3.6.12

WORKDIR /server

# Устанавливаем зависимости приложения
COPY ./requirements.txt /server/requirements.txt
RUN pip install -r /server/requirements.txt

# Копируем код приложения
COPY ./app /server/app

ENV FLASK_APP=app.app:app

CMD flask run --host 0.0.0.0 --port ${PORT:-8000} --reload
