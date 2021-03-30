<template>
  <div class="add-species-container">
    <div class="center-div">
      <div class="heading">Add a new species</div>
      <div class="column-div">
        <div class="input-group mb-3">
          <div class="subheading">Scientific name:</div>
          <input type="text" class="form-control" v-model="scientificName"/>
        </div>

        <div class="input-group mb-3">
          <div class="subheading">Common name:</div>
          <input type="text" class="form-control" v-model="commonName"/>
        </div>

        <div class="row-div">
          <div class="field-item" id="size">
            <h5>Size:</h5>
            <input v-on:click="setSize('S')" id="S" class="btn btn-outline-success" type="button" value="Small">
            <input v-on:click="setSize('M')" id="M" class="btn btn-outline-success" type="button" value="Medium">
            <input v-on:click="setSize('L')" id="L" class="btn btn-outline-success" type="button" value="Large">
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

      </div>

      <div class="row-div">
        <div class="button-div"> 
          <button class="btn btn-dark" @click="submitShipment()">Submit</button>
        </div>

        <b-alert
          :show="dismissCountDown"
          dismissible
          variant="success"
          @dismissed="dismissCountDown=0"
          @dismiss-count-down="countDownChanged"
        >
          <p>Shipment added succesfully!</p>
        </b-alert>
      </div>
    </div>
  </div>  
</template>

<script>
import request from 'superagent-bluebird-promise'

export default {
  name: 'AddSpecies',
  data() {
    return {
      scientificName: "",
      commonName: "",
      size: "",
      wingShape: 0,
      primaryColor: "",
      secondaryColor: "", 
      pattern: "", 
      eyespot: 0,  
      image: null,
      message: "",
      dismissSecs: 3,
      dismissCountDown: 0
    }
  },

  methods: {
    async submitSpecies() {
      request.post('/api/species/post')
        .type('json')
        .send({scientificName: this.scientificName,
              commonName: this.commonName,
              size: this.size,
              wingShape: this.wingShape,
              primaryColor: this.primaryColor,
              secondaryColor: this.secondaryColor,
              pattern: this.pattern,
              eyespot: this.eyespot,
              image: this.image})
        .then((res) => {
          this.message = res.body.message
          this.dismissCountDown = this.dismissSecs
          this.scientificName = ""
          this.commonName = ""
          this.size = ""
          this.wingShape = 0
          this.primaryColor = ""
          this.secondaryColor = ""
          this.pattern = ""
          this.eyespot = 0
          this.image = null
      })
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
  }
}

</script>

<style scoped>
.add-species-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 5px 0 5px;
  width: 90%;
  margin-bottom: 40px;
}
.center-div {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  background-color: #eeeeed;
  border: 3px solid #eeeeed;
  border-radius: 10px;
  width: 80%;
  padding: 40px;
}
.heading {
  font-size: 24px;
  margin-bottom: 30px;
}
.subheading {
  padding: 15px 15px 0 0;
  width: 16%;
  text-align: left;
}
.input-group {
  margin: 10px 0 10px 0;
}
.row-div {
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  flex-wrap: wrap;
  width: 100%;
}
.column-div {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  flex-wrap: wrap;
  width: 100%;
}
.field-item {
  margin-right: 80px;
  margin-top: 30px;
}
input, select {
  background-color: white;
  border: none;
  border-radius: 15px !important;
}
.button-div {
  margin-top: 20px;
  margin-right: 40px;
}

@media only screen and (max-width: 600px) {
  .center-div {
    padding: 15px;
  }
}
</style>