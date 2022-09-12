import request from '@/utils/request'

export function feiShuLogin(data) {
  return request({
    url: '/feishu/login/',
    method: 'post',
    data
  })
}
