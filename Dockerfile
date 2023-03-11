FROM python:3.10.8

WORKDIR /Gobikrish07

COPY requirements.txt ./

RUN pip install -r requirements.txt

copy . .

CMD [ "python3", "app.py" ]
