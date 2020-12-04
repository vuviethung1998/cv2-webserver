FROM python:3.6-slim-buster
MAINTAINER hungvv

RUN apt-get update && apt-get install -y build-essential  \
  && apt-get install -y libgl1-mesa-glx \
  && apt-get install -y libgtk2.0-dev \
  && rm -rf /var/lib/apt/lists/*

#RUN pip install -r /app/requirements.txt
RUN pip install vietocr==0.3.2
RUN pip install torch
RUN pip install torchvision
RUN pip install PyYAML
RUN pip install flask
RUN pip install gunicorn

COPY requirements.txt /app/
COPY src/ /app/src/
COPY data/ /app/data/
COPY image_predicting_server.py /app/image_predicting_server.py

WORKDIR /app
# CMD gunicorn --bind=0.0.0.0:5000 --workers=5 image_predicting_server:app
CMD ["python3", "./image_predicting_server.py"]
