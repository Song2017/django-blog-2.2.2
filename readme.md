# Blog - Django
1. Blog website based on Django framework. 
2. Running on Aliyun: [sjgo.online](http://39.97.239.252/)
3. Server
    - Nginx serve static files
    - Gunicorn(Django web) handle requests

# Docker
1. Run command: ```docker run -p 8080:8080 -dit songgs/django-blog:sqlite```
2. Service Stack:
3. Init blog data: http://your-url:8080/admin + admin/admin123
4. Sample blog: http://39.97.239.252:8080/
