FROM python:3

EXPOSE 5000

WORKDIR /usr/src/library-api

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-u", "./src/run.py"]
