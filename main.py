from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello:
  return(render_template("main.html", **templatedata)
  
if __name__ == "__main__":
  app.run(debug = True, host = '10.0.0.28', port = 70)
