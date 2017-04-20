
from flask import Flask, render_template, request, redirect, \
jsonify, url_for, flash
# import httplib2
import json
from flask import make_response
import urllib.parse
import time

app = Flask(__name__)

APPLICATION_NAME = "MedReminder Application"

#Project Hash : 35aa3f03dceda115c9557a7fbd60aa8c646cd044a06b9baf3d5423bb1ede72ec
@app.route('/', methods=['GET','POST'])
def MedReminder():
    global request
    if request.method == 'POST':
        name = request.form['name']
        number = '91' #Only India Supported
        number += request.form['number']
        detail = request.form['detail']
        age = request.form['age']
        sender = 'MedReminder Team'
        print (name + number + detail)
        message = 'This is a reminder : ' + detail
        if number.isdigit() and len(number) == 12 and len(detail) > 5 and len(name) > 3 and int(age) > 0 and int(age) < 100:
            data =  urllib.parse.urlencode({'apiKey': 'ZywG5kFs3QA-LVrOpdG5pQCVC1qWQYPMEYnK0rk7Fs', 'numbers': number,
                'message' : message, 'sender': sender})
            data = data.encode('utf-8')
            request = urllib.request.Request("http://api.textlocal.in/send/?")
            f = urllib.request.urlopen(request, data)
            fr = f.read()
            print('yolo + \n')
            print (fr)
            return render_template('index.html', flash = 'Successfully Registered!', flashType = 'success')
        else :
            return render_template('index.html', flash = 'Incorrect Details. Please retry.', flashType = 'danger')
    else :
        return render_template('index.html', flash = None)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key_bro'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
