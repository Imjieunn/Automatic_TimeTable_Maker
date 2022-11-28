from flask import Flask, render_template, request, redirect, url_for
 
app = Flask(__name__)
 
#@app.route('/') # 기본적 page -> main page
#def main():
     # 원하는 파이썬 코드 작성 -> 해당 html로 변수 넘겨주기
#    return render_template("main.html")
 
 # @app.route('/login.html')
 # def login():
#    def main():
 #     return render_template("login.html")
 
# @app.route('/select')
# def select():
#     return render_template("select.html")
 
# @app.route('/subject.html')
# def subject():
#     return render_template("subject.html")
 
# @app.route('/result')
# def result():
#     val = request.form
#     print("val from html" + str(val))
#     # return render_template("result.html", result=val)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        testDict=request.form.to_dict(flat=True)
        for key, value in testDict.items():
            print(key,value)
        return(f'<h1>{testDict}</h1>')
    return render_template('prac.html')
 
if __name__ == '__main__':
     app.run(debug=True)
