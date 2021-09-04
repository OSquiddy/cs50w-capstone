/* eslint-disable */
module.exports = {
    'devServer': {
      'open': true,
    //   'port': 3000,
      'compress': true,
    //   'public': 'http://192.168.1.35:8080/',
      'public': 'http://localhost:8080/',
      'host': 'localhost',
      'disableHostCheck': true
    }
    // 'chainWebpack': config => {
    //   config.module
    //     .rule('vue')
    //     .use('vue-svg-inline-loader')
    //     .loader('vue-svg-inline-loader')
    //     .options({ /* ... */ })
  
      // config.output.chunkFilename('[name].[contenthash].js')
      // config.optimization.moduleIds = 'deterministic'
    // }
  
  }