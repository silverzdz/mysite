<template>
  <div id="app">
    <router-view :key="$route.path"></router-view>
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
#app {
  background: url("assets/bg.jpg") no-repeat center;
  height: 100%;
  width: 100%;
  background-size: cover;
  position: fixed;
}
h1, h2, h3, h4 {
  color: #ffffff;
  text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.8);
}
h4 {
  margin-block-start: 10px;
  margin-block-end: 10px;
}
.el-radio__label {
  color: #ffffff;
  text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.8);
}
.box_border {
  background: rgba(255, 255, 255, 0.15);
  box-shadow: 1px 0px 15px rgba(0, 0, 0, 0.45);
  border-radius:10px;
  padding:20px 20px 20px 20px;
}
.btn-grp {
  padding:20px 20px 20px 20px;
}
</style>