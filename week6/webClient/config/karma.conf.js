var webpackConfig = require('./webpack.test');

module.exports = function (config) {
    var _config = {
        basePath: '',

        frameworks: ['jasmine'],

        files: [
            {pattern: './config/karma-test-shim.js', watched: false}
        ],

        preprocessors: {
            './config/karma-test-shim.js': ['webpack', 'sourcemap']
        },
        //client:{
        //     clearContext: false // leave Jasmine Spec Runner output visible in browser
        //},

        webpack: webpackConfig,

        webpackMiddleware: {
            stats: 'errors-only'
        },

        webpackServer: {
            noInfo: true
        },

        reporters: ['progress','kjhtml'],
        port: 9876,
        colors: true,
        logLevel: config.LOG_INFO,
        autoWatch: false,
        browsers: ['Chrome'],
        singleRun: true // change singleRun to true, to get a single test run, the browers info of jasmine will be closed automatically
        // use false to prevent jasmine browser closed automatically
        // click on debug to see the jasmine debug session
    };

    config.set(_config);
};
