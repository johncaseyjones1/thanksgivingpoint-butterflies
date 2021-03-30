<template>
  <div class="shipment-container">
    <div class="center-div">
      <div class="buttons" v-show="showTable">
          <button class="btn btn-outline-success option-btn" @click="showAddShipment()">Add new shipment</button>
          <button class="btn btn-outline-success option-btn" @click="download()">Download shipment data</button>
      </div>
      <button class="btn btn-dark add-shipment-btn" v-show="addShipment" @click="hideAddShipment()">Cancel</button>
      <v-client-table v-show="showTable" v-model="shipments" :columns="columns" :options="options">
        <div slot="FTE" slot-scope="{row, update, setEditing, isEditing, revertValue}">
          <span @click="setEditing(true)" v-if="!isEditing()">
              {{row.FTE}}
          </span>
          <span v-else>
            <input type="number" class="form-control" v-model="row.FTE">
            <button type="button" class="btn btn-dark btn-sm" @click="update(row.FTE); setEditing(false); updateShipment(row)">Submit</button>
            <button type="button" class="btn btn-sm" @click="revertValue(); setEditing(false)">Cancel</button>        
          </span>  
        </div>
        <div slot="W" slot-scope="{row, update, setEditing, isEditing, revertValue}">
          <span @click="setEditing(true)" v-if="!isEditing()">
              {{row.W}}
          </span>
          <span v-else>
            <input type="number" class="form-control" v-model="row.W">
            <button type="button" class="btn btn-dark btn-sm" @click="update(row.W); setEditing(false); updateShipment(row)">Submit</button>
            <button type="button" class="btn btn-sm" @click="revertValue(); setEditing(false)">Cancel</button>        
          </span>  
        </div>
        <div slot="Parasite" slot-scope="{row, update, setEditing, isEditing, revertValue}">
          <span @click="setEditing(true)" v-if="!isEditing()">
              {{row.Parasite}}
          </span>
          <span v-else>
            <input type="number" class="form-control" v-model="row.Parasite">
            <button type="button" class="btn btn-dark btn-sm" @click="update(row.Parasite); setEditing(false); updateShipment(row)">Submit</button>
            <button type="button" class="btn btn-sm" @click="revertValue(); setEditing(false)">Cancel</button>        
          </span>  
        </div> 
        <div slot="Delete" slot-scope="{row}">
          <span>
            <button type="button" class="btn btn-outline-dark btn-sm" @click="deleteShipment(row)">Delete</button>
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
      editMessage: "",
      shipments: [],
      columns: ["id","formattedDate","Supplier","Species","Origin","Quantity","EmergedEarly","DOA","FTE","W","Parasite","Delete"],
      options: {
        headings: {
          id: 'ID',
          formattedDate: 'Date',
          Supplier: 'Supplier',
          Species: 'Species',
          Origin: 'Origin',
          Quantity: 'Qty',
          EmergedEarly: 'EE',
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
        },
        orderBy: {column: "formattedDate", ascending: false}
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
    },
    updateShipment(row) {
      console.log(row._id)
      request.post('/api/shipment/edit')
        .type('json')
        .send({
              _id: row._id.$oid,
              date: row.Date.$date,
              supplier: row.Supplier,
              species: row.Species,
              origin: row.Origin,
              quantity: row.Quantity,
              emergedEarly: row.EmergedEarly,
              deadOnArrival: row.DOA,
              FTE: row.FTE,
              W: row.W,
              Parasite: row.Parasite})
        .then((res) => {
          this.editMessage = res.body.message
          console.log(this.editMessage)
      })
    },
    deleteShipment(row) {
      console.log("delete " + row)
      console.log(row._id)
      request.post('/api/shipment/delete')
        .type('json')
        .send({
              _id: row._id.$oid,
              })
        .then((res) => {
          this.editMessage = res.body.message
          console.log(this.editMessage)
          const index = this.shipments.findIndex(item => item.id === row.id);

          if (index !== undefined) this.shipments.splice(index, 1);

      })
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
.add-shipment-btn {
  margin-bottom: 30px;
}
</style>
