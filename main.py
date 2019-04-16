from flask import Flask, request,render_template, redirect
import cgi
import os

app=Flask (__name__)
app.config['DEBUG']=True

@app.route('/user-signup')
def index():
    return render_template('user_signup_form.html', title="User-Signup")

 

@app.route('/user-signup', methods=['POST'])
def user_signup():
    username=request.form['username']
    password=request.form['password']
    val_password=request.form['val_password']
    email=request.form['email']

    username_error=''
    password_error=''
    val_password_error=''
    email_error=''

    if not username:
        username_error='Not a valid username'
        username=''
    else:
        username=str(username)
        if len(username) > 20 or len(username) <3:
            username_error='Not a valid username. Username must be between 3 and 20 characters'
        if ' ' in username:
            username_error='Not a valid username. No spaces allowed'     

    if not password:
        password_error = "Password is required"
        password=''
    else:
        password=str(password)
    
        if len(password) > 20 or len(password) < 3:
            password_error='Not a valid password. Password must be between 3 and 20 character. Do not use any spaces' 
        if ' ' in password:
            password_error="Not a valid password. No spaces allowed"    
 
    if password != val_password:
        val_password_error='Passwords do not match'
        val_password=''        

    if email:
        email=str(email)
        if len(email) >20 or len(email) <3:
            email_error='Not a valid email'
        elif ' ' in email:
            email_error="Not a valid email. No spaces allowed"
        elif email.count('@') != 1 or email.count('.') != 1:
            email_error='Not a valid email. Only 1 @ and . may exist'
    

    if not username_error and not password_error and not val_password_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))

    else:
        return render_template('user_signup_form.html', username=username, password='', val_password='', email=email, 
        username_error=username_error, 
        password_error=password_error,
        val_password_error=val_password_error,
        email_error=email_error)    

@app.route('/welcome')
def welcome():
    user_name=request.args.get('username')
    return '<h1>Welcome, {0}!</h1>'.format(user_name)        
                
    


app.run()