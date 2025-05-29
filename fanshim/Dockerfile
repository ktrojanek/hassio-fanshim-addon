ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest
FROM ${BUILD_FROM}

ENV LANG C.UTF-8

RUN apk add --no-cache py3-pip && \
    pip install --break-system-packages fanshim psutil RPi.GPIO

COPY run.py /run.py
COPY rootfs /  # Skopiuje plik `run` do /etc/services.d/
