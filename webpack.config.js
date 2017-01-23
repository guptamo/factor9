const path = require("path")
const webpack = require("webpack")
const merge = require("webpack-merge")
const parts = require("./webpack.parts")
const friendlyErrors = require("friendly-errors-webpack-plugin")

const PATHS = {
    app: path.resolve(__dirname, "homepage", "app"),
    build: path.resolve(__dirname, "homepage", "build"),
}

const common = {
    entry: path.resolve(PATHS.app, "js", "index.js"),
    output: {
        path: PATHS.build,
        publicPath: PATHS.build,
        filename: "bundle.js"
    },
    plugins:[new friendlyErrors()]
}

module.exports = function(env) {
    if (env === "production"){
        return merge(
            common,
            {
                devtool: 'source-map'
            },
            parts.setupJS(PATHS.app),
            parts.extractCSS(PATHS.app)
        )
    } else {
        return merge(
            common,
            {
                devtool: "eval-source-map",
                performance: {
                    hints: false
                }
            },
            parts.setupJS(PATHS.app),
            parts.setupSASS(PATHS.app),
            parts.devServer({
                "host": process.env.host,
                "port": process.env.port,
                "path": path.resolve(__dirname, "homepage")
            })
        )
    }
}

// {
//     devtool: "eval-source-map",
//     devServer: {
//         contentBase: path.resolve(__dirname, "homepage")
//     },
//     performance: {hints: false},
//     plugins: [new webpack.NamedModulesPlugin()],
//
// },
