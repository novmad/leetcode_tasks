FROM mcr.microsoft.com/devcontainers/python:1-3.11-buster
WORKDIR /usr/src

# Install the xz-utils package
RUN apt-get update \
    && apt-get install -y xz-utils openssh-client

# RUN python -m venv /opt/venv
# ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip

COPY requirements.txt /usr/src
RUN pip install -r requirements.txt

COPY . /usr/src
ENV C_FORCE_ROOT=1