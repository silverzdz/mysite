<template>
    <div class="chat-page">
        <div class = "chat box_border">
            <h4>欢迎，医生{{this.$route.query.d_id}}，您诊断的病人是{{this.$route.query.p_id}}。</h4>
        </div>
    </div>
</template>

<script>

</script>

<style scoped>
.chat-page{
    width:100%;
    height:100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
}
.logo{
    text-align: center;
    margin: 5px !important;
}
.title{
    text-align: center;
    margin: 0 auto;
}
h1, h2, h3, h4 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
.option{
  text-align: center;
  margin: 0 auto;
}
a {
  color: #42b983;
}
</style>