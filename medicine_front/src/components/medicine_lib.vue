<template>
  <div class="medicine_lib">
    <el-row class="logo box_border">
        <el-col :span="24">
            <img src="../assets/logo.png">
        </el-col>
    </el-row>
    <el-row class="input-box" type="flex" justify="center" align="middle">
        <el-input v-model="id_input" placeholder="Please input drug id" style="display:inline-table; width: 25%; float:left"></el-input>
        <el-input v-model="name_input" placeholder="Please input drug name" style="display:inline-table; width: 25%; float:left"></el-input>
        <el-input v-model="inventory_input" placeholder="Please input drug inventory" style="display:inline-table; width: 25%; float:left"></el-input>
        <el-button type="primary" @click="addDrug()" style="float:left; margin: 2px;">Add</el-button>
    </el-row>
    <el-row class="table" type="flex" justify="center" align="middle">
        <el-table :data="drugList" :header-cell-style="{textAlign: 'center'}" :cell-style="{ textAlign: 'center' }" border >
          <el-table-column prop="id" label="drug-id" min-width="100" >
            <template slot-scope="scope"> {{ scope.row.pk }} </template>
          </el-table-column>
          <el-table-column prop="drug_name" label="drug-name" min-width="100">
            <template slot-scope="scope"> {{ scope.row.fields.drug_name }} </template>
          </el-table-column>
          <el-table-column prop="add_time" label="add-time" min-width="100">
            <template slot-scope="scope"> {{ scope.row.fields.add_time }} </template>
          </el-table-column>
          <el-table-column prop="drug_inventory" label="drug-inventory" min-width="100">
            <template slot-scope="scope"> {{ scope.row.fields.drug_inventory }} </template>
          </el-table-column>
        </el-table>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'medicine_lib',
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
      this.$axios.get('http://127.0.0.1:8000/medicine/add_drug?drug_id='+this.id_input+'&drug_name='+this.name_input+'&drug_inventory='+this.inventory_input)
        .then((response) => {
            var res = JSON.parse(response.request.response)
            if (res.error_num == 0) {
              this.showDrugs();
              this.id_input='';
              this.name_input='';
              this.inventory_input='';
            } else {
              this.$message.error('Fail to add the drug, please retry!')
              console.log(res['msg'])
            }
        })
    },
    showDrugs(){
      this.$axios.get('http://127.0.0.1:8000/medicine/show_drugs')
        .then((response) => {
            var res = JSON.parse(response.request.response)
            if (res.error_num == 0) {
              console.log(res['list'])
              this.drugList = res['list']
            } else {
              this.$message.error('Fail to search drug!')
              console.log(res['msg'])
            }
            console.log("finish")
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.logo{
    text-align: center;
    margin:5px !important;
}
.input-box{
    text-align: center;
    margin:5px !important;
}
.table{
  width: 80%;
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