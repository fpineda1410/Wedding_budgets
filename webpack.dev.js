const webpack = require('webpack');
const merge = require('webpack-merge');
const common = require('./webpack.common.js');

const port = 3000;
let publicUrl = `http://localhost:${port}`;
if(process.env.GITPOD_WORKSPACE_URL){
  const [schema, host] = process.env.GITPOD_WORKSPACE_URL.split('://');
  publicUrl = `${port}-${host}`;
}

module.exports = merge(common, {
    mode: 'development',
    devtool: 'cheap-module-source-map',
    devServer: {
        contentBase:  './src',
        hot: true,
        disableHostCheck: true,
        historyApiFallback: true,
        public: publicUrl
    }

});