const HtmlWebPackPlugin = require ("html-webpack-plugin");

const path = require ("path");

const port = 3000;
let publicUrl = `http://localhost:${port}`;
if(process.env.GITPOD_WORKSPACE_URL){
  const [schema, host] = process.env.GITPOD_WORKSPACE_URL.split('://');
  publicUrl = `${port}-${host}`;
}

module.exports = {
    mode: 'development',
    devtool: 'cheap-module-source-map',
    entry:"./src/front/index.js",
    devServer: {
        contentBase:  './dist',
        hot: true,
        disableHostCheck: true,
        historyApiFallback: true,
        public: publicUrl
    },
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

    },
    {
        test: /\.svg$/,
        use: [
          {
            loader: "babel-loader"
          },
          {
            loader: "react-svg-loader",
            options: {
              jsx: true // true outputs JSX tags
            }
          }
        ]
      }
]
},
    plugins: [new HtmlWebPackPlugin (),
    new Dotenv({ safe: true, systemvars: true })]
};