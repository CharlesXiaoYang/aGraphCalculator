from flask import Flask, render_template, redirect, url_for
from flask import request, url_for, redirect, flash
from flask import Flask, render_template
from flask import url_for, escape

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        expr = request.form.get('expr')
        print(expr)
        if not expr:
            flash('Invalid input.')  # 显示错误提示
            return redirect(url_for('index'))  # 重定向回主页
    # TODO: 这里expr已经提取了用户输入，计算逻辑在这写。
    # call return x y
    return render_template('index.html', x=[1, 2, 3, 4], y=[5, 6, 7, 8])


if __name__ == '__main__':
    app.run()
