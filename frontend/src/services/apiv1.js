// member.js 用于定义用户的登录、注册、注销等
import axiosClient from '@/utils/axiosClient'
// 定义接口  

// 项目类别列表
export const getProjectTypes = () => axiosClient.get(`/v1/project_types`)
// 项目列表
export const getProjectList = (typeId, page) => axiosClient.get(`v1/projects?type_id=${typeId}&page=${page}`)
// 修改项目详情
export const updateProject = (projectId, itemInfo) => axiosClient.put(`v1/project/${projectId}`, itemInfo)
//获取数据总览
export const getDB = () => axiosClient.get(`v1/db`)
//待选选项
export const getOptions = () => axiosClient.get(`v1/options`)