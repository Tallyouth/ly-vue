# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:alpine

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=ly-vue Version=0.0.1
EXPOSE 8000

WORKDIR /root/ly-vue
ADD . /root/ly-vue

# Using pip:
RUN pip install --upgrade setuptools && \
    python -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt

WORKDIR /root/ly-vue/mionter
CMD ["python3", "manage.py", "runserver"]
