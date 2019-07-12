# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:3.6

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=mionter Version=0.0.1
EXPOSE 8000

# Define mountable directories.
VOLUME ["/root/mionter", "/root/mionter"]

WORKDIR /root/mionter

# Using pip:

