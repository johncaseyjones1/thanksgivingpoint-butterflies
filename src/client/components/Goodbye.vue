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
        .get('/api/goodbye')
        .then((res) => {
          //console.log(res.body)
          this.msg = res.body.bye2
        })
        //.catch((err) => {

          //console.log(err)
        //})
    }
  },

  created() {
    this.fetchData()
  }
}
</script>
