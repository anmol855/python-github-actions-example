from flask import Flask

app = Flask(__name__)
a=2
b=3
@app.route("/")
def index():
    return a+b 
@app.route("/sub")
def sub():
    return a-b
@app.route("/mul")
def mul():
    return a*b
@app.route("/power")
def power():
    return a**b
@app.route("/exp")
def exp():
    return a*b+a**b

#"Hello, world!"


if __name__ == "__main__":
    app.run()

#from flask import Flask

#app = Flask(__name__)

#@app.route("/")
#def index():
#    return "Hello, world!"


#if __name__ == "__main__":
#    app.run()

