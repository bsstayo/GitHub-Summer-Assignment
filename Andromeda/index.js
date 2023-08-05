const express = require('express')

const app = express()

app.use(express.static("public"))

app.get('/', (req, res) => {
    res.send("안녕 웹앱")
})

const server = require("http").createServer({}, app)

server.listen(300, () => {
    console.log("http를 포트 3000에 오픈합니다")
})