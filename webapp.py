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

    #for optional/required boxes
    if color =="" or free=="":
        return render_template('response.html', response = "Please fill out all required boxes")
    
    #transforms birthday info into month name and also the last two digits of the year
    month = birthday[5: 7]
    if birthday != "":
        birthday = birthday[2:4] + "_"
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
        elif month == "12":
            month = "Dec"

    #Makes last name info into either first letter and last letter, or first two letters
    last = random.randrange(0, 2)
    if lname!="":
        if last == 0:
            lname = lname[0:2]
        else:
            lname = lname[0] + lname[-1]
    
    #if adjective/color/keyword length is bigger than password length, shorten it
    volu = int(vol)-5
    a = len(color)
    if a>volu:
        color = color[0:4]
        
    b = len(free)
    if b>volu:
        free = free[0:4]

    #randomizes what data will be included into the password
    reply = "Password: "
    thislist = []
    listvalues = random.randrange(0, 3)
    if listvalues == 0:
        thislist = [lname, birthday, color]
    elif listvalues == 1:
        thislist = [color, month, lname]
    elif listvalues == 2:
        thislist = [lname, free, birthday]
    
    #randomizes order of the data, and puts it into the reply
    random.shuffle(thislist)
    for x in thislist:
        reply += x
    
    #if only the required boxes are filled out, make a different randomized password using both of them
    alist = [free, color]
    randnumb = random.randrange(0,2)
    if lname == "" and birthday == "":
        if randnumb == 0:
            reply = "Password: " + alist[0] + alist[1]
        else:
            reply = "Password: " + alist[1] + alist[0]
    
    #used to add random numbers to the end of the password to match the correct length of it
    volum = int(vol)
    i = len(reply)-10
    number = 1
    while i < volum:
        number = random.randrange(1, 10)
        reply = reply + str(number)
        i+=1
    
    #used for a corner case in which a password of 8 length has a 1/3 chance of returning a 9 length password.
    a = len(reply)-10
    if a>volum:
        reply=reply[0:18]
    
    return render_template('response.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
