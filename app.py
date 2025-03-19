from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World</h1>"


@app.route("/greet")
def greeting():
    return "<h3>Welcome to our python commiunity.</h3>"


@app.route("/greet/<name>")
def greet_user(name):
    return "<h3>Welcome to our python commiunity %s.</h3>" %name



@app.route('/sum/<nums>')
def sum_numbers(nums):
    sum = 0
    for i in nums:
        sum += int(i)
        
    return f'<h2>The sum of numbers is: {sum}</h2>'



@app.route("/handle_params", methods = ['GET', 'POST'])
def handle_url_params():
    if 'name' in request.args.keys() and 'password' in request.args.keys():
        name = request.args.get('name')
        password = request.args.get('password')
    
    else:
        if request.method == 'GET':
            return f'Some parameters are missing with request method: {request.method}'
        if request.method == 'POST':
            return f'Some parameters are missing with request method: {request.method}'
    
    return f'Name: ({name})<br>Password: ({password})<br> With request method: {request.method}'




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8888)