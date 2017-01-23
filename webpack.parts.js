const extractPlugin = require("extract-text-webpack-plugin")
const webpack = require("webpack")

exports.setupSASS = function(paths){
    return {
        module: {
            rules: [{
                    test: /\.(sass|css)$/,
                    include: paths,
                    loader: ["style-loader", "css-loader", "sass-loader"]
                }
            ]
        }
    }
}

exports.extractCSS = function(paths){
    return {
        module: {
            rules: [{
                    test: /\.(sass|css)$/,
                    include: paths,
                    loader: extractPlugin.extract({
                            fallbackLoader: "style-loader",
                            loader: ["css-loader", "sass-loader"]
                        }
                    )
                }
            ]
        },
        plugins: [new extractPlugin("bundle.css")]
    }
}

exports.devServer = function(options){
    return {
        devServer: {
            contentBase: options.path,
            historyApiFallback: true,
            watchContentBase: true,
            hot: true,
            inline: true,
            host: options.host,
            port: options.port
        },
        plugins: [new webpack.HotModuleReplacementPlugin({})]
    }
}

exports.setupJS = function(paths){
    return {
        module: {
            rules: [
                {
                    test: /\.(js|jsx)$/,
                    use: ["babel-loader"],
                    include: paths
                }
            ]
        }
    }
}
