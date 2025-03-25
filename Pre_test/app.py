from flask import Flask, request, render_template, redirect, url_for, session, make_response


app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.secret_key = 'Some-Key'


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        names = ['John doe', 'Jane doe', 'John wick']
        return render_template('index.html', names=names)
    
    username = request.form.get('username') if request.form.get('username') else None
    password = request.form.get('password') if request.form.get('password') else None
    result = f"Username: {username}\nPassword: {password}"
    
    return result


@app.route("/other")
def other():
    some_text = 'Hello world'
    return render_template('other.html', item=some_text)


@app.template_filter('reverse_str')
def reverse_str(t):
    return t[::-1]

@app.template_filter('alternate_case')
def alternate_case(t):
    return t.upper()




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




@app.route('/redirect_endpoint')
def redirect_to_other():
    return redirect(url_for('other'))




@app.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files['file']
    
    if file.content_type == 'text/plain':
        return file.read().decode()
    
    
    
    
@app.route('/set_data')
def set_data():
    session['name'] = 'John'
    session['other'] = 'Hello world!'
    session['age'] = '2007-05-19'
    
    return render_template('index.html', message = 'Session data set.')


@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys() and 'age' in session.keys():
        name = session['name']
        other = session['other']
        age = session['age']
        
        return render_template('index.html', message=f'Name: {name}, Other: {other}, Age: {age}')

    else:
        return render_template('index.html', message='No sessions found!')
    


@app.route('/clear_session')
def clear_session():
    session.clear()
    
    return render_template('index.html', message='The session data has been deleting!')


@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index.html', message='Cookie set.'))
    response.set_cookie('cookie_name', 'cookie_value')
    
    return response


@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies['cookie_name']
    
    return render_template('index.html', message=f'Cookie value: {cookie_value}')



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8000)