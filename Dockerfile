FROM python:3.6-slim-buster
MAINTAINER hungvv

COPY requirements.txt /app/
COPY src/ /app/src/
COPY data/ /app/data/
COPY image_predicting_server.py /app/image_predicting_server.py

RUN apt-get update && apt-get install -y \
  libgl1-mesa-glx \
  && rm -rf /var/lib/apt/lists/*

RUN pip install -r /app/requirements.txt
# RUN pip install vietocr==0.3.2
# RUN pip install torch
# RUN pip install torchvision
# RUN pip install PyYAML
# RUN pip install flask
# RUN pip install gunicorn

WORKDIR /app

CMD gunicorn --bind=0.0.0.0:5000 --workers=2 image_predicting_server:app
