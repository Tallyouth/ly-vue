// member.js 用于定义用户的登录、注册、注销等
import req from '@/utils/axiosClient'
// 定义接口  

// 项目类别列表
export const getProjectTypes = () => req.get(`/v1/project_types`)
// 项目列表
export const getProjectList = (typeId,page) => req.get(`v1/projects?page=${page}&type_id=${typeId}`)
// 修改项目详情
export const updateProject = (projectId, itemInfo, csrftoken) => req.put(`v1/project/${projectId}`, itemInfo,
    {
        headers: {
            "X-CSRFToken": csrftoken
        }
    })