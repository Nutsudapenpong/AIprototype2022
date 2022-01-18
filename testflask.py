from flask import Flask, request, render_template
import json
app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello, World!"

@app.route("/name")
def hellofair():
        return "Hello, Fair!"
##API
@app.route('/request',methods=['POST'])
def request_detail():
    payload = request.data.decode("utf-8")
    inmessage = json.loads(payload)

    print(inmessage)
    
    json_data = json.dumps({'y': 'received!'})
    return json_data

##webapp 
@app.route("/home")
def home():
    return render_template("home.html",name = 'Fair')

def hellofair():
            return "Hello, Fair!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')#host='0.0.0.0'