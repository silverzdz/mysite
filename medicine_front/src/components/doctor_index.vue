<template>
    <div class="doctor-query-page">
        <div class="d-query box_border">
            <el-row class="logo">
                <el-col :span="24">
                    <img src="../assets/logo.png">
                </el-col>
            </el-row>
            <el-row class="title">
                <el-col :span="24">
                    <h1>病人列表</h1>
                </el-col>
            </el-row>
            <el-row class="table" type="flex" justify="center" align="middle">
                <el-table :data="docList" :header-cell-style="{textAlign: 'center'}" :cell-style="{ textAlign: 'center' }" border>
                    <el-table-column prop="p_id" label="病人ID" min-width="100">
                        <template slot-scope="scope"> {{scope.row.pk}} </template>
                    </el-table-column>
                    <el-table-column prop="p_telephone" label="联系电话" min-width="150">
                        <template slot-scope="scope"> {{scope.row.fields.p_telephone}} </template>
                    </el-table-column>
                    <el-table-column prop="query" label="操作" min-width="100">
                        <template slot-scope="scope">
                            <el-button type="primary" @click="gotoChat(scope.row.pk)">问诊</el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </el-row>
        </div>
    </div>
</template>

<script>
export default {
    name: 'doctor_query',
    data() {
        return {
            docList: [],
        }
    },
    mounted: function() {
        this.showPatients()
    },
    methods: {
        showPatients(){
            var url = 'http://localhost:8000/identity/show_patients';
            this.$axios.get(url).then((response) => {
                var res = JSON.parse(response.request.response);
                if (res.error_num == 0) {
                    //console.log(res['list']);
                    this.docList = res['list'];
                }
                else {
                    this.$message.error('Fail to search patients!');
                }
            })
        },
        gotoChat: function(id){
            this.$router.push({ path: '/doctor/chat', query: {d_id: this.$route.query.userId, p_id: id} });
        }
    }
}
</script>

<style scoped>
.doctor-query-page{
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
.el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
}
.table{
  width: 100%;
  margin: 0 auto;
  display:flex;
  align-items: center;
  text-align: center;
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
a {
  color: #42b983;
}
</style>