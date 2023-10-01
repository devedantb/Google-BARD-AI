from flask import Flask,render_template,request
from bardapi import Bard
import os
from dotenv import load_dotenv

load_dotenv()
def create_app():
    app = Flask(__name__)
    # def get_token():
    #     try:
    #         token = os.getenv("BARD_TOKEN")
    #         bard = Bard(token=token)
    #         return bard
    #     except:
    #         return ('We are facing some connectivity issues. Please try again after some time')
    # bard = get_token()
    token = os.getenv("BARD_TOKEN")
    bard = Bard(token=token)
    @app.route("/", methods=["GET", "POST"])
    def home():
        try:
            if request.method == "POST":
                question=request.form["question"]
                isResult=False
                if len(question)>0:
                    result=bard.get_answer(question)['content']
                    isResult=True
                else:
                    result='Ask me somthing'
                return render_template("home.html", result=result,isResult=isResult)
            else:
                return render_template("home.html")
        except:
            return 'We are facing some connectivity issues. Please try again after some time'
    return app
