<template>
  <div class="species-data-container">
    <div class="center-div">
      <div class="buttons" v-show="showTable">
          <button class="btn btn-outline-success option-btn" @click="showAddSpecies()">Add new species</button>
          <button class="btn btn-outline-success option-btn" @click="download()">Download species data</button>
      </div>
      <button class="btn btn-dark add-species-btn" v-show="addSpecies" @click="hideAddSpecies()">Cancel</button>
      <v-client-table v-show="showTable" v-model="speciesData" :columns="columns" :options="options">
        <div slot="Delete" slot-scope="{row}">
          <span>
            <button type="button" class="btn btn-outline-dark btn-sm" @click="deleteSpecies(row)">Delete</button>
          </span>  
        </div> 
      </v-client-table>
    </div>
    <AddSpecies v-show="addSpecies"/>
  </div>
</template>

<script>
import request from 'superagent-bluebird-promise'
import AddSpecies from './AddSpecies'

export default {
  name: 'SpeciesData',
  data() {
    return {
      addSpecies: false,
      showTable: true,
      collectingData: false,
      editMessage: "",
      speciesData: [],
      columns: ["Species", "CommonName", "Location", "Size", "Pattern", "PrimaryColor",
       "SecondaryColor", "WingShape", "Eyespot", "ImagePath", "Quick Fact", 
       "Caterpillar Host Plants", "Sexually Dimorphic", "Delete"],
      options: {
        headings: {

        },
        editableColumns:[],
        orderBy: {column: "formattedDate", ascending: false}
      },
      speciesToAdd: {
        scientificName: "",
        commonName: "",
        size: "",
        eyespot:0,
        pattern: "",
        wingShape: 0,
        primaryColor: "",
        secondaryColor: "", 
      },
    }
  },

  components: {
    AddSpecies
  },

  methods: {
    getAllSpecies() {
      this.collectingData = true;
      request
        .get('/api/butterfly_species')
        .then((res) => {
          this.speciesData = JSON.parse(res.body.allButterflies)
          var ind
          for (ind in this.speciesData) {
            this.speciesData[ind].id = this.speciesData[ind]._id.$oid
          }
        })
    },
    showAddSpecies() {
      this.addSpecies = true;
      this.showTable = false;
    },
    hideAddSpecies() {
      this.addSpecies = false;
      this.showTable = true;
    },
    /*updateSpecies(row) {
      console.log(row._id)
      request.post('/api/species/edit')
        .type('json')
        .send({ ... })
        .then((res) => {
          this.editMessage = res.body.message
          console.log(this.editMessage)
      })
    },*/
    deleteSpecies(row) {
      console.log("delete " + row)
      console.log(row._id)
      request.post('/api/butterfly_species/delete')
        .type('json')
        .send({
              _id: row._id.$oid,
              })
        .then((res) => {
          this.editMessage = res.body.message
          console.log(this.editMessage)
          const index = this.speciesData.findIndex(item => item.id === row.id);

          if (index !== undefined) this.speciesData.splice(index, 1);

      })
    }
  },

  created() {
    this.getAllSpecies()
  }
}

</script>

<style scoped>
.species-data-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 0 5px 0 5px;
}
.center-div {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}
.buttons {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  margin-bottom: 30px;
  margin-right: 20px;
}
.option-btn {
  margin-right: 20px;
}
.add-species-btn {
  margin-bottom: 30px;
}
</style>