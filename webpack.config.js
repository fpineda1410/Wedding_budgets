const HtmlWebPackPlugin = require ("html-webpack-plugin");

const path = require ("path");

module.exports = {
    entry:"./src/front/index.js",
    output: {
        path: path.resolve(__dirname,"dist"),
        filename: "bundle.js",
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: "/node_modules/",
                use: {
                    loader: "babel-loader"
                }
            },
            {
                test: /\.(css|less)$/i,
                use: [
                    {
                      loader: "style-loader",
                    },
                    {
                      loader: "css-loader",
                    },
                    {
                        loader: "less-loader",
                        options: {
                            lessOptions: {
                               javascriptEnabled: true
                            }
                          }
                    }
        ]

    }]
},
    plugins: [new HtmlWebPackPlugin ({template:"./src/front/index.html"})]
};