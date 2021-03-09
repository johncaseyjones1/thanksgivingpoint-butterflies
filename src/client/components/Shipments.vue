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
            <th scope="col">Failed to emerge</th>
            <th scope="col">DOA</th>
            <th scope="col">Parasitized</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>Mar 8, 2021</td>
            <td>Costa Rica Butterflies</td>
            <td>Catonephele-numilia</td>
            <td>Costa Rica</td>
            <td>35</td>
            <td>3</td>
            <td>2</td>
            <td>0</td>
            <td>0</td>
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
