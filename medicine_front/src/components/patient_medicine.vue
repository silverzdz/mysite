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
                  <h1>欢迎，病人{{this.$route.query.userId}}！</h1>
              </el-col>
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
                        <el-button type="primary" @click="buyDrug(scope.row.pk)">购买</el-button>
                    </template>
                </el-table-column>
              </el-table>
          </el-row>
      </div>
  </div>
</template>

<script>
export default {
  name: 'patient_medicine',
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
              this.$message.error('Fail to add the drug, please retry!')
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
              this.$message.error('Fail to search drug!')
            }
        })
    },
    buyDrug: function(id){
        this.$prompt('请输入购买数量','提示',{
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            inputPattern: /^([1-9][0-9]*)$/,
            inputErrorMessage: '非法的数量'
        }).then((value) => {
            var url = 'http://localhost:8000/medicine/buy_drug?drug_id='+id+'&buy_num='+value['value'];
            this.$axios.get(url).then((response) => {
                var res = JSON.parse(response.request.response);
                if(res.error_num == 0){
                    this.$message.success('Buy success!');
                    this.showDrugs();
                }
                else{
                    console.log(res['msg']);
                    this.$message.error('Fail to buy drug!');
                }
            });
        }).catch(() => {
            this.$message({
                type: 'info',
                message: '取消输入'
            });
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
.title{
    text-align: center;
    margin: 5px 5px 0px 5px !important;
}
.input-box{
    text-align: center;
    margin:5px !important;
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