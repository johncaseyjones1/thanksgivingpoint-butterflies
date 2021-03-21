<template>
  <div class="shipment-container">
    <div class="center-div">
      <button class="btn btn-dark add-shipment-btn" v-show="showTable" @click="showAddShipment()">Add new shipment</button>
      <button class="btn btn-dark add-shipment-btn" v-show="addShipment" @click="hideAddShipment()">Cancel</button>
      <v-client-table v-show="showTable" v-model="shipments" :columns="columns" :options="options">
        <div slot="FTE" slot-scope="{row, update, setEditing, isEditing, revertValue}">
          <span @click="setEditing(true)" v-if="!isEditing()">
              {{row.FTE}}
          </span>
          <span v-else>
            <input type="text" class="form-control" v-model="row.FTE">
            <button type="button" class="btn btn-dark btn-sm" @click="update(row.FTE); setEditing(false)">Submit</button>
            <button type="button" class="btn btn-sm" @click="revertValue(); setEditing(false)">Cancel</button>        
          </span>  
        </div>
        <div slot="W" slot-scope="{row, update, setEditing, isEditing, revertValue}">
          <span @click="setEditing(true)" v-if="!isEditing()">
              {{row.W}}
          </span>
          <span v-else>
            <input type="text" class="form-control" v-model="row.W">
            <button type="button" class="btn btn-dark btn-sm" @click="update(row.W); setEditing(false)">Submit</button>
            <button type="button" class="btn btn-sm" @click="revertValue(); setEditing(false)">Cancel</button>        
          </span>  
        </div>
        <div slot="Parasite" slot-scope="{row, update, setEditing, isEditing, revertValue}">
          <span @click="setEditing(true)" v-if="!isEditing()">
              {{row.Parasite}}
          </span>
          <span v-else>
            <input type="text" class="form-control" v-model="row.Parasite">
            <button type="button" class="btn btn-dark btn-sm" @click="update(row.Parasite); setEditing(false)">Submit</button>
            <button type="button" class="btn btn-sm" @click="revertValue(); setEditing(false)">Cancel</button>        
          </span>  
        </div> 
      </v-client-table>
    </div>
    <AddShipment v-show="addShipment"/>
  </div>
</template>

<script>
import request from 'superagent-bluebird-promise'
import AddShipment from './AddShipment'

export default {
  name: 'Shipments',
  data() {
    return {
      addShipment: false,
      showTable: true,
      collectingData: false,
      shipments: [],
      columns: ["id","formattedDate","Supplier","Species","Origin","Quantity","EmergedEarly","DOA","FTE","W","Parasite"],
      options: {
        headings: {
          id: 'ID',
          formattedDate: 'Date',
          Supplier: 'Supplier',
          Species: 'Species',
          Origin: 'Origin',
          Quantity: 'Qty',
          EmergedEarly: 'Emerged early',
          DOA: 'DOA',
          FTE: 'FTE',
          W: 'Wings',
          Parasite: 'Parasite'
        },
        editableColumns:['FTE','W','Parasite'],
        customSorting: {
          formattedDate: function (ascending) {
            return function (a, b) {
              var dateA = a.Date.$date;
              var dateB = b.Date.$date;

              if (ascending)
                return dateA >= dateB ? 1 : -1;

              return dateA <= dateB ? 1 : -1;
            }
          }
        }
      }
    }
  },

  components: {
    AddShipment
  },

  methods: {
    getAllShipments() {
      this.collectingData = true;
      request
        .get('/api/shipment')
        .then((res) => {
          this.shipments = JSON.parse(res.body.allShipments)
          var ind
          for (ind in this.shipments) {
            this.shipments[ind].formattedDate = new Date(this.shipments[ind].Date.$date).toDateString()
            this.shipments[ind].id = this.shipments[ind]._id.$oid
          }
        })
    },
    showAddShipment() {
      this.addShipment = true;
      this.showTable = false;
    },
    hideAddShipment() {
      this.addShipment = false;
      this.showTable = true;
    }
  },

  created() {
    this.getAllShipments()
  }
}

</script>

<style scoped>
.shipment-container {
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
.add-shipment-btn {
  margin-bottom: 30px;
}
</style>
