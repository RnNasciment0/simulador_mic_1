FROM ubuntu:latest
LABEL authors="Renan"

ENTRYPOINT ["top", "-b"]