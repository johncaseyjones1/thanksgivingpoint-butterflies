<template>
  <div>
    <h1>What is your species prediction?</h1>
     <input v-model="speciesPrediction" placeholder="Prediction goes here"> <br>
     <button v-on:click="addObservation(speciesPrediction)">Send Observation</button>
     {{message}}
  </div>
</template>

<script>
import request from 'superagent-bluebird-promise'

export default {
  data () {
    return {
      message: 'Bye World!',
      speciesPrediction: ''
    }
  },

  methods: {
    addObservation(speciesPrediction) {
      request
        .post('/api/observation/post/')
        .type('json')
        .send({speciesPrediction: speciesPrediction})
        .then((res) => {
          this.message = res.body.message
        })

    }
  },

  created() {
    
  }
}
</script>
