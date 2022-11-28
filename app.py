from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/') # 기본적 page -> main page
def main():
    # 원하는 파이썬 코드 작성 -> 해당 html로 변수 넘겨주기
    return render_template("main.html")

# @app.route('/login.html')
# def login():
#     # id = request.args.get("id")
#     # pw = request.args.get("pw")
#     import crawling
#     return render_template("login.html")


@app.route('/select')
def select():
    return render_template("select.html")

# @app.route('/subject.html')
# def subject():
#     return render_template("subject.html")

@app.route('/result')
def result():
    name_list=[]
    time_list=[]
    num_list=[]
    subject_name = request.args.get("subject")
    name_list.append(subject_name)
    time = request.args.get("time")
    time_list.append(time)
    num = request.args.get("num")
    num_list.append(num)
    return render_template("result.html")

if __name__ == '__main__':
    app.run(debug=True)
