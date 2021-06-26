<template>
    <div class="admin-page">
        <div class="admin-grp">
            <el-row class="logo">
                <el-col :span="24">
                    <img src="../assets/logo.png">
                </el-col>
            </el-row>
            <el-row class="title">
                <el-col :span="24">
                    <h1>欢迎！管理员{{this.$route.query.userId}}！</h1>
                </el-col>
            </el-row>
            <el-row class="btn-grp" :span="24">
                <el-button type="primary" class="btn-doctor" @click="ToDoctor()">医生管理</el-button>
                <el-button type="primary" class="btn-merchant" @click="ToMerchant()">商人管理</el-button>
            </el-row>
        </div>
    </div>
</template>

<script>
export default {
    name:"admin_index",
    data() {
        return {
            
        }
    },
    methods:{
        ToDoctor:function(){
            this.$router.push({path:'/admin/add_doctor', query: {userId: this.$route.query.userId}});
        },
        ToMerchant:function(){
            this.$router.push({path:'/admin/add_merchant', query: {userId: this.$route.query.userId}});
        }
    }
}
</script>

<style scoped>
.admin-page{
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
.btn-grp{
    text-align: center;
    margin: 0 auto;
}
h1, h2 {
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
a {
  color: #42b983;
}
</style>