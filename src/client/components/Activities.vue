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
      msg: 'Bye World!',
      listOfData:[]
    }
  },

  methods: {
    fetchData() {
      request
        .get('/api/activities')
        .then((res) => {
          this.msg = res.body.activities
        })

    }
  },

  created() {
    this.fetchData()
  }
}
</script>
