FROM python:3.6.12-slim-stretch
MAINTAINER Jocky Hawk <hezw@yunjiacloud.com>

ENV APP_DIR /app
RUN mkdir ${APP_DIR}
VOLUME ${APP_DIR}
WORKDIR ${APP_DIR}

COPY requirements.txt .

RUN true \
    && pip install -U pip -i https://mirror.baidu.com/pypi/simple \
    # pip install packages
    && pip install -r requirements.txt -i https://mirror.baidu.com/pypi/simple


# expose http port
EXPOSE 8502

# copy config files into filesystem
ADD dirs.tar .

# exectute start up script
CMD ["streamlit", "run", "src/main.py", "--server.port", "8502", "--server.baseUrlPath", "/case-recommendation", "--server.enableCORS", "false"]