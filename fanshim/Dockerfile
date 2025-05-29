ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base-python:3.12
FROM ${BUILD_FROM}

ENV LANG C.UTF-8

RUN pip install fanshim psutil RPi.GPIO

COPY run.py /run.py

CMD ["python3", "/run.py"]
