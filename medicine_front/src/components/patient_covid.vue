<template>
    <div class="covid-page">
        <div class="cov box_border">
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
            <el-form ref="form" :model="form" :rules="rules" @submit.native.prevent>
                <el-row>
                    <el-col :span="20" :offset="2">
                        <el-form-item prop="hospital">
                            <el-input type="text" placeholder="请输入预约医院" v-model="form.hospital"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="20" :offset="2">
                        <el-form-item prop="date">
                            <el-date-picker type="date" placeholder="请选择预约时间" v-model="form.date" style="width:99.5%"></el-date-picker>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="24" class="option">
                        <el-form-item prop="type" >
                            <el-radio v-model="form.type" label="1">核酸检测</el-radio>
                            <el-radio v-model="form.type" label="2">新冠疫苗</el-radio>
                        </el-form-item>
                    </el-col>
                </el-row>
            </el-form>
            <el-row class="btn-grp" :span="24">
                <el-button type="primary" class="btn-reg" @click="DoRegister('form')">预约</el-button>
                <el-button type="primary" class="btn-back" @click="GoBack()">返回个人主页</el-button>
            </el-row>
        </div>
    </div>
</template>

<script>
export default {
    name:"patient_covid",
    data() {
        return {
            form: {
                hospital: '',
                date: '',
                type: '0'
            },
            rules: {
                hospital:[
                    {required: true, message: '请输入预约医院', trigger: 'blur'}
                ],
                date:[
                    {required: true, message: '请选择预约时间', trigger: 'blur'}
                ],
                type:[
                    {required: true, message: '请选择预约类型', trigger: 'blur'}
                ]
            }
        }
    },
    methods:{
        DoRegister:function(formName){
            this.$refs[formName].validate((valid) => {
                if(valid){
                    
                    var url_1 = 'http://localhost:8000/appointment/get_c_id';
                    this.$axios.get(url_1).then((response_1) =>{
                        var res_1 = JSON.parse(response_1.request.response);
                        console.log(res_1['msg'])
                        if(res_1.error_num == 0) {
                            var c_id = res_1.res;
                            
                            var now = new Date(this.form.date);
                            var year = now.getFullYear();
                            var month = now.getMonth()+1;
                            var day = now.getDate();
                            var back_url = 'year='+year+'&month='+month+'&day='+day+'&c_id='+c_id+'&c_hospital='+this.form.hospital+'&c_type='+this.form.type+'&p_id='+this.$route.query.userId;
                            var url_2 = 'http://localhost:8000/appointment/add_covid?'+back_url;
                            this.$axios.get(url_2).then((response_2) => {
                                var res_2 = JSON.parse(response_2.request.response);
                                //console.log(res_2['msg']);
                                if(res_2.error_num == 0){
                                    this.$message.success('预约成功！');
                                }
                                else if(res_2.error_num == 1){
                                    this.$message.error('预约失败！');
                                }
                                else{
                                    this.$message.error('请选择预约类型！');
                                }
                                this.form.hospital = '';
                                this.form.date = '';
                                this.form.type = '';
                            });
                        }
                    });
                }
            });
        },
        GoBack:function(){
            this.$router.push({ path: '/patient', query:{userId: this.$route.query.userId}});
        }
    }
}
</script>

<style scoped>
.covid-page{
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