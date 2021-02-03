# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


# 路由解析，通过访问路径，匹配相应的函数
# @app.route('/') # 路由解析
# def hello_world():
#     return '你好，世界 '

# 路由解析,当请求路径是/index时执行index函数
@app.route('/index')
def index():
    return "主页"


# 通过访问路径，获取用户字符串参数，<>种的名字需和变量名一样
@app.route('/user/<name>')
def welcome(name):
    return "你好,%s" % name


# 通过访问路径，获取用户整型参数 此外也可以获取flot参数
@app.route('/user/<int:id>')
def welcome2(id):
    return "你好,%d" % id + "号会员"


# 返回用户渲染后的网页
# @app.route('/')
# def index2():
#     return render_template("index.html")


# 向页面传递变量
# 返回用户渲染后的网页
@app.route('/')
def index2():
    local_time = datetime.date.today()  # 普通变量
    name = ['小张', '小王', '小钟']
    task = {"任务": "打扫卫生", "时间": "3小时"}
    return render_template("index.html", var=local_time, list=name, task=task)


@app.route('/test/register')
def register():
    return render_template("test/register.html")


@app.route('/result', methods=['GET', 'POST'])
def result():
    print(request.method)
    if request.method == "POST":
        res = request.form
        print(res)
        return render_template("test/result.html", res=res)
    else:
        print('erro')
        return "erro"


'''
flask主要提供两个功能一个是路由功能，另一个是模板渲染功能
路由:
app = Flask(__name__) 通过Fask实例化app对象
通过@app.route(’/‘)设置路由，其中有method参数可以设置请求方式，例如:@app.route('/',method=['post'])，详细见上方例子
可以同过app.route('/<name>') 可以同过再路由后面再加/<name> 的方式获取路径种的字符串等数据，详细见上方例子
模板渲染:
模板渲染通过flask种render_template模块来实现
如 return render_template('index.html') 注意:需要在当前目录下建立templates文件夹,flask会自动访问该文件并且寻找对应的html页面然后进行渲染
后台给前端的数据可以返回字符串，列表和字典
例:
@app.route('/')
def index2():
    local_time = datetime.date.today()  # 普通变量
    name = ['小张', '小王', '小钟']
    task = {"任务": "打扫卫生", "时间": "3小时"}
    return render_template("index.html", var=local_time, list=name, task=task)
    
其中var,list,task等参数名是提供给前端的名字，前端需要访问数据时通过该名字访问，local_time,name,task等是变量，后端用数据名
在html页面种通过{{data}} （注：data是后台传的数据）的方式获取后台发送的数据

通过{%for i in range(1)%}
    {{i}}
   {% endor%}
的方式在html页面进行控制语句输出，如 for，if等语句

在html页面中表单中<form action={{url_for('result')}} method="post"> 可以通过{{url_for（'路由名字'）}}的方式来自动定位路由，不要用死
路径

'''

if __name__ == '__main__':
    app.run()
