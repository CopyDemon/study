#!/bin/sh
# node 放后台, nginx 前台 (daemon off) 作为容器主进程; nginx 退了容器就退
node index.js &
exec nginx -g 'daemon off;' -p /app -c /app/nginx.conf
