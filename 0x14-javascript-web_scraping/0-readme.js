#!/usr/bin/node
const fs = require('fs');
const MyFiles = process.argv.slice(2);
fs.readFile(MyFiles[0], 'utf8', function (err, data) {
  if (err) console.log('error', err);
  else process.stdout.write(data);
});
