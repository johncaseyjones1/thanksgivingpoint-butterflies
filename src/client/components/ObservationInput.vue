<template>
  <div id="predictionForm">

    <div class="header-div">
      <div class="header-text">
        <div class="colored-line"></div>
        <h1>Spot a butterfly?<br>Tell us what you see!</h1>
      </div>
      <div class="cover-photo">
        <img class="img" src="/static/photos/catonephele-numilia.jpg" alt="catonephele-numilia"/>
      </div>
    </div>

    <div id="predictionField">
      <div id="size">
        <h4>Size:</h4>
        <input type="radio" id="small" value="S" v-model="size">
        <label for="one">Small</label>
        <br>
        <input type="radio" id="medium" value="M" v-model="size">
        <label for="two">Medium</label>
        <br>
        <input type="radio" id="large" value="L" v-model="size">
        <label for="two">Large</label>
        <br>
      </div>

      <div id="primaryColor">
        <h4>Primary Color:</h4>
        <select v-model="primaryColor">
          <option disabled value="">Please select one</option>
          <option>Red</option>
          <option>Orange</option>
          <option>Yellow</option>
          <option>Green</option>
          <option>Blue</option>
          <option>Purple</option>
          <option>Brown</option>
          <option>White</option>
          <option>Black</option>
          <option>Tan</option>
        </select>
      </div>

      <div id="secondaryColor">
        <h4>Secondary Color:</h4>
        <select v-model="secondaryColor">
          <option disabled value="">Please select one</option>
          <option>Red</option>
          <option>Orange</option>
          <option>Yellow</option>
          <option>Green</option>
          <option>Blue</option>
          <option>Purple</option>
          <option>Brown</option>
          <option>White</option>
          <option>Black</option>
          <option>Tan</option>
        </select>
      </div>

      <div id="pattern">
        <h4>Pattern:</h4>
        <input type="radio" id="striped" value="Stiped" v-model="pattern">
        <label for="striped">Striped</label>
        <br>
        <input type="radio" id="veination" value="Veination" v-model="pattern">
        <label for="veination">Veination</label>
        <br>
        <input type="radio" id="mottled" value="Mottled" v-model="pattern">
        <label for="mottled">Mottled</label>
        <br>
        <input type="radio" id="spotted" value="Spots" v-model="pattern">
        <label for="spotted">Spotted</label>
        <br>
        <input type="radio" id="none" value="None" v-model="pattern">
        <label for="none">None (solid color)</label>
        <br>
      </div>

      <div id="wingShape">
        <h4>Wing Shape:</h4>
        <input type="radio" id="one" value="1" v-model="wingShape">
        <label for="one">One</label>
        <br>
        <input type="radio" id="two" value="2" v-model="wingShape">
        <label for="two">Two</label>
        <br>
        <input type="radio" id="three" value="3" v-model="wingShape">
        <label for="three">Three</label>
        <br>
        <input type="radio" id="four" value="4" v-model="wingShape">
        <label for="four">Four</label>
        <br>
        <input type="radio" id="five" value="5" v-model="wingShape">
        <label for="five">Five</label>
        <br>
      </div>

      <div id="eyespot">
        <h4>Eyespot:</h4>
        <input type="radio" id="yes" value="Y" v-model="eyespot">
        <label for="yes">Yes</label>
        <br>
        <input type="radio" id="no" value="N" v-model="eyespot">
        <label for="no">No</label>
        <br>
      </div>
      <button class="predictionFormItem btn btn-dark" v-on:click="getObservationOptions(size, eyespot, pattern, wingShape, primaryColor, secondaryColor, predictionRequest)">Get Options</button>
    </div>

    <div id="potential-species">
      <ul>
        <li  v-for="species in potentialSpecies" :key="species.CommonName">
          <div @click="setSpeciesPrediction(species)">
            {{species.CommonName}}
            <img class="speciesOptionImage" :src=species.ImagePath alt="">
          </div>
        </li>
      </ul>
    </div>

    <div class="make-prediction">
      {{speciesPrediction.CommonName}}
      <input class="predictionFormItem" type="file" name="photo" @change="fileChanged">
      <br>
      <button class="predictionFormItem btn btn-dark" v-on:click="addObservation(speciesPrediction, file)">Send Observation</button>
      <p class="predictionFormItem">{{message}}</p>
    </div>
    
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
      file: null,
      size: "",
      eyespot:0,
      pattern: "",
      wingShape: 0,
      primaryColor: "",
      secondaryColor: "",    
      predictionRequest: {
        size: "",
        eyespot:0,
        pattern: "",
        wingShape: 0,
        primaryColor: "",
        secondaryColor: "",  
      },
      potentialSpecies: [],
    }
  },
  methods: {
    async getObservationOptions(size, eyespot, pattern, wingShape, primaryColor, secondaryColor, predictionRequest) {
      predictionRequest.size = size;
      predictionRequest.eyespot = eyespot;
      predictionRequest.pattern = pattern;
      predictionRequest.wingShape = wingShape;
      predictionRequest.primaryColor = primaryColor;
      predictionRequest.secondaryColor = secondaryColor;
      this.predictionRequest = predictionRequest;
      request
        .post('/api/prediction/get')
        .type('json')
        .send(predictionRequest)
        .then((res) => {
          this.potentialSpecies = JSON.parse(res.body.speciesPrediction)
        })
    },

    async addObservation(speciesPrediction, file) {
      request.post('/api/photos')
      .attach('image', file)
      .then((res) => {
        request
        .post('/api/observations')
        .type('json')
        .send({speciesPrediction: speciesPrediction.Species,
              filePath: res.body.filePath})
        .then((res) => {
          this.message = res.body.message
        })
      })
      
    },
    setSpeciesPrediction(species) {
      this.speciesPrediction = species
    },


    fileChanged(event) {
      this.file = event.target.files[0]
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
  .header-div {
    display: flex;
    flex-direction: row-reverse;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    height: 400px;
    position: relative;
    background-color: #eeeeed;
  }
  .header-text {
    margin-right: 100px;
  }
  .colored-line {
    width: 140px;
    height: 5px;
    background-color: #fe4600;
    margin-bottom: 20px;
  }
  .cover-photo {
    width: 60%;
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
  .make-prediction {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    width: 100%;
    padding: 40px 10px 20px 10px;
  }
  .predictionFormItem {
    width: 60%;
  }
  .speciesOptionImage {
    max-width: 20%;
  }
  @media only screen and (max-width: 600px) {
    .cover-photo {
      width: 80%;
      height: 300px;
      margin-top: 20px;
    }
    .header-div {
      flex-direction: column;
      justify-content: flex-start;
      height: 500px;
      padding-top: 40px;
    }
    .header-text { 
      margin-right: 0;
    }
    h1 {
      font-size: 28px;
    }
      .predictionFormItem {
        width: 80%;
      }
  }
</style>