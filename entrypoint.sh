#!/usr/nginx/env bash
set -e

python --version
pip --version

# init django
echo "INFO: init django ..."
cd /app/django_blog
python manage.py migrate

echo "INFO: config nginx ..."
# forward request and error logs to docker log collector
#ln -sf /dev/stdout /var/log/nginx/access.log
#ln -sf /dev/stderr /var/log/nginx/error.log
# Remove default configuration from Nginx
rm -r /etc/nginx/conf.d/default.conf
cp /app/nginx/nginx.conf /etc/nginx/nginx.conf
echo "daemon off;" >> /etc/nginx/nginx.conf # supervisord as daemon process
# chown app folder
chown -R www-data:www-data /app
## create logs/
#mkdir /app/logs
#touch /app/logs/nginx.access.log
#chmod 777 /app/logs/nginx.access.log


# Start Supervisor
echo """
[supervisord]
nodaemon=true

[program:guncorn]
command=/usr/local/bin/gunicorn --workers 3 --threads 2 --bind unix:/tmp/gunicorn.sock django_blog.wsgi:application
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0
directory=/app/django_blog
autostart=true
autorestart=true
environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8

[program:nginx]
command=/usr/sbin/nginx -c /etc/nginx/nginx.conf
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0
stopsignal=QUIT
""" >/etc/supervisor/conf.d/supervisord.conf
exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf

echo "INFO: Command Mode ..."
echo "$@"
