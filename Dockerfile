FROM python:3.10

WORKDIR /Gobikrish07

COPY requirements.txt /

RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "app.py" ]
