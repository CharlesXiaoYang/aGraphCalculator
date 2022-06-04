from flask import request, url_for, redirect, flash
from flask import Flask, render_template
from flask import url_for, escape
from math import *
app = Flask(__name__)
list = eval('dir()')

def pre_start():
    n = len(list)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if len(list[j]) < len(list[j + 1]) :
                list[j], list[j + 1] = list[j + 1], list[j]

pre_start()


@app.route('/', methods=['GET', 'POST'])
def index():
    xs = []
    ys = []
    if request.method == 'POST':
        expr = request.form.get('expr')
        #print(expr)
        if not expr:
            flash('Invalid input.')  # 显示错误提示
            return redirect(url_for('index'))  # 重定向回主页
    #TODO: 这里expr已经提取了用户输入，计算逻辑在这写。
    #call return x y
        expr1 = "" + expr
        
        for each in list:
            index = expr1.find(each)
            while index != -1:
                expr1 = expr1[0 : index] + " " * len(each) + expr1[index + len(each) :]
                index = expr1.find(each)
        found = False
        location =[]
        print(expr1)
        for index in range(len(expr1)):
            char = expr1[index]
            if found == False:
                if (char > 'A' and char < 'Z') or (char > 'a' and char < 'z'):
                    var = char
                    found = True
                    location.append(index)
            else:
                if (char > 'A' and char < 'Z') or (char > 'a' and char < 'z'):
                    if var == char:
                        location.append(index)
        last = 0
        expr2 = ''
        for each in location:
            if each == 0:
                expr2 = "number"
                last = 1
            else:
                expr2 = expr2 + expr[last:each] + "number"
                last = each + 1
        expr2 += expr[last:]
        
        for i in range(20001):
            number = -1000 + i * 0.1
            y = eval(expr2)
            xs.append(number)
            ys.append(y)
    return render_template('index.html', x= xs, y = ys)

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)

@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
    print(url_for('hello'))  # 输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'


if __name__ == '__main__':
    app.run()
