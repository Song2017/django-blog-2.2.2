#!/usr/bin/env bash
set -e

python --version
pip --version

if [ -f /app/supervisord.conf ]; then
    echo "INFO: Init Context ..."
    echo "INFO: config gunicorn ..."
    rm -f /tmp/gunicorn.sock
    touch /tmp/gunicorn.sock
    # chown www-data:www-data /tmp/gunicorn.sock
    chmod 777 /tmp/gunicorn.sock
    #cp guncorn.ini /etc/guncorn/guncorn.ini

    echo "INFO: config nginx ..."
    # forward request and error logs to docker log collector
    ln -sf /dev/stdout /var/log/nginx/access.log 
    ln -sf /dev/stderr /var/log/nginx/error.log
    # Remove default configuration from Nginx
    rm -r /etc/nginx/conf.d/default.conf
    # supervisord as daemon process
    echo "daemon off;" >> /etc/nginx/nginx.conf
    if [ -f /app/nginx.conf ]; then
        cp /app/nginx.conf /etc/nginx/nginx.conf
    else
        echo "INFO: nginx.conf not found ..."
    fi
    # chown app folder
    chown -R www-data:www-data /app
    # create logs/
    mkdir /app/logs
    touch /app/logs/nginx.access.log
    chmod 777 /app/logs/nginx.access.log

    echo "INFO: config supervisord ..."
    mv supervisord.conf /etc/supervisor/conf.d/supervisord.conf
    chmod +x start.sh
    echo 'INFO: Init Done ...'
fi
echo "INFO: Command Mode ..."
echo "$@"
exec "$@"
