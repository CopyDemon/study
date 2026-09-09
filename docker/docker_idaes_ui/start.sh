#!/bin/bash

# source nvm
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")" && \
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# source conda
source "${HOME}/conda/etc/profile.d/conda.sh"

# activate conda
conda activate idaes_ui_3.10

# use nvm 18.12.0
nvm use 18.12.0

cd /app/idaes-ui


# install npm packages in project root folder
npm install

# install npm packages in IDAES-UI folder
cd /app/idaes-ui/IDAES-UI
npm install

# run vite with expose mode the expose port is 5173 defined in dockerfile docker compose
npx vite --host 0.0.0.0

# echo "idaes-ui start"