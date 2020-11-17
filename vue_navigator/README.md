导航页（iframe-navigation）
--------------------------

## 构建配置（Build Setup）

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

## Docker部署

[参考](https://blog.csdn.net/jiangyu1013/article/details/84572582)


```
docker build -f Dockerfile.vuedev -t hawk/vue-dev:v1 .
```