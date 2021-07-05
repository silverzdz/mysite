<template>
    <div class="patient-query-page">
        <div class="p-query box_border">
            <el-row class="logo">
                <el-col :span="24">
                    <img src="../assets/logo.png">
                </el-col>
            </el-row>
            <el-row class="title">
                <el-col :span="24">
                    <h1>医生列表</h1>
                </el-col>
            </el-row>
            <el-row class="table" type="flex" justify="center" align="middle">
                <el-table :data="docList" :header-cell-style="{textAlign: 'center'}" :cell-style="{ textAlign: 'center' }" border>
                    <el-table-column prop="d_name" label="姓名" min-width="100">
                        <template slot-scope="scope"> {{scope.row.fields.d_name}} </template>
                    </el-table-column>
                    <el-table-column prop="d_telephone" label="联系电话" min-width="150">
                        <template slot-scope="scope"> {{scope.row.fields.d_telephone}} </template>
                    </el-table-column>
                    <el-table-column prop="d_hospital" label="医院" min-width="150">
                        <template slot-scope="scope"> {{scope.row.fields.d_hospital}} </template>
                    </el-table-column>
                    <el-table-column prop="d_department" label="部门" min-width="150">
                        <template slot-scope="scope"> {{scope.row.fields.d_department}} </template>
                    </el-table-column>
                    <el-table-column prop="query" label="操作" min-width="100">
                        <template slot-scope="scope">
                            <el-button type="primary" @click="gotoChat(scope.row.fields.d_name)">问诊</el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </el-row>
        </div>
    </div>
</template>

<script>
export default {
    name: 'patient_query',
    data() {
        return {
            docList: [],
        }
    },
    mounted: function() {
        this.showDocs()
    },
    methods: {
        showDocs(){
            var url = 'http://localhost:8000/identity/show_docs';
            this.$axios.get(url).then((response) => {
                var res = JSON.parse(response.request.response);
                if (res.error_num == 0) {
                    //console.log(res['list']);
                    this.docList = res['list'];
                }
                else {
                    this.$message.error('Fail to search doctors!');
                }
            })
        },
        gotoChat: function(id){
            this.$router.push({ path: '/patient/query/chat', query: {p_id: this.$route.query.userId, d_id: id} });
        }
    }
}
</script>

<style scoped>
.patient-query-page{
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