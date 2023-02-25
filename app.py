from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    return "machine learning project practice"


if __name__=="__main__":
    app.run(debug=True)