var helpers = require('./helpers');
var rimraf = require('rimraf');

var distPath = helpers.serverRoot('public');
rimraf(distPath, function(error){
  if (error != null) {
      console.log('rimraf [Error]: ', error);
  } else {
    console.log('rimraf, removed folder: ',distPath);
  }
});
