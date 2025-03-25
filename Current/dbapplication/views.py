from flask import render_template, request
from models import Person, User
from flask_login import login_user, logout_user, current_user, login_required



def register_routes(app, db, bcrypt):
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        
        elif request.method == 'POST':
            pass
    
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        
        elif request.method == 'POST':
            pass
    
    
    @app.route('/logout')
    def logout():
        logout_user()
        return 'Success'