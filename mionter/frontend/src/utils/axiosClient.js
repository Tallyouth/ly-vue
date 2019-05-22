var axios = require('axios')
// 创建实例
var axiosInstance = axios.create({
  baseURL: process.env.NODE_ENV === 'production' ? '/' : 'http://localhost:8000/',
})
 // 一、请求拦截器 忽略
axiosInstance.interceptors.request.use(config => {
  let token = localStorage.getItem('token')
  if (token) {
    config.headers.authorization = 'JWT ' + token
  }
  return config
}, err => {
  // 对请求错误做些什么
  console.log(err)
  return Promise.reject(err)
})
// 二、响应拦截器 忽略
axiosInstance.interceptors.response.use(res => res, err => {
  try {
    if (err.response.statusText === 'Unauthorized') {
      localStorage.setItem('token', '')
    }
  } catch (e) { }
  return Promise.reject(err)
})

export default axiosInstance
