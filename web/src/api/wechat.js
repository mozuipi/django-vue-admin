import request from '@/utils/request'

export function wechatLogin(data) {
  return request({
    url: '/wechat/login/',
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