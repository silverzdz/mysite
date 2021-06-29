<template>
    <div class="sign-page">
        <div class="sign box_border">
            <el-row class="logo">
                <el-col :span="24">
                    <img src="../assets/logo.png">
                </el-col>
            </el-row>
            <el-row class="title">
                <el-col :span="24">
                    <h1>新用户注册</h1>
                </el-col>
            </el-row>
            <el-form class="login-table" ref="from" :model="form" :rules="rules" @submit.native.prevent>
                <el-row >
                    <el-col :span="4">
                        <h4>用户名</h4>
                    </el-col>
                    <el-col :span="18" :offset="2">
                        <el-form-item prop="id">
                            <el-input type="text" placeholder="请输入用户名" v-model="form.id"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row >
                    <el-col :span="4">
                        <h4>密码</h4>
                    </el-col>
                    <el-col :span="18" :offset="2">
                        <el-form-item prop="pw">
                            <el-input type="text" placeholder="请输入密码" v-model="form.pw" show-password></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row >
                    <el-col :span="4">
                        <h4>再次输入密码</h4>
                    </el-col>
                    <el-col :span="18" :offset="2">
                        <el-form-item prop="pw2">
                            <el-input type="text" placeholder="请再次输入密码" v-model="form.pw2" show-password></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row >
                    <el-col :span="4">
                        <h4>姓名</h4>
                    </el-col>
                    <el-col :span="18" :offset="2">
                        <el-form-item prop="name">
                            <el-input type="text" placeholder="请输入姓名" v-model="form.name"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row >
                    <el-col :span="4">
                        <h4>电话</h4>
                    </el-col>
                    <el-col :span="18" :offset="2">
                        <el-form-item prop="telephone">
                            <el-input type="text" placeholder="请输入电话" v-model="form.telephone"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
            </el-form>
            <el-row class="btn" :span="24">
                    <el-button type="primary" class="btn-sign" @click="signup('form')">注册</el-button>
                    <el-button type="primary" class="btn-back" @click="back()">返回</el-button>
            </el-row>
        </div>
    </div>
</template>

<script>
export default {
    name: "sign_up",
    data(){
        return{
            form: {
                id: '',
                pw: '',
                pw2: '',
                name: '',
                telephone: ''
            },
            rules: {
                id:[
                    {required: true, message: '请输入用户名', trigger: 'blur'}
                ],
                pw:[
                    {required: true, message: '请输入密码', trigger: 'blur'}
                ],
                pw2:[
                    {required: true, message: '请再次输入密码', trigger: 'blur'}
                ],
                name:[
                    {required: true, message: '请输入姓名', trigger: 'blur'}
                ],
                telephone:[
                    {required: true, message: '请输入电话', trigger: 'blur'}
                ]
            }
        }
    },
    methods:{
        signup: function(formName){
            if(this.form.pw != this.form.pw2){
                this.$message.error('两次输入的密码不一致！');
            }
            else{
                var back_url = 'p_id='+this.form.id+'&p_pw='+this.form.pw+'&p_name='+this.form.name+'&p_telephone='+this.form.telephone;
                var url = 'http://localhost:8000/identity/add_patient?'+back_url;
                this.$axios.get(url).then((response) => {
                    var res = JSON.parse(response.request.response);
                    if(res.error_num == 0){
                        this.$message.success('注册成功！');
                        this.$router.push({path: '/'});
                    }
                    else{
                        this.$message.error('注册失败！');
                    }
                });
            }
        },
        back: function(){
            this.$router.push({path: '/'});
        }
    }
}
</script>

<style scoped>
.sign-page{
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
.login-table{
  text-align: center;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
.btn{
  text-align: center;
  margin: 0 auto;
}

a {
  color: #42b983;
}
</style>