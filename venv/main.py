from flask import Flask, render_template, request, jsonify
import pymysql
app = Flask(__name__)
db = pymysql.connect(host ='localhost', port=3306, user='root', passwd='', db='sjs_test', charset ="utf8")
cursor = db.cursor()

@app.route("/page", methods =["GET"])
def hello():
    return render_template("index.html")
