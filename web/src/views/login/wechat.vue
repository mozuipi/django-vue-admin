<template>
  <div>
    {{ loginForm.code }}
    {{ loginForm.state }}
    {{ loginForm.appid }}
  </div>
</template>

<script>
    export default {
        name: 'WechatLogin',

        data() {
            return {
                loginForm: {
                    code: this.$route.query.code,
                    state: this.$route.query.state,
                    appid: this.$route.query.appid,
                },
                listLoading: true
            }
        },
        mounted() {
            this.wechatLogin()
        },
        methods: {
            wechatLogin() {
                console.log('wechatLogin')
                this.loading = true
                this.$store.dispatch('user/wechatLogin', this.loginForm).then(() => {
                    this.$router.push({ path: this.redirect || '/' })
                    this.loading = false
                }).catch(() => {
                    this.loading = false
                })
            }
        },
    }
</script>

<style>

</style>