from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])

def index():

return(render_template("1st test.html"))

if __name__ == "__main__":

app.run()
