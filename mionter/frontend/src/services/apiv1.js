 // member.js 用于定义用户的登录、注册、注销等
 import req from '@/utils/axiosClient'
 // 定义接口  
 // 在这里定义了一个登陆的接口，把登陆的接口暴露出去给组件使用
//  export const LOGIN = params => req('post', '/operator/login', params);
 // 这里使用了箭头函数，转换一下写法：
 //export const LOGIN=function(req){
 //    return req('post','/operator/login',params)
 //}
 // 定义注册接口
//  export const REG = params => req('post', '/operator/reg', params);
 // 定义注销接口
//  export const LOGOUT = params => req('post', '/operator/logout', params);
// 项目类别列表
export const getProjectTypes = () => req.get(`/v3/project_types`)