from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資管二B 410917465 吳子翟 網頁</h1>"
    homepage += "<a href=/about>mis工作</a><br>"
    return homepage

@app.route("/about")
def about():
    return render_template("dill.html") 

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>" 
    
@app.route("/current")
def current():
    now = datetime.now()
    return render_template("current.html", datetime = str(now)) 

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)  

@app.route("/hi")
def hi():
    # 載入原始檔案
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # 計數加1
    count += 1

    # 覆寫檔案
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()
    return "本網站總拜訪人次：" + str(count)

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return "您輸入的名字為：" + user 
    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.run()