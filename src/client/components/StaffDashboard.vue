<template>
  <div>
    <div class="header-div">
      <div class="header-text">Welcome Staff Member</div>
      <div>This is where the magic happens</div>
    </div>
    <div class="page-buttons">
      <button class="btn btn-outline-dark">Releases</button>
      <button class="btn btn-outline-dark">Shipments</button>
    </div>
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
  .header-div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    height: 300px;
    background-color: #eeeeed;
    border-bottom: 30px solid #598400;
  }

  .header-text {
    font-size: 40px;
  }

  .page-buttons {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    margin-top: 40px;
  }

  .btn {
    margin-left: 20px;
    margin-right: 20px;
    width: 150px;
  }

  @media only screen and (max-width: 600px) {

    .header-div {
      height: 200px;
    }

    .header-text {
      font-size: 22px;
      font-weight: bold;
    }

    .page-buttons {
      flex-direction: column;
    }

    .btn {
      margin-bottom: 20px;
    }

  }


</style>