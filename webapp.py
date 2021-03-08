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
    if color =="" or free=="":
        return render_template('response.html', response = "Please fill out all required boxes")
    
    if birthday != "":
        month = birthday[5: 7]
        if month == "01":
            month = "Jan"
        elif month == "02":
            month = "Feb"
        elif month == "03":
            month = "Mar"
        elif month == "04":
            month = "Apr"
        elif month == "05":
            month = "May"
        elif month == "06":
            month = "Jun"
        elif month == "07":
            month = "Jul"
        elif month == "08":
            month = "Aug"
        elif month == "09":
            month = "Sep"
        elif month == "10":
            month = "Oct"
        elif month == "11":
            month = "Nov"
        else:
            month = "Dec"

    last = random.randrange(0, 2)
    if lname!="":
        if last == 0:
            lname = lname[0:2]
        else:
            lname = lname[0] + lname[-1]

    if birthday!="":
        birthday = birthday[2:4] + "_"
    
    volu = int(vol)-5
    if len(color)>volu:
        color = color[0:4]
        
    if len(free)>volu:
        free = free[0:4]

    reply = "Password: "
    thislist = []
    listvalues = random.randrange(0, 3)
    if listvalues == 0:
        thislist = [lname, birthday, color]
    elif listvalues == 1:
        thislist = [color, month, lname]
    elif listvalues == 2:
        thislist = [lname, free, birthday]
    
    random.shuffle(thislist)
    for x in thislist:
        reply += x
    
    alist = [free, color]
    randnumb = random.randrange(0,2)
    if lname == "" and birthday == "":
        if randnumb == 0:
            reply = "Password: " + alist[0] + alist[1]
        else:
            reply = "Password: " + alist[1] + alist[0]

    volum = int(vol)
    i = len(reply)-10
    number = 1
    while i < volum:
        number = random.randrange(0, 10)
        reply = reply + str(number)
        i+=1
    
    a = len(reply)-10
    if a>volum:
        reply=reply[0:18]
    
    reply = "test"
    
    return render_template('response.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
