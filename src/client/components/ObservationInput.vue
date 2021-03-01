<template>
  <div>
    <h1>What is your species prediction?</h1>
      <input v-model="speciesPrediction" placeholder="Prediction goes here"> <br>
      <p></p>
      <input type="file" name="photo" @change="fileChanged">
      <button v-on:click="addObservation(speciesPrediction, file)">Send Observation</button>
      <p></p>
    {{message}}
  </div>
</template>



<script>
import request from 'superagent-bluebird-promise'
//import axios from 'axios'

export default {
  data () {
    return {
      message: 'Please use the highest quality photo you can',
      speciesPrediction: '',
      file: null
    }
  },

  methods: {
    addObservation(speciesPrediction, file) {
      request.post('/api/photos')
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
      })
      


    },
    fileChanged(event) {
      this.file = event.target.files[0]
    },
    async upload() {
      try {
        const formData = new FormData();
        formData.append('photo', this.file, this.file.name)
        //let r1 = await axios.post('/api/photos', formData);
        //let r2 = await axios.post('/api/observations', {
        //  title: this.title,
        //  path: r1.data.path
        //});
       //this.addItem = r2.data;
      } catch (error) {
        //console.log(error);
      }
    },
  },

  created() {
    
  }
}
</script>
