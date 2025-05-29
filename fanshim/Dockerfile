ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-addon-base:latest
FROM ${BUILD_FROM}

ENV LANG C.UTF-8

RUN apk add --no-cache py3-pip && \
    pip install --break-system-packages fanshim psutil RPi.GPIO

COPY run.py /run.py
COPY rootfs/ /
