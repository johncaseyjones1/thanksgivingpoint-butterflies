<template>
  <div id="predictionForm">

    <div class="header-div">
      <div class="header-text">
        <div class="colored-line"></div>
        <h1 class="predictionFormItem">Spot a butterfly?<br>Tell us what you see!</h1>
      </div>
      <div class="cover-photo">
        <img class="img" src="/static/photos/catonephele-numilia.jpg" alt="catonephele-numilia"/>
      </div>
    </div>

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
    background-color: #eeeeed;
    padding-top: 40px;
    padding-bottom: 40px;
  }

  .header-div {
    display: flex;
    flex-direction: row-reverse;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    height: 400px;
    padding: 0 40px 0 0;
    position: relative;
  }

  .header-text {
    margin-right: 60px;
  }

  .colored-line {
    width: 140px;
    height: 5px;
    background-color: #fe4600;
    margin-bottom: 20px;
  }

  .cover-photo {
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    width: 60%;
    display: block;
    height: 100%;
  }

  .img {
    max-width: 100%;
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    vertical-align: middle;
  }

  .predictionFormItem {

  }

</style>
