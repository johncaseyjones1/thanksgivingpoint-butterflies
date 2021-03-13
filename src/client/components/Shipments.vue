<template>
  <div class="shipment-container">
    <div class="center-div">
      <table class="table">
        <thead class="thead-dark">
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Date</th>
            <th scope="col">Supplier</th>
            <th scope="col">Species</th>
            <th scope="col">Origin</th>
            <th scope="col">Qty</th>
            <th scope="col">Emerged early</th>
            <th scope="col">DOA</th>
            <th scope="col">Failed to emerge</th>
            <th scope="col">Parasitized</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="shipment in shipments" :key="shipment.shipmentID">
            <td>{{ shipment.shipmentID }}</td>
            <td>{{ shipment.dateEntered }}</td>
            <td>{{ shipment.supplier }}</td>
            <td>{{ shipment.species }}</td>
            <td>{{ shipment.origin }}</td>
            <td>{{ shipment.quantity }}</td>
            <td>{{ shipment.emergedEarly }}</td>
            <td>{{ shipment.deadOnArrival }}</td>
            <td>{{ shipment.failedToEmerge }}</td>
            <td>{{ shipment.parasitized }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Shipments',
  data() {
    return {
      collectingData: false,
      shipments: [],
    }
  },

  methods: {
    getAllShipments() {
      this.collectingData = true;
      request
        .get('/api/')
        .then((res) => {
          this.shipments = JSON.parse(res.body.allShipments)
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
</style>
