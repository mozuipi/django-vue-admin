<template>
  <div>
    <!-- {{ loginForm.authCode }}
    {{ loginForm.state }} -->
  </div>
</template>

<script>
    export default {
        name: 'dingTalkLogin',

        data() {
            return {
                loginForm: {
                    authCode: this.$route.query.authCode,
                    state: this.$route.query.state,
                },
            }
        },
        mounted() {
            this.dingTalkLogin()
        },
        methods: {
            dingTalkLogin() {
                console.log('dingTalkLogin===============')
                this.loading = true
                this.$store.dispatch('user/dingTalkLogin', this.loginForm).then(() => {
                    console.log('dingTalkLogin2===============')
                    // this.$router.push({ path: this.redirect || '/' })
                    top.location.href = '/'
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