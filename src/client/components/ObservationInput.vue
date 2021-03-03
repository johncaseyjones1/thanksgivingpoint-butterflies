<template>
  <div id="predictionForm">
    <h1 class="predictionFormItem">What is your species prediction?</h1>
      <br><br>
      <input class="predictionFormItem" v-model="speciesPrediction" placeholder="Prediction goes here"> <br>
      <p></p>
      <input class="predictionFormItem" type="file" name="photo" @change="fileChanged">
      <br>
      <button class="predictionFormItem" v-on:click="addObservation(speciesPrediction, file)">Send Observation</button>
      <p class="predictionFormItem">{{message}}</p>

  </div>
</template>



<script>
import request from 'superagent-bluebird-promise'
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

<style scoped>
  #predictionForm {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    justify-content: center;
  }

  .predictionFormItem {
    align-self: center;
    flex-grow: 4;
    max-width: 80%;
    min-width: 60%;
  }

</style>
