const path = require("path")
const HtmlWebPackPlugin = require("html-webpack-plugin")//导入 在内存中自动生成index页面的插件


//常见插件实例

const htmlPlugin = new HtmlWebPackPlugin({
    template:path.join(__dirname, "./src/index.html")  ,//源文件
    filename: "index.html"//生成内存中首页名称
})
module.exports = 
{
    entry: path.join(__dirname, "src/main.js"),
    output:{
      path:path.join(__dirname, "./dist"),
      filename: "bundle.js"
    },
    mode:"development",//development production 两种模式，
    //webpack 4.x 约定大于配置 约定 默认打包入口路径 src -> index.js 目的尽量减少配置文件体积
    //打包输出路径 dist -> main.js
    //4.x mode选项 development production 两种模式，必选
    // webpack 只打包处理 .js 后缀类型文件，其他png vue要配置第三方loader
    plugins:[
        htmlPlugin
    ],
    module: {
        rules: [
            // 'transform-runtime' 插件告诉 babel 要引用 runtime 来代替注入。
            {
              test: /\.js|jsx$/,
              exclude: /(node_modules|bower_components)/,
              use: {
                loader: 'babel-loader',
                options: {
                  presets: ['@babel/preset-env']
                }
              }
            },
            //?追加参数modules，对普通样式表启用模块化
            //规定第三方样式表以 .css结尾
            //自己的样式表以 .scss或 .less结尾
            
            {test: /\.css$/i,use: [
              {loader:'style-loader'}, 
              {loader:'css-loader'}
              ],},
              
              { test: /\.ttf|woff|woff2|eot|svg$/, use:"url-loader"},//打包处理字体文件
              { test:/\.scss$/, use:[
              {loader:'style-loader'},
              {loader:'css-loader'},
              {loader:'sass-loader'}, 
              ],},// 打包处理scss文件

          ]
      },
    resolve:{
      extensions:[".js", ".jsx", "json"],//后缀名默认补全
      alias:{
        "@":path.join(__dirname, "./src")//@表示项目根目录下src路径（绝对路径）
      }

    }
    }