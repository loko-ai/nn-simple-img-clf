FROM python:3.8-slim
RUN apt-get update --fix-missing && apt-get install -y python3-tk && rm -rf /var/cache/apt
ADD ./requirements.txt /
RUN pip install -r /requirements.txt
ARG GATEWAY
ENV GATEWAY=$GATEWAY
ADD . /plugin
ENV PYTHONPATH=$PYTHONPATH:/plugin
WORKDIR /plugin/services
CMD python services.py