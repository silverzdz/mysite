<template>
  <div id="app">
    <div id="container">
      <router-view :key="$route.path"></router-view>
    </div>
  </div>
</template>

<script>

export default {
  name: 'app'
}
</script>

<style scoped>
  #app{
    width:100%;
    height:100%;
  }
</style>
<style>
html,body{
      margin:0;
      padding:0;
   }

#app {
  background: url("assets/bg.jpg") no-repeat center;
  height: 100%;
  width: 100%;

  background-size: cover;
  position: fixed;
}
#container {
  background-color: rgba(255, 255, 255, 0.5);
  height: 100%;
}
h1, h2, h3, h4 {
  color: #000000;
  text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.2);
}
h4 {
  margin-block-start: 10px;
  margin-block-end: 10px;
}
.el-radio__label {
  color: #000000;
  text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.2);
}
.box_border {
  background: rgba(255, 255, 255, 0.5);
  box-shadow: 1px 0px 15px rgba(0, 0, 0, 0.45);
  border-radius:10px;
  padding:20px 20px 20px 20px;
}
.btn-grp {
  padding:20px 20px 20px 20px;
}
</style>