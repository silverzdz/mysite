# mysite
仅上传了后端，供测试同学测试

**尽量在Linux环境下运行！！**

首先安装pip和python：

```sh
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
```

之后安装django和mysql：

```sh
sudo pip3 install Django
sudo apt install python-django-common
sudo pip3 install pymysql
sudo apt install mysql-server
sudo apt install mysql-clinet
```

安装好后，设置mysql：

```sh
sudo service mysql restart
sudo mysql_secure_installation
y
0
输入两次root密码
y
y
n
直接回车
直接回车
sudo mysql
set global validate_password.policy=0;
set global validate_password.length=1;
create user 'django'@'localhost' identified by 'django-user-password';
grant usage on *.* to 'django'@'localhost';
grant all privileges on django-database-1.* to 'django'@'localhost';
create database mysite_db;
quit;
sudo pip3 install django-cors-headers
```

这里也可以使用不同的用户名和密码，但要注意在mysite目录下的settings.py中DATABASES里改掉。

之后启动后端：

```sh
python3 manage.py makemigrations medicine
python3 manage.py makemigrations appointment
python3 manage.py makemigrations identify
python3 manage.py migrate
python3 manage.py runserver
```

之后就可以开始测试了。测试的主要方式为利用http请求。**只需进行具体类测试和压力测试即可！**

这里举个例子，比如说要测试identity模块中添加admin功能，可以看到` ./identity/views.py`中定义了add_admin方法，要传递的参数在` ./identity/models.py`中，因此，http的get请求写法就是：
```http
http://127.0.0.1:8000/identity/add_admin?a_id=admin&a_pw=123456
```
意思是添加了一个id为admin，密码为123456的管理员。发送请求后可以根据收到的json信息或者直接查看数据库信息判断是否成功。其他的功能测试方法可以以此类推。注意我用了md5保存密码，因此在数据库里看到的不是明文。

如果配环境的时候遇到问题随时问我！
