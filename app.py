from flask import Flask, render_template, request, redirect, url_for, jsonify,json
from werkzeug.utils import secure_filename
import requests,response
import os

app = Flask(__name__)

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    return render_template('login.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/login', methods=['POST'])
def LoginSubmit():
    Username = request.form['username']
    pword =request.form['password']

    # response = client.admin_initiate_auth(
    #     UserPoolId='us-east-1_8wVT5mhbD',
    #     ClientId='4irr8hou82ha4lpuvfole30b3t',
    #     AuthFlow='USER_SRP_AUTH' | 'REFRESH_TOKEN_AUTH' | 'REFRESH_TOKEN' | 'CUSTOM_AUTH' | 'ADMIN_NO_SRP_AUTH' | 'USER_PASSWORD_AUTH' | 'ADMIN_USER_PASSWORD_AUTH',
    #     AuthParameters={
    #         'string': 'string'
    #     },
    #     ClientMetadata={
    #         'string': 'string'
    #     },
    #     AnalyticsMetadata={
    #         'AnalyticsEndpointId': 'string'
    #     },
    #     ContextData={
    #         'IpAddress': 'string',
    #         'ServerName': 'string',
    #         'ServerPath': 'string',
    #         'HttpHeaders': [
    #             {
    #                 'headerName': 'string',
    #                 'headerValue': 'string'
    #             },
    #         ],
    #         'EncodedData': 'string'
    #     }
    # )
    url = "https://1dww0e3e4m.execute-api.us-east-1.amazonaws.com/Prod/getlogin/profilegetlogin?EmailID=" + Username + ""
    payload = {}
    headers = {}
    print("the data" + Username + "the data")
    response = requests.request("GET", url, headers=headers, data=payload)
    newdata = response.text
    newdata=newdata.replace('"', '')

    print("print data items is"+newdata+"the return password isssss"+pword)
    if newdata == pword :
      print("this is the matching strings")
      return render_template('dashboard.html')
    else:
      print("this is not matching strings")
      return render_template('login.html')



@app.route("/getTrendingDatas", methods=["GET"])
def getTrendingDatas():

    print("this is page used to get data items....")
    url = "https://api.twitter.com/1.1/trends/place.json?id=23424848"
    payload = {}
    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAAJFCgEAAAAAa7FQmixNzSu5lZkIkqBsav7jXpI%3DQRdTBvjL4Y1xNJmigaOgWOsvIfQrDJ2iO8PSfzQniAl9JJr9qJ'
    }
    response = requests.request("GET", url, headers=headers, data=payload)


    tuples=[]
    newdata=response.text
    print(newdata)
    return newdata


@app.route('/postcontent', methods=['POST'])
def imageUploading():
    print("the is posting content and file method here")
    datas = request.get_json()
    filename = datas['contentfile']
    postdata = datas['postcontent']
    print(filename)

    url = "https://1dww0e3e4m.execute-api.us-east-1.amazonaws.com/UploadFile/uploadingfile?fileName=" + filename + "&fileContnet=" + postdata + ""

    payload = "<file contents here>"
    headers = {
        'Content-Type': 'image/png',
        'Content-Type': 'image/gif',
        'Content-Type': 'image/jpeg'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))

    return 'empty data'


if __name__ == '__main__':
    app.run()
