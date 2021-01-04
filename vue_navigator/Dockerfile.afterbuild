FROM nginx:latest
LABEL maintainer="Jocky Hawk <hezw@yunjiacloud.com>"

# volumes:
#     - ./vue_navigator/dist:/usr/share/nginx/html
#     - ./vue_navigator/nginx.conf:/etc/nginx/conf.d/default.conf
COPY dist/ /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/conf.d/default.conf

# expose http port
EXPOSE 80