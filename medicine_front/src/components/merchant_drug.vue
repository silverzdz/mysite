<template>
  <div class="merchant-drug">
      <div class="mer box_border">
          <el-row class="logo">
              <el-col :span="24">
                  <img src="../assets/logo.png">
              </el-col>
          </el-row>
          <el-row class="title">
                <el-col :span="24">
                    <h1>欢迎，卖家{{this.$route.query.userId}}！</h1>
                </el-col>
            </el-row>
          <el-row class="input-box-1" type="flex" justify="center" align="middle">
              <el-col :span="8" >
                <el-input v-model="id_input" placeholder="请输入药品ID" style="display:inline-table; width:90%; float:left" min-width="120"></el-input>
              </el-col>
              <el-col :span="8">
                <el-input v-model="name_input" placeholder="请输入药品名" style="display:inline-table; width:90%; float:left" min-width="120"></el-input>
              </el-col>
              <el-col :span="8">
                <el-input v-model="inventory_input" placeholder="请输入药品库存" style="display:inline-table; width:90%; float:left" min-width="120"></el-input>
              </el-col>
              <el-button type="primary" @click="addDrug()" style="float:left; margin: 2px;">添加</el-button>
          </el-row>
          <el-row class="table" type="flex" justify="center" align="middle">
              <el-table :data="drugList" :header-cell-style="{textAlign: 'center'}" :cell-style="{ textAlign: 'center' }" border >
                <el-table-column prop="id" label="药品ID" min-width="100" >
                    <template slot-scope="scope"> {{ scope.row.pk }} </template>
                </el-table-column>
                <el-table-column prop="drug_name" label="药品名" min-width="150">
                    <template slot-scope="scope"> {{ scope.row.fields.drug_name }} </template>
                </el-table-column>
                <el-table-column prop="add_time" label="入库时间" min-width="200">
                    <template slot-scope="scope"> {{ scope.row.fields.add_time }} </template>
                </el-table-column>
                <el-table-column prop="drug_inventory" label="药品库存" min-width="100">
                    <template slot-scope="scope"> {{ scope.row.fields.drug_inventory }} </template>
                </el-table-column>
                <el-table-column prop="delete" label="操作" min-width="100">
                    <template slot-scope="scope">
                        <el-button type="primary" @click="deleteDrug(scope.row.pk)">删除</el-button>
                    </template>
                </el-table-column>
              </el-table>
          </el-row>
      </div>
  </div>
</template>

<script>
export default {
  name: 'merchant_drug',
  data () {
    return {
      id_input: '',
      name_input: '',
      inventory_input: '',
      drugList: [],
    }
  },
  mounted: function() {
      this.showDrugs()
  },
  methods: {
    addDrug(){
      this.$axios.get('http://localhost:8000/medicine/add_drug?drug_id='+this.id_input+'&drug_name='+this.name_input+'&drug_inventory='+this.inventory_input)
        .then((response) => {
            var res = JSON.parse(response.request.response)
            if (res.error_num == 0) {
              this.showDrugs();
              this.id_input='';
              this.name_input='';
              this.inventory_input='';
            } else {
              this.$message.error('添加药品失败，请重试')
            }
        })
    },
    showDrugs(){
      this.$axios.get('http://localhost:8000/medicine/show_drugs')
        .then((response) => {
            var res = JSON.parse(response.request.response)
            if (res.error_num == 0) {
              this.drugList = res['list']
            } else {
              this.$message.error('找不到该药品！')
            }
        })
    },
    deleteDrug: function(id){
        console.log(id);
        var url = 'http://localhost:8000/medicine/delete_drug?drug_id='+id;
        this.$axios.get(url).then((response) => {
            var res = JSON.parse(response.request.response)
            if (res.error_num == 0){
                this.$message.success('删除成功！');
                this.showDrugs();
            }
            else{
                console.log(res['msg']);
                this.$message.error('删除失败！');
            }
        });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.merchant-drug{
    width:100%;
    height:100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
}
.logo{
    text-align: center;
    margin:5px !important;
}
.el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
}
.title{
    text-align: center;
    margin: 5px 5px 0px 5px !important;
}
.input-box{
    text-align: center;
    margin:0px !important;
}
.table{
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