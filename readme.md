# Blog - Django
1. Blog website based on Django framework. 
2. Running on Aliyun: [sjgo.online](http://39.97.239.252/)
3. Server Stack: request <-> Nginx <-> Gunicorn(Django web)

# Docker
1. Run command: ```docker run -p 8080:8080 -dit songgs/django-blog:init-sqlite```
2. Service Stack: 
+ request <->  
+ Supervisord(Daemon) < - > nginx <-> gunicorn <-> django <-> blog app <-> sqlite
3. Init blog data: http://your-url:8080/admin + admin/admin123
4. Sample blog: http://39.97.239.252:8080/
