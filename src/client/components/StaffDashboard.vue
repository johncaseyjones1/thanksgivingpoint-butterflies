<template>
  <div id="inputForm">
    
  </div>
</template>



<script>
//import request from 'superagent-bluebird-promise'
//import axios from 'axios'

export default {
  data () {
    return {
      message: 'Please use the best photo you can',
      speciesPrediction: '',
      file: null
    }
  },

  methods: {
    /*submitEntry() {
      request.post('/api/staff/dashboard')
      .attach('image', file)
      .then((res) => {
        request
        .post('/api/observations')
        .type('json')
        .send({speciesPrediction: speciesPrediction,
              filePath: res.body.filePath})
        .then((res) => {
          this.message = res.body.message
        })
      })*/
      
  },

  created() {
    
  }
}
</script>

<style scoped>


</style>