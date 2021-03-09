<template>
  <div class="shipment-container">
    <div class="center-div">
      <table class="table">
        <thead class="thead-dark">
          <tr>
            <th scope="col">Date</th>
            <th scope="col">Species</th>
            <th scope="col">Qty</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Mar 16, 2021</td>
            <td>Catonephele-numilia</td>
            <td>23</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>   
</template>

<script>

export default {
  name: 'Releases',
  data() {

  }
}

</script>

<style scoped>
.releases-container {
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