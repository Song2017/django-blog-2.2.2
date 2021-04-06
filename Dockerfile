FROM python:3.7-buster

LABEL maintainer="Songgs<bensong2017@hotmail.com>"

COPY . /app

#install nginx, serve static filese
RUN bash /app/nginx/install_nginx_debian.sh

WORKDIR /app

EXPOSE 8080

# Install Supervisord.
# Copy the entrypoint that will generate Nginx additional configs
RUN apt-get update \
    && apt-get install -y supervisor \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -r requirement.txt

ENTRYPOINT ["sh", "/app/entrypoint.sh"]