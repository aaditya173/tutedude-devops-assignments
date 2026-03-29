FROM node:18

WORKDIR /app

COPY package*.json ./

RUN npm install

RUN npm install dotenv

COPY . .

EXPOSE 3000

CMD ["node", "app.js"]
