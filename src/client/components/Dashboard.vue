<template>
  <div>
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
import request from 'superagent-bluebird-promise'

export default {
  data () {
    return {
      msg: 'Hello World!'
    }
  },

  methods: {
    fetchData() {
      request
        .get('/api/dashboard')
        .then((res) => {
          this.msg = res.body.dashboard
        })
    }
  },

  created() {
    this.fetchData()
  }
}
</script>
