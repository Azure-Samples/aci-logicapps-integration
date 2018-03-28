FROM python:2

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY app.py ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]