import OS 
from flask import Flask
app = flask(_name_)

@app.route("/")
def main():
     return "Welcome!"

@app.route('/how are you')
def hello():
     return 'I am good. How about you ?'

if _name_ == "_main_":
   app.run()
