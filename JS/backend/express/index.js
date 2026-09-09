const express = require('express');
const router = require('./router/router');

const port = process.env.PORT || 3000;
const app = express();

app.use(router);

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});