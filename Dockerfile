FROM debian:10-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN=true
ENV DEBCONF_NOWARNINGS=yes

RUN apt-get update
RUN apt-get install -y --no-install-recommends python3 python3-pip
RUN pip3 install wheel
RUN pip3 install fastapi uvicorn pydantic

WORKDIR /opt/service
COPY api/main.py /opt/service/main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
