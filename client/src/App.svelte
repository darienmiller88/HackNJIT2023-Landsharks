<script lang="ts">
  import Card from "./components/Card/Card.svelte";
  let latitude: Number = 39.8
  let longtitude: Number = 41.5
  let windSpeed: Number = 20
  let waveHeight: Number = 12
  let windDirection: string = "Northeast"

</script>

<main>
  <div class="title">Nautical Navigator!</div>
  <div class="weather-info lat-long-wrapper">
      <div class="latitude">
        Latitude: {latitude}&deg;
      </div>
      <div class="longitude">
        Longitude: {longtitude}&deg;
      </div>
  </div>
  <div class="cards">
    <Card title={"Wind Speed"} value={windSpeed}/>
    <Card title={"Wind Direction"} value={windDirection}/>
    <Card title={"Wave Height"} value={waveHeight}/>

  </div>
  <!-- <div class="weather-info">Wind Speed: </div>
  <div class="weather-info">Wind Direction: </div>
  <div class="weather-info">Wave Height: </div> -->
</main>

<style lang="scss">
  .title{
    text-align: center;
    font-size: 50px;
    padding: 20px;
    
    color: var(--primary);
  }

  .lat-long-wrapper{
    display: flex;
    justify-content: space-between;
    font-size: 30px;
    text-align: center;

    margin: auto;
    margin-bottom: 20px;

    width: fit-content;

    .latitude{
      margin-right: 20px;

      span{
        font-size: 20px;
      }
    }
  }

  .weather-info{
    font-size: 20px;
    padding: 10px 20px;
    color: var(--primary);
  }

  .cards{
    display: flex;
    justify-content: space-between;
    margin: auto;

    width: 60vw;
  }
  
</style>
