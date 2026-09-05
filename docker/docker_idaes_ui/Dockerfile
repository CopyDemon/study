# TODO list
# 1. try not to use ubuntu or ubuntu latest the version is not specific then may crash, and try to use the image already build with python and node version
# 3. try to learn RUN, and how to write RUN command now RUN will enable a new layer of SHELL that is odd
# 4. Mike said to build dependency into another docker image and use that image to build the idaes-ui app docker image
FROM ubuntu:latest 

# ENV
ENV NODE_VERSION 18.12.0

# define the port that vite will run on
EXPOSE 5173

# use bash shell
# may not be default shell...
# SHELL ["/bin/bash", "--login", "-c"]

# think about user role, app for all users

# update apt and install wget git
RUN apt update && apt upgrade -y && apt-get install -y wget && apt-get install -y git

# install conda create python 3.10 environment
RUN wget -O Miniforge3.sh "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh" && \ 
    bash Miniforge3.sh -b -p "${HOME}/conda" && \ 
    source "${HOME}/conda/etc/profile.d/conda.sh" && \
    conda create -n idaes_ui_3.10 python=3.10 -y && \
    conda activate idaes_ui_3.10 && \
    pip install idaes-pse && \
    idaes get-extensions    

# install nvm and setup nvm default node version
RUN wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash && \
    export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")" && \
    [ -s "$NVM_DIR/nvm.sh" ] && \
    . "$NVM_DIR/nvm.sh" && \
    nvm install $NODE_VERSION && \
    nvm alias default $NODE_VERSION && \
    nvm use default

# # # to app dir
# WORKDIR /app


# # clone or copy idaes-ui to image

# # # clone idaes-ui if remote need this docker
# # RUN git clone https://github.com/IDAES/idaes-ui.git

# # copy idaes-ui local files to container if dev need this docker
# COPY ./idaes-ui.* /app

# WORKDIR /app/idaes-ui
# RUN source ${HOME}/conda/etc/profile.d/conda.sh && \
#     conda activate idaes_ui_3.10 && \
#     cd /app/idaes-ui && \
#     pip install . && \
#     pip install requirements-dev.txt

# # copy container start.sh to image and use as CMD
# COPY start.sh /usr/local/bin/start.sh
# RUN chmod +x /usr/local/bin/start.sh
# CMD ["/usr/local/bin/start.sh"]

# # # finsih build
# # # RUN echo "Docker build complete"