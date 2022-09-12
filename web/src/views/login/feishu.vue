<template>
    <div>
      <!-- {{ loginForm.code }}
      {{ loginForm.state }} -->
    </div>
  </template>
  
  <script>
      export default {
          name: 'feiShuLogin',
  
          data() {
              return {
                  loginForm: {
                      code: this.$route.query.code,
                      state: this.$route.query.state,
                  },
              }
          },
          mounted() {
              this.dingTalkLogin()
          },
          methods: {
              dingTalkLogin() {
                  console.log('feiShuLogin===============')
                  this.loading = true
                  this.$store.dispatch('user/feiShuLogin', this.loginForm).then(() => {
                      console.log('feiShuLogin2===============')
                    //   this.$router.push({ path: this.redirect || '/' })
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