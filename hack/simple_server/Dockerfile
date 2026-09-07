# Ubuntu + nginx (反向代理, 80) + node (index.js, 8080)
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

# nginx + Node 22 (apt 自带的 node 太老, import.meta.dirname 需要 >= 20.11)
RUN apt-get update \
 && apt-get install -y --no-install-recommends nginx curl ca-certificates \
 && curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
 && apt-get install -y --no-install-recommends nodejs \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 先只拷 package*.json 装依赖, 这样改代码不会让 npm install 那层缓存失效
COPY package*.json ./
RUN npm ci --omit=dev

COPY index.js index.html nginx.conf start.sh ./
RUN mkdir -p logs uploads && chmod +x start.sh

EXPOSE 80
CMD ["./start.sh"]
