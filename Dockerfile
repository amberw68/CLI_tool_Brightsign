FROM python:3.9.13

WORKDIR /app

COPY get_loc.py ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "./get_loc.py"]
