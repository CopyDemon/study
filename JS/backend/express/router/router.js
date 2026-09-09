const express = require('express');
const indexRouter = require('./index.router');

const router = express.Router();

router.use('/', indexRouter);

module.exports = router;

