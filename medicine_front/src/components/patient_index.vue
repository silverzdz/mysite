<template>
    <div class="patient-page">
        <div class="patient-grp box_border">
            <el-row class="logo">
                <el-col :span="24">
                    <img src="../assets/logo.png">
                </el-col>
            </el-row>
            <el-row class="title">
                <el-col :span="24">
                    <h1>欢迎！病人{{this.$route.query.userId}}！</h1>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="5" :offset="-5">
                    <h3>我的挂号：</h3>
                </el-col>
            </el-row>
            <el-row class="table-1" type="flex" justify="center" align="middle">
                <el-table :data="registerList" :header-cell-style="{textAlign: 'center'}" :cell-style="{ textAlign: 'center' }" border>
                    <el-table-column prop="r_id" label="预约号" min-width="100">
                        <template slot-scope="scope"> {{scope.row.pk}} </template>
                    </el-table-column>
                    <el-table-column prop="r_hospital" label="医院" min-width="150">
                        <template slot-scope="scope"> {{scope.row.fields.r_hospital}} </template>
                    </el-table-column>
                    <el-table-column prop="r_department" label="科室" min-width="150">
                        <template slot-scope="scope"> {{scope.row.fields.r_department}} </template>
                    </el-table-column>
                    <el-table-column prop="r_time" label="时间" min-width="150">
                        <template slot-scope="scope"> {{scope.row.fields.r_time}} </template>
                    </el-table-column>
                    <el-table-column prop="d_id" label="医生" min-width="100">
                        <template slot-scope="scope"> {{scope.row.fields.d_id}} </template>
                    </el-table-column>
                </el-table>
            </el-row>
            <el-row>
                <el-col :span="5" :offset="-5">
                    <h3>我的预约：</h3>
                </el-col>
            </el-row>
            <el-row class="table-2" type="flex" justify="center" align="middle">
                <el-table :data="covidList" :header-cell-style="{textAlign: 'center'}" :cell-style="{ textAlign: 'center' }" border>
                    <el-table-column prop="c_id" label="预约号" min-width="100">
                        <template slot-scope="scope"> {{scope.row.pk}} </template>
                    </el-table-column>
                    <el-table-column prop="c_type" label="类型" min-width="100">
                        <template slot-scope="scope"> {{scope.row.fields.c_type=='1'?'核酸检测':'新冠疫苗'}} </template>
                    </el-table-column>
                    <el-table-column prop="c_hospital" label="医院" min-width="150">
                        <template slot-scope="scope"> {{scope.row.fields.c_hospital}} </template>
                    </el-table-column>
                    <el-table-column prop="c_time" label="时间" min-width="150">
                        <template slot-scope="scope"> {{scope.row.fields.c_time}} </template>
                    </el-table-column>
                </el-table>
            </el-row>
            <el-row class="btn-grp" :span="24">
                <el-button type="primary" class="btn-query" @click="ToQuery()">轻度问诊</el-button>
                <el-button type="primary" class="btn-register" @click="ToRegister()">线上挂号</el-button>
                <el-button type="primary" class="btn-medicine" @click="ToMedicine()">线上购药</el-button>
                <el-button type="primary" class="btn-covid" @click="ToCovid()">核酸检测/新冠疫苗预约</el-button>
            </el-row>
        </div>
    </div>
</template>

<script>
export default {
    name:"patient_index",
    data() {
        return {
            registerList: [],
            covidList: [],
        }
    },
    mounted: function() {
        this.showRegister(),
        this.showCovid()
    },
    methods:{
        ToQuery:function(){
            this.$router.push({path:'patient/query', query: {userId: this.$route.query.userId}});
        },
        ToRegister:function(){
            this.$router.push({path:'patient/register', query: {userId: this.$route.query.userId}});
        },
        ToCovid:function(){
            this.$router.push({path:'patient/covid', query: {userId: this.$route.query.userId}});
        },
        ToMedicine:function(){
            this.$router.push({path:'patient/medicine', query: {userId: this.$route.query.userId}});
        },
        showRegister:function(){
            var url = 'http://localhost:8000/appointment/check_register?p_id='+this.$route.query.userId;
            this.$axios.get(url).then((response) => {
                var res = JSON.parse(response.request.response);
                if(res.error_num == 0) {
                    this.registerList = res['list'];
                }
                else {
                    this.$message.error('Fail to check register records!');
                }
            });
        },
        showCovid:function(){
            var url = 'http://localhost:8000/appointment/check_covid?p_id='+this.$route.query.userId;
            this.$axios.get(url).then((response) => {
                var res = JSON.parse(response.request.response);
                if(res.error_num == 0) {
                    this.covidList = res['list'];
                }
                else {
                    this.$message.error('Fail to check covid register records!');
                }
            });
        }
    }
}
</script>

<style scoped>
.patient-page{
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
.table-1{
  width: 100%;
  margin: 0 auto;
  display:flex;
  align-items: center;
  text-align: center;
}
.table-2{
  width: 100%;
  margin: 0 auto;
  display:flex;
  align-items: center;
  text-align: center;
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