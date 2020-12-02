FROM node:15.3.0 as build-stage
LABEL maintainer="Jocky Hawk <hezw@yunjiacloud.com>"

WORKDIR /opt/build

COPY . .

RUN true \
    && yarn config set registry https://registry.npm.taobao.org 

RUN true \
    && yarn install --prod --no-lockfile \
    && yarn build


FROM nginx:latest
LABEL maintainer="Jocky Hawk <hezw@yunjiacloud.com>"


# system local config
RUN true \
    # timezone to china
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime


COPY --from=build-stage /opt/build/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

# expose http port
EXPOSE 80