const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const types = {'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.svg':'image/svg+xml','.webp':'image/webp','.png':'image/png','.ttf':'font/ttf','.pdf':'application/pdf'};
http.createServer((req,res) => {
  let url;
  try {url = decodeURIComponent(new URL(req.url,'http://localhost').pathname);} catch {res.writeHead(400).end();return;}
  const file = path.resolve(__dirname,'.'+(url==='/'?'/index.html':url));
  if (!file.startsWith(__dirname+path.sep)) {res.writeHead(403).end();return;}
  fs.readFile(file,(err,body) => {
    if (err) {res.writeHead(404).end('Not found');return;}
    res.writeHead(200,{'Content-Type':types[path.extname(file)]||'application/octet-stream'});res.end(body);
  });
}).listen(4174,'127.0.0.1',()=>console.log('Product portfolio: http://127.0.0.1:4174'));
