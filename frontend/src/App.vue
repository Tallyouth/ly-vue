<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
  export default {
    name: 'App',
    data() {
      return {
        message: 'hello vue'
      }
    },
  }
</script>

<style>
  #app {
    margin: 0
  }

  html,
  body {
    margin: 0;
    padding: 0;
    background-color: #fbfcfd;
  }

  .clearfix::after,
  .clearfix::before {
    content: " ";
    display: table;
  }

  .clearfix::after {
    clear: both;
  }
</style>