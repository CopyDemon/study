import express from 'express';
import fs from 'node:fs';
import path from 'node:path';

const app = express();
app.use(express.json());   // 全局中间件：把 Content-Type: application/json 的 body 解析成 req.body
const port = 8080;
const __dirname = import.meta.dirname;

// GET / -> 返回 index.html
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// POST /upload -> 把请求 body 原样写成文件，文件名从 header 拿
const uploadDir = path.join(__dirname, 'uploads');
app.post(
    '/upload',
    express.raw({ type: '*/*', limit: '50mb' }),
    async (req, res) => {
        console.log(`receive frontend request, ${req.body.length} bytes, filename=${req.get("x-filename")}`)
        const name = path.basename(decodeURIComponent(req.get('x-filename') || 'unnamed'));
        fs.writeFileSync(path.join(uploadDir, name), req.body);   // 同步按路径写
        res.send(name);
});

// POST /read  body: { fileName } -> 读回文件内容
app.post('/read', (req, res) => {
    const fileName = req.body?.fileName;   // 取字段，不是整个 body
    console.log(`request file ${fileName}`)
    if (!fileName) {
        console.log(`No File Name`)
        return res.status(400).send('Read file fail, no file name');
    }
    const filePath = path.join(uploadDir, path.basename(fileName));
    if (!fs.existsSync(filePath)) {
        return res.status(404).send('file not found');
    }
    const file = fs.readFileSync(filePath,'utf-8');        // 同步读，拿到 Buffer
    console.log(file)
    res.status(200).send(file);
});

// here is another secrete: passCode123!

app.listen(port, () => {
  console.log(`server running at http://localhost:${port}`);
});
