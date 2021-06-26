<template>
    <div class="index">
        <div class="login-box">
            <el-row class="logo">
                <el-col :span="24">
                    <img src="../assets/logo.png">
                </el-col>
            </el-row>
            <el-row class="title">
                <el-col :span="24">
                    <h1>互联网医疗服务系统</h1>
                </el-col>
            </el-row>
            <el-form class="login-table" ref="form" :model="form">
                <el-row>
                    <el-col :span="4">
                        <h4>用户名</h4>
                    </el-col>
                    <el-col :span="18" :offset="2">
                        <el-form-item prop="userName">
                            <el-input type="text" placeholder="请输入用户名" v-model="form.userName"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="4">
                        <h4>密码</h4>
                    </el-col>
                    <el-col :span="18" :offset="2">
                        <el-form-item prop="userPass">
                            <el-input type="password" placeholder="请输入密码" v-model="form.userPass"></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col class="option" :span="24" >
                        <el-form-item prop="userType">
                            <el-radio v-model="form.userType" label="1">病人</el-radio>
                            <el-radio v-model="form.userType" label="2">医生</el-radio>
                            <el-radio v-model="form.userType" label="3">商人</el-radio>
                            <el-radio v-model="form.userType" label="4">管理员</el-radio>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col class="btn" :span="20">
                        <el-form-item prop="loginButton">
                            <el-button type="primary" class="btn-submit" @click="login('form')">登录</el-button>
                            <el-button type="primary" class="btn-signup" @click="signup()">新用户注册</el-button>
                        </el-form-item>
                    </el-col>
                </el-row>
            </el-form>
        </div>
    </div>
</template>

<script>
export default {
  name:"index",
  data() {
    return {
      form: {
        userName:'',
        userPass:'',
        userType:'0'
      },
      rules:{
        userName:[
          {required: true, message: '请输入用户名', trigger:'blur'}
        ],
        userPass:[
          {required: true, message: '请输入密码', trigger:'blur'}
        ]
      }
    }
  },
  methods:{
    signup: function(){
      this.$router.push({path: '/sign_up'});
    },
    login:function(formName){
      this.$refs[formName].validate((valid)=>{
        var url_replace='';
        var id_str='';
        var pw_str='';
        switch(this.form.userType) {
          case '1':
            url_replace='login_patient';
            id_str='p_id';
            pw_str='p_pw';
            break;
          case '2':
            url_replace='login_doctor';
            id_str='d_id';
            pw_str='d_pw';
            break;
          case '3':
            url_replace='login_merchant';
            id_str='m_id';
            pw_str='m_pw';
            break;
          case '4':
            url_replace='login_admin';
            id_str='a_id';
            pw_str='a_pw';
            break;
        }
        var url = 'http://localhost:8000/identity/'+url_replace+'?'+id_str+'='+this.form.userName+'&'+pw_str+'='+this.form.userPass;
        this.$axios.get(url).then((response)=>{
          var res = JSON.parse(response.request.response);
          if(res.error_num == 0) {
            console.log('Login '+this.form.userName+' success!');
            if (this.form.userType=='4'){
              this.$router.push({ path: '/admin', query: {userId: this.form.userName}});
            }
            else if(this.form.userType=='1'){
              this.$router.push({ path: '/patient', query: {userId: this.form.userName}});
            }
            else if(this.form.userType=='2'){
              this.$router.push({ path: '/doctor', query: {userId: this.form.userName}});
            }
            else if(this.form.userType=='3'){
              this.$router.push({ path: '/merchant/drug', query: {userId: this.form.userName}});
            }
            else{
              this.$router.push({ path:'/medicine'});
            }
          }
          else{
            this.$message.error('Login failed!');
            console.log(res['msg']);
          }
        })
      })
    }
  }
}
</script>

<style scoped>
.index{
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
    margin: 5px 5px 0px 5px !important;
}
.login-table{
  text-align: center;
}
.btn{
  text-align: center;
  margin: 0 auto;
}
.option{
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