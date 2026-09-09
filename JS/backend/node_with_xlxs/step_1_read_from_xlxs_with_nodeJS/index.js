const { app, BrowserWindow, dialog } = require('electron');

app.on('ready', () => {
  let win = new BrowserWindow();
  
  dialog.showOpenDialog(win, {
    properties: ['openFile']
  }).then(result => {
    console.log(result.filePaths);
  }).catch(err => {
    console.log(err);
  });
});

console.log(`app working`)