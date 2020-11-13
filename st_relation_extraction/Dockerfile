FROM python:3.6.12-slim-stretch
MAINTAINER Jocky Hawk <howhaw@163.com>


ENV APP_DIR /app
RUN mkdir ${APP_DIR}
VOLUME ${APP_DIR}
WORKDIR ${APP_DIR}

COPY requirements.txt .

RUN true \
    && pip install -U pip -i https://mirror.baidu.com/pypi/simple \
    # pip install packages
    && pip install -r requirements.txt -i https://mirror.baidu.com/pypi/simple


# streamlit-specific commands
# RUN true \
#     && mkdir -p /root/.streamlit \
#     && bash -c 'echo -e "\
# [general]\n\
# email = \"\"\n\
# " > /root/.streamlit/credentials.toml' \
#     && bash -c 'echo -e "\
# [browser]\n\
# serverAddress=\"relation.extraction\"\n\
# " > /root/.streamlit/config.toml'

# expose http port
EXPOSE 8502

# copy config files into filesystem
ADD dirs.tar .

# exectute start up script
# CMD ["streamlit", "run", "src/app.py", "--server.host", "0.0.0.0", "--server.port", "80", "--server.enableCORS", "false"]
CMD ["streamlit", "run", "src/app.py", "--server.port", "8502", "--server.baseUrlPath", "/relation-extraction", "--server.enableCORS", "false"]