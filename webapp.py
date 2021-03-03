from flask import Flask, url_for, render_template, request
import random

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    lname = request.args['lname']
    birthday = request.args['birthday']
    color = request.args['color'] 
    free = request.args['free']
    vol = request.args['vol']
    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue
    reply = lname + birthday + color + free + vol
    
    return render_template('response.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
