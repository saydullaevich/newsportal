module.exports ={
    devServer:{
        proxy: {
            '^/api/': {
                target: process.env.BACKEND_SERVER_URL || 'http://127.0.0.1:8000',
                ws: true,
                changeOrigin: true
            }
        }
    }
};

