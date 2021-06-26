<template>
    <div class="add-merchant-page">
        <div class="mer">
            <el-row class="logo">
                <el-col :span="24">
                    <img src="../assets/logo.png">
                </el-col>
            </el-row>
            <el-row class="input-box-1" type="flex" justify="center" align="middle">
                <el-input v-model="id_input" placeholder="请输入商人ID" style="display:inline-table; width: 25%; float:left"></el-input>
                <el-input v-model="name_input" placeholder="请输入商人姓名" style="display:inline-table; width: 25%; float:left"></el-input>
            </el-row>
            <el-row class="input-box-2" type="flex" justify="center" align="middle">
                <el-input v-model="telephone_input" placeholder="请输入商人联系电话" style="display:inline-table; width: 25%; float:left"></el-input>
                <el-input v-model="pw_input" placeholder="请输入商人密码" style="display:inline-table; width: 25%; float:left"></el-input>
                <el-button type="primary" @click="addMer()" style="float:left; margin: 2px;">添加</el-button>
            </el-row>
            <el-row class="table" type="flex" justify="center" align="middle">
                <el-table :data="merList" :header-cell-style="{textAlign: 'center'}" :cell-style="{ textAlign: 'center' }" border>
                    <el-table-column prop="m_id" label="商人ID" min-width="100">
                        <template slot-scope="scope"> {{scope.row.pk}} </template>
                    </el-table-column>
                    <el-table-column prop="m_name" label="姓名" min-width="100">
                        <template slot-scope="scope"> {{scope.row.fields.m_name}} </template>
                    </el-table-column>
                    <el-table-column prop="m_telephone" label="联系电话" min-width="150">
                        <template slot-scope="scope"> {{scope.row.fields.m_telephone}} </template>
                    </el-table-column>
                </el-table>
            </el-row>
        </div>
    </div>
</template>

<script>
export default {
    name: "add_merchant",
    data() {
        return {
            id_input: '',
            name_input: '',
            telephone_input: '',
            pw_input: '',
            merList: [],
        }
    },
    mounted: function() {
        this.showMers()
    },
    methods: {
        showMers(){
            var url = 'http://localhost:8000/identity/show_mers';
            this.$axios.get(url).then((response) => {
                var res = JSON.parse(response.request.response);
                if (res.error_num == 0) {
                    console.log(res['list']);
                    this.merList = res['list'];
                }
                else {
                    this.$message.error('Fail to search merchants!');
                }
            })
        },
        addMer(){
            var back_url = 'm_id='+this.id_input+'&m_name='+this.name_input+'&m_telephone='+this.telephone_input+'&m_pw='+this.pw_input;
            var url = 'http://localhost:8000/identity/add_merchant?'+back_url;
            this.$axios.get(url).then((response) => {
                var res = JSON.parse(response.request.response);
                if (res.error_num == 0) {
                    this.showMers();
                    this.id_input='';
                    this.name_input='';
                    this.telephone_input='';
                    this.pw_input='';
                }
                else{
                    this.$message.error('Fail to add the merchant, please retry!')
                }
            })
        }
    }
}
</script>

<style scoped>
.add-merchant-page{
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