FROM node:latest

WORKDIR /app

COPY ["pakage.json", "pakage-lock.json", "./"]

RUN npm install

COPY ./ ./

RUN npm start