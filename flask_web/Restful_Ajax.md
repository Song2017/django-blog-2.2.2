RESTful: representational state transfer 资源表现层状态转化
设计原则
1. url不应该包含动词, 使用http方法来表现
GET /users/1
DELETE /users/1
PUT /users/1
2. 关注请求头
查看请求头信息, 并给予正确的状态码, 例如通过Accept, 查看客户端请求返回信息的类型
http方法语义
OPTIONS: 获取资源支持的所有的http方法
HEAD: 只获取请求某个资源返回的头信息
GET: 获取某个资源, 200
POST: 创建新资源. 完成后返回201,并返回创建的资源的详细信息
PUT: 创建 201 或替换资源 200
PATCH: 局部更新资源 200
DELETE: 删除资源, 204
3. 对输出的结果不再包装
HTTP/1.1 200 OK
{'success': t rue ,
'data': { ' id' : 1, 'name': ' xiaoming'}
}
没有必要再添加success
HTTP /1 .1 200 OK
{ ' id' : 1, 'name': ' xiaoming'}
4. URI的失效 410 gone 和迁移 301 redirect
5. 速度限制
X -RateLimit -Limit :当前时间段允许的并发请求数。
• X -RateLimit -Remaining :当前时间段保留的请求数。
• X -RateLimit -Reset :当前时间段剩余的秒数
6. 缓存
在请求头中使用If-Modifìed -Since 、If-None-Match 等来确认资源是否经过修改。
7. 并发控制
缺少并发控制的PUT和PATCH 请求可能导致"更新丢失" 。这个时候可以使用Last-Modified和Tag 头来实现条件请求
    1. 客户端发起的请求如果没有包含If-Unmodified-Since 或者If-Match 头，就返同状态码"403 Forbidden"
    2. If-Unmodified-Since 或者If-Match 头与服务器记录的实际修改时间或ETag 值不匹配时， 
    返问状态码"412 Precondition Failed"
    3. 实际修改时间或ETag 的历史值匹配.但资源已经被修改过时，返回状态码"409 Conflict"
    4. 客户端发起的请求所提供的条件符合实际值，就更新资源， 响应" 200 OK " 或者"204 No Content" 
    并包含更新过的Last-Modified 和 ETag 头，同时包含Content-Location头, 包含更新后的资源URL

Ajax: Asynchronous JavaScript and XML 
传统Ajax 指的是XMLHttpRequest ( XHR ), 通过Ajax向服务器发送HTTP 请求，接收服务器逅回的JSON 数据，
然后用JavaScript修改网页的局部来实现更新和提交
Fetch ( htφ5:/，但ithub.com/github/fetch ) API基于Promise.
Promise 对象代表着一个还未完成，但预期将来会完成的操作. 
    ECMAScript 2015 ( ES6 )规也中有一个新的特性Promise
    ES 7 提供的async/awaitAPI