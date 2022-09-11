import request from '@/utils/request'

export function dingTalkLogin(data) {
  return request({
    url: '/dingtalk/login/',
    method: 'post',
    data
  })
}

export function getWechatQRCode() {
  return request({
    url: '/wechat/qrcode/',
    method: 'get',
    params: {}
  })
}