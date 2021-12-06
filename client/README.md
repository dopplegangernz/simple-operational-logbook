# client

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


docker run -p 8080:8080 -w /app -v "$(pwd):/app" node:lts-alpine sh -c "npm install && npm run serve"