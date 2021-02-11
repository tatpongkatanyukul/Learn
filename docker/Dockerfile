FROM python:3

WORKDIR /ship1

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./data .

CMD ["python", "main.py"]
