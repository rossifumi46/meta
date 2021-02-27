<template>
  <div id="app">
    <div class="main">
      <div class="doctor"
        v-for="doctor in info"
        :key="doctor.name"
      >
        <img :src="doctor.photo" alt="" class="photo">
        <div class="info">
          <h1 class="name">
            {{ doctor.name }}
          </h1>
          <div class="methods">
            <h2 class="title">Методы:</h2>
            <div class="methods-list">
              <div class="methods-item"
                v-for="method in doctor.methods"
                :key="method.name"
              >
                {{ method.name }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const axios = require('axios');

export default {
  name: "App",
  components: {

  },
  data() {
    return {
      info: null
    };
  },
  mounted() {
    axios
      .get('http://127.0.0.1:8000/doctors')
      .then(response => {
        console.log(response);
        this.info = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.main {
  width: 100%;;
  padding: 60px 30px;
  
}

.doctor {
  display: flex;
  padding: 50px 0;
}

.photo {
  width: 30%;
  object-fit: contain;
}

.info {
  padding: 0 50px;
  width: 70%;
}

.name {
  text-align: center;
  margin: 0;
}

.methods-list {
  display: flex;
}

.methods-item {
  margin-left: 10px;
  background: aqua;
  padding: 5px;
  border-radius: 5px;
}

.methods-item:first-of-type {
  margin-left: 0;
}

</style>
