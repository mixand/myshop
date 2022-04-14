FROM python:3.10

RUN mkdir -p /usr/src/myshop/

WORKDIR /usr/src/myshop/

COPY . /usr/src/myshop/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]