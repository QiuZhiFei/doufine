<template>
  <div id="app">
    <UserMoments/>
  </div>
</template>

<script>
import UserMoments from "./components/page/UserMoments.vue"

export default {
  name: 'app',
  components: {
    UserMoments,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
