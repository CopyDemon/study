# 1. add OS
# 2. install dependencies
# 3. copy all need files to container
# 4. execute the command to start the app


# 1. add OS
# image depends on layer by layer, we can create image from base layer then add dependencies
# or we can create a exist image by use the image has already have the dependencies and already created by other from docker hub

# node verion, linux os(small linux os several MB)
FROM node:18-alpine 

# 2. install dependencies
RUN apk add --update nodejs

# 3. copy all need files to container (copy file or folder from host to container)
COPY index.js /index.js

# 4. execute the command to start the app
# [command, param...]
CMD ["node", "index.js"]

# build docker image
# docker build -t image name, build path
# docker build -t docker-example .