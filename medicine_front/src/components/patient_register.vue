<template>
    <div class="register-page">
        <div class="reg">
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
                            <el-input type="text" placeholder="请输入挂号医院" v-model="form.hospital"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="20" :offset="2">
                        <el-form-item prop="department">
                            <el-input type="text" placeholder="请输入挂号科室" v-model="form.department"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="20" :offset="2">
                        <el-form-item prop="date">
                            <el-date-picker type="date" placeholder="请选择挂号时间" v-model="form.date"></el-date-picker>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="20" :offset="2">
                        <el-form-item prop="doctor">
                            <el-input type="text" placeholder="请输入挂号医生" v-model="form.doctor"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
            </el-form>
            <el-row class="btn-grp" :span="24">
                <el-button type="primary" class="btn-reg" @click="DoRegister('form')">挂号</el-button>
                <el-button type="primary" class="btn-back" @click="GoBack()">返回个人主页</el-button>
            </el-row>
        </div>
    </div>
</template>

<script>
export default {
    name:"patient_register",
    data() {
        return {
            form: {
                hospital: '',
                department: '',
                date: '',
                doctor: ''
            },
            rules: {
                hospital:[
                    {required: true, message: '请输入挂号医院', trigger: 'blur'}
                ],
                department:[
                    {required: true, message: '请输入挂号科室', trigger: 'blur'}
                ],
                date:[
                    {required: true, message: '请选择挂号时间', trigger: 'blur'}
                ],
                doctor:[
                    {required: true, message: '请输入挂号医生', trigger: 'blur'}
                ]
            }
        }
    },
    methods:{
        DoRegister:function(formName){
            this.$refs[formName].validate((valid) => {
                if(valid){
                    var url_1 = 'http://localhost:8000/appointment/get_r_id';
                    this.$axios.get(url_1).then((response_1) =>{
                        var res_1 = JSON.parse(response_1.request.response);
                        if(res_1.error_num == 0) {
                            var r_id = res_1.res;
                            var now = new Date(this.form.date);
                            var year = now.getFullYear();
                            var month = now.getMonth()+1;
                            var day = now.getDate();
                            var back_url_1 = 'year='+year+'&month='+month+'&day='+day+'&r_id='+r_id+'&r_hospital='+this.form.hospital;
                            var back_url_2 = '&r_department='+this.form.department+'&d_id='+this.form.doctor+'&p_id='+this.$route.query.userId;
                            var url_2 = 'http://localhost:8000/appointment/add_register?'+back_url_1+back_url_2;
                            this.$axios.get(url_2).then((response_2) => {
                                var res_2 = JSON.parse(response_2.request.response);
                                if(res_2.error_num == 0){
                                    this.$message.success('挂号成功！');
                                }
                                else{
                                    this.$message.error('挂号失败！');
                                }
                                this.form.hospital = '';
                                this.form.department = '';
                                this.form.date = '';
                                this.form.doctor = '';
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
.register-page{
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
a {
  color: #42b983;
}
</style>