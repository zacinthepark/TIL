const path = require("path");
module.exports = {
  mode: "development",
  // 엔트리 포인트는 Webpack에게 번들링을 시작할 애플리케이션의 시작점을 지정
  entry: "./src/index.ts",
  devtool: "inline-source-map",
  devServer: {
    static: {
      directory: path.join(__dirname, "./"),
    },
  },
  module: {
    rules: [
      // .ts, .tsx로 끝나는 파일이 있을 시 해당 룰을 적용
      { 
        // $는 이 패턴이 파일의 맨 마지막에 와야 한다는 의미
        // x?는 x가 optional
        test: /\.tsx?$/,
        use: "ts-loader",
        exclude: /node_modules/,
      },
    ],
  },
  resolve: {
    extensions: [".tsx", ".ts", ".js"],
  },
  output: {
    filename: "bundle.js",
    // resolve 메서드는 하드코딩되어 있지 않은 path name을 구축할 수 있도록 해주는 메서드
    // 다른 디렉토리에서 실행을 해도 작동해주도록 함
    // bundle.js를 만들어 dist 폴더에 넣으라는 뜻
    path: path.resolve(__dirname, "dist"),
    publicPath: "/dist",
  },
};
