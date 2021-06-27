<template>
    <div class="add-doctor-page">
        <div class="doc box_border">
            <el-row class="logo">
                <el-col :span="24">
                    <img src="../assets/logo.png">
                </el-col>
            </el-row>
            <el-row class="input-box-1" type="flex" justify="center" align="middle">
                <el-input v-model="id_input" placeholder="请输入医生ID" style="display:inline-table; width: 25%; float:left"></el-input>
                <el-input v-model="name_input" placeholder="请输入医生姓名" style="display:inline-table; width: 25%; float:left"></el-input>
                <el-input v-model="telephone_input" placeholder="请输入医生联系电话" style="display:inline-table; width: 25%; float:left"></el-input>
            </el-row>
            <el-row class="input-box-2" type="flex" justify="center" align="middle">
                <el-input v-model="hospital_input" placeholder="请输入医生ID" style="display:inline-table; width: 25%; float:left"></el-input>
                <el-input v-model="department_input" placeholder="请输入医生姓名" style="display:inline-table; width: 25%; float:left"></el-input>
                <el-input v-model="pw_input" placeholder="请输入医生密码" style="display:inline-table; width: 25%; float:left"></el-input>
                <el-button type="primary" @click="addDoc()" style="float:left; margin: 2px;">添加</el-button>
            </el-row>
            <el-row class="table" type="flex" justify="center" align="middle">
                <el-table :data="docList" :header-cell-style="{textAlign: 'center'}" :cell-style="{ textAlign: 'center' }" border>
                    <el-table-column prop="d_id" label="医生ID" min-width="100">
                        <template slot-scope="scope"> {{scope.row.pk}} </template>
                    </el-table-column>
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
                </el-table>
            </el-row>
        </div>
    </div>
</template>

<script>
export default {
    name: 'add_doctor',
    data() {
        return {
            id_input: '',
            name_input: '',
            telephone_input: '',
            hospital_input: '',
            department_input: '',
            pw_input: '',
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
        addDoc(){
            var back_url = 'd_id='+this.id_input+'&d_name='+this.name_input+'&d_telephone='+this.telephone_input + '&d_hospital='+this.hospital_input+'&d_department='+this.department_input+'&d_pw='+this.pw_input;
            var url = 'http://localhost:8000/identity/add_doctor?'+back_url;
            this.$axios.get(url).then((response) => {
                var res = JSON.parse(response.request.response);
                if (res.error_num == 0) {
                    this.showDocs();
                    this.id_input='';
                    this.name_input='';
                    this.telephone_input='';
                    this.hospital_input='';
                    this.department_input='';
                    this.pw_input='';
                }
                else{
                    this.$message.error('Fail to add the doctor, please retry!')
                }
            })
        }
    }
}
</script>

<style scoped>
.add-doctor-page{
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