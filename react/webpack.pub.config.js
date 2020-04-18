const path = require("path")
const HtmlWebPackPlugin = require("html-webpack-plugin")
const {CleanWebpackPlugin} = require("clean-webpack-plugin")
const webpack = require("webpack")
// 重置清理输出路径所有文件

const htmlPlugin = new HtmlWebPackPlugin({
    template:path.join(__dirname, "./src/index.html")  ,
    filename: "index.html"
})


const cleanWebpackPlugin =  new CleanWebpackPlugin()

const webpackDedupe = new webpack.optimize.DedupePlugin({
  'process.env.NODE_ENV': '"production"'
})
module.exports = 
{
    entry: {
      app: path.join(__dirname, "src/main.js"),
    
    },
    optimization:{
      splitChunks:{
        chunks: "initial",
        // 抽离入口
        name:"jquery",
        // 抽离文件名
        filename:"js/vendors.js",

      },
    },
    output:{
      path:path.join(__dirname, "./dist"),  
      filename: "js/bundle.js"
    },
    mode:"production",
    

    plugins:[
        htmlPlugin,
        cleanWebpackPlugin,
        webpackDedupe,
        
    ],
    module: {
        rules: [
            { test: /\.js|jsx$/,
              exclude: /(node_modules|bower_components)/,
              use: {
                loader: 'babel-loader',
                options: {
                  presets: ['@babel/preset-env']
                }
              }
            },
            
            {test: /\.css$/i,use: [
              {loader:'style-loader'}, 
              {loader:'css-loader'}
              ],
            },
              
            { test: /\.ttf|woff|woff2|eot|svg$/, use:"url-loader"},
            { test:/\.scss$/, use:[
                {loader:'style-loader'},
                {loader:'css-loader'},
                {loader:'sass-loader'}, 
                ],
            },
            { test: /\.(png|gif|jpg|bmp)$/i, 
              loader:"url-loader",
              options: {
                limit: 5000,
                name:"image/[name]-[hash:4].[ext]",
  
              }

            },


          ]
      },
    resolve:{
      extensions:[".js", ".jsx", "json"],
      alias:{
        "@":path.join(__dirname, "./src")
      }

    }
    }