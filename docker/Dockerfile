FROM debian:jessie
MAINTAINER docker@cryptobase.nl

# Note: The official Debian and Ubuntu images automatically ``apt-get clean``
# after each ``apt-get``
RUN apt-get update && apt-get install -y python wget

RUN cd /opt && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py

RUN pip install flask && \
    pip install flask-cors

RUN mkdir -p /opt/app

ADD app /opt/app

ENTRYPOINT ["/opt/app/api.py"]
