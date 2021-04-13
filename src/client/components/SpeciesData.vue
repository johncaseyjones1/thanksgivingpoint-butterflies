<template>
  <div class="species-data-container">
    <div class="center-div">
      <div class="buttons" v-show="showTable">
          <button class="btn btn-outline-success option-btn" @click="showAddSpecies()">Add new species</button>
          <a class="btn btn-outline-success option-btn" href="/static/butterfly_species/butterfly_species.csv" download="butterfly_species.csv">Download species data</a>
        </div>
      <button class="btn btn-dark add-species-btn" v-show="addSpecies" @click="hideAddSpecies()">Cancel</button>
      <v-client-table v-show="showTable" v-model="speciesData" :columns="columns" :options="options">
        <div slot="Species" slot-scope="{row, update, setEditing, isEditing, revertValue}">
          <span @click="setEditing(true)" v-if="!isEditing()">
              {{row.Species}}
          </span>
          <span v-else>
          <input type="text" v-model="row.Species">
              <button type="button" @click="update(row.Species); setEditing(false); updateSpecies(row)">Submit</button>
              <button type="button" @click="revertValue(); setEditing(false)">Cancel</button>        
            </span>  
        </div>   
        <div slot="CommonName" slot-scope="{row, update, setEditing, isEditing, revertValue}">
          <span @click="setEditing(true)" v-if="!isEditing()">
              {{row.CommonName}}
          </span>
          <span v-else>
          <input type="text" v-model="row.CommonName">
              <button type="button" @click="update(row.CommonName); setEditing(false); updateSpecies(row)">Submit</button>
              <button type="button" @click="revertValue(); setEditing(false)">Cancel</button>        
            </span>  
        </div>    
        <div slot="Location" slot-scope="{row, update, setEditing, isEditing, revertValue}">
          <span @click="setEditing(true)" v-if="!isEditing()">
              {{row.Location}}
          </span>
          <span v-else>
          <input type="text" v-model="row.Location">
              <button type="button" @click="update(row.Location); setEditing(false); updateSpecies(row)">Submit</button>
              <button type="button" @click="revertValue(); setEditing(false)">Cancel</button>        
            </span>  
        </div>   
        <div slot="Size" slot-scope="{row, update, setEditing, isEditing, revertValue}">
          <span @click="setEditing(true)" v-if="!isEditing()">
              {{row.Size}}
          </span>
          <span v-else>
          <input type="text" v-model="row.Size">
              <button type="button" @click="update(row.Size); setEditing(false); updateSpecies(row)">Submit</button>
              <button type="button" @click="revertValue(); setEditing(false)">Cancel</button>        
            </span>  
        </div> 
        <div slot="Pattern" slot-scope="{row, update, setEditing, isEditing, revertValue}">
          <span @click="setEditing(true)" v-if="!isEditing()">
              {{row.Pattern}}
          </span>
          <span v-else>
          <input type="text" v-model="row.Pattern">
              <button type="button" @click="update(row.Pattern); setEditing(false); updateSpecies(row)">Submit</button>
              <button type="button" @click="revertValue(); setEditing(false)">Cancel</button>        
            </span>  
        </div> 
        <div slot="PrimaryColor" slot-scope="{row, update, setEditing, isEditing, revertValue}">
          <span @click="setEditing(true)" v-if="!isEditing()">
              {{row.PrimaryColor}}
          </span>
          <span v-else>
          <input type="text" v-model="row.PrimaryColor">
              <button type="button" @click="update(row.PrimaryColor); setEditing(false); updateSpecies(row)">Submit</button>
              <button type="button" @click="revertValue(); setEditing(false)">Cancel</button>        
            </span>  
        </div> 
        <div slot="SecondaryColor" slot-scope="{row, update, setEditing, isEditing, revertValue}">
          <span @click="setEditing(true)" v-if="!isEditing()">
              {{row.SecondaryColor}}
          </span>
          <span v-else>
          <input type="text" v-model="row.SecondaryColor">
              <button type="button" @click="update(row.SecondaryColor); setEditing(false); updateSpecies(row)">Submit</button>
              <button type="button" @click="revertValue(); setEditing(false)">Cancel</button>        
            </span>  
        </div> 
        <div slot="WingShape" slot-scope="{row, update, setEditing, isEditing, revertValue}">
          <span @click="setEditing(true)" v-if="!isEditing()">
              {{row.WingShape}}
          </span>
          <span v-else>
          <input type="number" v-model="row.WingShape">
              <button type="button" @click="update(row.WingShape); setEditing(false); updateSpecies(row)">Submit</button>
              <button type="button" @click="revertValue(); setEditing(false)">Cancel</button>        
            </span>  
        </div> 
        <div slot="Eyespot" slot-scope="{row, update, setEditing, isEditing, revertValue}">
          <span @click="setEditing(true)" v-if="!isEditing()">
              {{row.Eyespot}}
          </span>
          <span v-else>
          <input type="text" v-model="row.Eyespot">
              <button type="button" @click="update(row.Eyespot); setEditing(false); updateSpecies(row)">Submit</button>
              <button type="button" @click="revertValue(); setEditing(false)">Cancel</button>        
            </span>  
        </div> 
        <div slot="ImagePath" slot-scope="{row, update, setEditing, isEditing, revertValue}">
          <span @click="setEditing(true)" v-if="!isEditing()">
              {{row.ImagePath}}
          </span>
          <span v-else>
          <input type="text" v-model="row.ImagePath">
              <button type="button" @click="update(row.ImagePath); setEditing(false); updateSpecies(row)">Submit</button>
              <button type="button" @click="revertValue(); setEditing(false)">Cancel</button>        
            </span>  
        </div> 
        <div slot="QuickFact" slot-scope="{row, update, setEditing, isEditing, revertValue}">
          <span @click="setEditing(true)" v-if="!isEditing()">
              {{row.QuickFact}}
          </span>
          <span v-else>
          <input type="text" v-model="row.QuickFact">
              <button type="button" @click="update(row.QuickFact); setEditing(false); updateSpecies(row)">Submit</button>
              <button type="button" @click="revertValue(); setEditing(false)">Cancel</button>        
            </span>  
        </div> 
        <div slot="CaterpillarHostPlants" slot-scope="{row, update, setEditing, isEditing, revertValue}">
          <span @click="setEditing(true)" v-if="!isEditing()">
              {{row.CaterpillarHostPlants}}
          </span>
          <span v-else>
          <input type="text" v-model="row.CaterpillarHostPlants">
              <button type="button" @click="update(row.CaterpillarHostPlants); setEditing(false); updateSpecies(row)">Submit</button>
              <button type="button" @click="revertValue(); setEditing(false)">Cancel</button>        
            </span>  
        </div> 
        <div slot="SexuallyDimorphic" slot-scope="{row, update, setEditing, isEditing, revertValue}">
          <span @click="setEditing(true)" v-if="!isEditing()">
              {{row.SexuallyDimorphic}}
          </span>
          <span v-else>
          <input type="text" v-model="row.SexuallyDimorphic">
              <button type="button" @click="update(row.SexuallyDimorphic); setEditing(false); updateSpecies(row)">Submit</button>
              <button type="button" @click="revertValue(); setEditing(false)">Cancel</button>        
            </span>  
        </div> 
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
       "SecondaryColor", "WingShape", "Eyespot", "ImagePath", "QuickFact", 
       "CaterpillarHostPlants", "SexuallyDimorphic", "Delete"],
      options: {
        headings: {

        },
        editableColumns:["Species", "CommonName", "Location", "Size", "Pattern", "PrimaryColor",
       "SecondaryColor", "WingShape", "Eyespot", "ImagePath", "QuickFact", 
       "CaterpillarHostPlants", "SexuallyDimorphic", "Delete"],
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
    updateSpecies(row) {
      console.log(row._id)
      request.post('/api/butterfly_species/edit')
        .type('json')
        .send({
              _id: row._id.$oid,
              Species: row.Species,
              CommonName: row.CommonName,
              Location: row.Location,
              Size: row.Size,
              Pattern: row.Pattern,
              PrimaryColor: row.PrimaryColor,
              SecondaryColor: row.SecondaryColor,
              WingShape: row.WingShape,
              Eyespot: row.Eyespot,
              ImagePath: row.ImagePath,
              QuickFact: row.QuickFact,
              CaterpillarHostPlants: row.CaterpillarHostPlants,
              SexuallyDimorphic: row.SexuallyDimorphic})
        .then((res) => {
          this.editMessage = res.body.message
          console.log(this.editMessage)
      })
    },
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
* {
  font-size: 12px;
}
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