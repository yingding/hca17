/**
 * Created by yingding on 04.04.17.
 */
var path = require('path');
var _root = path.resolve(__dirname, '..');

// to the server in the same week example
var _serverRoot = path.resolve(__dirname, '../../server');

function root(args) {
    args = Array.prototype.slice.call(arguments, 0);
    return path.join.apply(path, [_root].concat(args));
}

function serverRoot(args) {
    args = Array.prototype.slice.call(arguments, 0);
    return path.join.apply(path, [_serverRoot].concat(args));
}
exports.root = root;
exports.serverRoot = serverRoot;