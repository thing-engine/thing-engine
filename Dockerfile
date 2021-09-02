FROM ubuntu:18.04
RUN ln -s /usr/share/zoneinfo/Etc/GMT+7 /etc/localtime

RUN apt update \
    && apt install -y git python3 \
    python3-pip \
    libsm6 \
    libxext6 \
    libfontconfig1 \
    libxrender1 \
    python3-tk 


COPY . /app
WORKDIR /app

EXPOSE 8080


RUN pip3 install --no-cache-dir --upgrade pip

RUN pip3 install -r requirements.txt


#ENTRYPOINT ["python"]
#CMD ["app.py"]
    