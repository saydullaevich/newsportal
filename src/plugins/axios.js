"use strict";

import axios from "axios";

// Full config:  https://github.com/axios/axios#request-config
// axios.defaults.baseURL = process.env.baseURL || process.env.apiUrl || '';
// axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

let config = {
    baseURL: process.env.baseURL || process.env.apiUrl || "/api/"
    // timeout: 60 * 1000, // Timeout
    // withCredentials: true, // Check cross-site Access-Control
};

const _axios = axios.create(config);

_axios.interceptors.request.use(
    function(config) {
        // Do something before request is sent
        return config;
    },
    function(error) {
        // Do something with request error
        return Promise.reject(error);
    }
);

// Add a response interceptor
_axios.interceptors.response.use(
    function(response) {
        let data = response.data
        data.success = data.status === "success"
        data.fail = data.status === "fail"
        data.error = data.status === "error"

        return data;
    },
    function(error) {
        // Do something with response error
        return {
            error: true,
            fail: false,
            success: false,
            data: error
        }
    }
);

export const $axios = _axios;

export default {
    install: (app) => {
        app.config.globalProperties.$axios =  _axios
    }
}
