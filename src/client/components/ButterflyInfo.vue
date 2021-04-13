<template>
  <div>

  </div>
</template>

<script>
import request from 'superagent-bluebird-promise'

export default {
  data() {
    return {
      collectingData: false,
      butterfly: null
    }
  },
  methods: {
    getButterfly() {
    this.collectingData = true;
    request
      .get('/api/ ... ' + $route.params.id)
      .then((res) => {
        this.butterfly = JSON.parse(res.body.butterfly)
      })
    }
  },
  created() {
    this.getButterfly()
  }
}
</script>

<style scoped>

</style>
