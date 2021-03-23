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

    <div class="center-div">
      <div id="predictionField">
        <div class="row-div">
          <div class="field-item" id="size">
            <h5>Size:</h5>
            <button v-on:click="setSize('S')" id="S" class="btn btn-outline-success" data-toggle="button">Small</button>
            <button v-on:click="setSize('M')" id="M" class="btn btn-outline-success" data-toggle="button">Medium</button>
            <button v-on:click="setSize('L')" id="L" class="btn btn-outline-success" data-toggle="button">Large</button>
          </div>
        </div>

        <div class="row-div">
          <div class="field-item" id="wingShape">
            <h5>Wing Shape:</h5>
            <input v-on:click="setWingShape(1)" id="wingShape1" class="btn btn-outline-success" type="button" value="1">
            <input v-on:click="setWingShape(2)" id="wingShape2" class="btn btn-outline-success" type="button" value="2">
            <input v-on:click="setWingShape(3)" id="wingShape3" class="btn btn-outline-success" type="button" value="3">
            <input v-on:click="setWingShape(4)" id="wingShape4" class="btn btn-outline-success" type="button" value="4">
            <input v-on:click="setWingShape(5)" id="wingShape5" class="btn btn-outline-success" type="button" value="5">
          </div>
        </div>

        <div class="row-div">
          <div class="field-item" id="primaryColor">
            <h5>Primary Color:</h5>
            <select class="custom-select" v-model="primaryColor">
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

          <div class="field-item" id="secondaryColor">
            <h5>Secondary Color:</h5>
            <select class="custom-select" v-model="secondaryColor">
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
        </div>

        <div class="row-div">
          <div class="field-item" id="pattern">
            <h5>Pattern:</h5>
            <input v-on:click="setPattern('Striped')" id="Striped" class="btn btn-outline-success pattern-button" type="button" value="Striped">
            <input v-on:click="setPattern('Veination')" id="Veination" class="btn btn-outline-success pattern-button" type="button" value="Veination">
            <input v-on:click="setPattern('Mottled')" id="Mottled" class="btn btn-outline-success pattern-button" type="button" value="Mottled">
            <input v-on:click="setPattern('Spots')" id="Spots" class="btn btn-outline-success pattern-button" type="button" value="Spotted">
            <input v-on:click="setPattern('None')" id="None" class="btn btn-outline-success pattern-button" type="button" value="None">
          </div>
        </div>

        <div class="row-div">
          <div class="field-item" id="eyespot">
            <h5>Eyespot:</h5>
            <input type="radio" id="yes" value="Y" v-model="eyespot">
            <label for="yes">Yes</label>
            <br>
            <input type="radio" id="no" value="N" v-model="eyespot">
            <label for="no">No</label>
            <br>
          </div>
        </div>

        <button class="predictionFormItem btn btn-dark" v-on:click="getObservationOptions(size, eyespot, pattern, wingShape, primaryColor, secondaryColor, predictionRequest)">Get Options</button>
      </div>
    </div>

    <div id="potential-species">
        <div v-for="species in potentialSpecies" :key="species.CommonName" @click="setSpeciesPrediction(species)" class="single-potential">
          <img class="speciesOptionImage" :src=species.ImagePath alt="">
          {{species.CommonName}}
        </div>
    </div>

    <div id="make-prediction-div" class="make-prediction" style="display: none;">
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
      size: "",
      wingShape: 0,
      primaryColor: "",
      secondaryColor: "", 
      pattern: "", 
      eyespot: 0,  
      message: "Please use the best photo you can",
      speciesPrediction: "",
      file: null,
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
          this.potentialSpecies = JSON.parse(res.body.speciesPrediction);
          this.scroll();
        })
      var make_prediction_div = document.getElementById("make-prediction-div");
      make_prediction_div.style.display = "flex";
    },

    async addObservation(speciesPrediction, file) {
      request.post('/api/photos')
      .attach('image', file)
      .then((res) => {
        request
        .post('/api/observations')
        .type('json')
        .send({speciesPrediction: speciesPrediction.Species,
              commonName: speciesPrediction.CommonName,
              filePath: res.body.filePath})
        .then((res) => {
          this.message = res.body.message
        })
      })     
    },

    scroll() {
      var scroll_div = document.getElementById("make-prediction-div");
      scroll_div.scrollIntoView({behavior: "smooth"});
    },

    setSpeciesPrediction(species) {
      this.speciesPrediction = species
    },

    fileChanged(event) {
      this.file = event.target.files[0]
    },

    setSize(size) {
        this.size = size;
        var sizes = ["S","M","L"];
        for (let i = 0; i < sizes.length; i++) {
            if (sizes[i] == size) {
                document.getElementById(size).classList.add("active");
            }
            else {
                document.getElementById(sizes[i]).classList.remove("active");
            }
        }
    },

    setWingShape(wingShape) {
        this.wingShape = wingShape;
        for (let i = 1; i < 6; i++) {
            if (i == wingShape) {
                document.getElementById("wingShape" + i).classList.add("active");
            }
            else {
                document.getElementById("wingShape" + i).classList.remove("active");
            }
        }
    },

    setPattern(pattern) {
        this.pattern = pattern;
        var patterns = ["Striped","Veination","Mottled","Spots","None"];
        for (let i = 0; i < patterns.length; i++) {
            if (patterns[i] == pattern) {
                document.getElementById(pattern).classList.add("active");
            }
            else {
                document.getElementById(patterns[i]).classList.remove("active");
            }
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
  .center-div {
    display: flex;
    justify-content: center;
  }
  .row-div {
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    flex-wrap: wrap;
    width: 100%;
  }
  #predictionField {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    margin-top: 50px;
    border: 3px solid #eeeeed;
    border-radius: 15px;
    padding: 30px;
  }
  .field-item {
    margin-right: 80px;
    margin-bottom: 30px;
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
  #potential-species {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
  }
  .single-potential {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
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
    h5 {
      font-size: 16px;
    }
    #predictionField {
      border: none;
      margin-top: 20px;
    }
    .predictionFormItem {
      width: 80%;
    }
    .field-item {
      margin-right: 0;
      margin-bottom: 30px;
    }
    .pattern-button {
      margin-bottom: 5px !important;
    }
  }
</style>