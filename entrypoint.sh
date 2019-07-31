#!/usr/bin/env bash
set -e

python --version
pip --version
if [ $APP_INIT == "Init" ]; then
    echo "INFO: Init Context ..."
    $APP_INIT = "Done"

    echo "INFO: config gunicorn ..."
    rm -f /tmp/gunicorn.sock
    touch /tmp/gunicorn.sock
    chown www-data:www-data /tmp/gunicorn.sock
    chmod 664 /tmp/gunicorn.sock
    rm /etc/guncorn/guncorn.ini
    cp guncorn.ini /etc/guncorn/guncorn.ini

    echo "INFO: config nginx ..."
    # forward request and error logs to docker log collector
    ln -sf /dev/stdout /var/log/nginx/access.log 
    ln -sf /dev/stderr /var/log/nginx/error.log
    # Remove default configuration from Nginx
    rm /etc/nginx/conf.d/default.conf
    # supervisord as daemon process
    echo "daemon off;" >> /etc/nginx/nginx.conf
    if [ -f /app/nginx.conf ]; then
        cp /app/nginx.conf /etc/nginx/nginx.conf
    else
        echo "INFO: nginx.conf not found ..."
    fi
    # chown app folder
    chown -R www-data:www-data /app

    echo "INFO: config supervisord ..."
    supervisord.conf /etc/supervisor/conf.d/supervisord.conf
    chmod +x start.sh
else
    echo "INFO: Command Mode ..."
    exec "$@"
fi