<template>
  <div id="app">
    <Navbar/>
    <Container/>
  </div>
</template>

<script>
import Container from "./components/Container"
import Navbar from "./components/Navbar";
export default {
  name: 'App',
  components: {
    Navbar,
    Container
  }
}
</script>

<style>
</style>
