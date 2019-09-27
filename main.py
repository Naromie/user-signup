from flask import Flask,request, redirect,render_template

app = Flask(__name__)

title = "SignUp"
@app.route("/")
def index():
    title = "SignUp"
    return render_template('home.html', title = title)
# def check_char():

 
@app.route("/", methods=['POST'])  
def validate_signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    verify_password = request.form['verify_password']
    
    username_error = ''
    email_error = ''
    password_error = ''
    verify_password_error = ''

    #Username Validation

    if username == '':
        username_error ="Please Enter Username"
    if not username.isalnum():
       username_error = "The username cannot contain any special characters"
       
    
    elif len(username) < 3:
       username_error = "Your Username cannot be less that 3 characters"
    elif len(username) > 20:
       username_error = "Your Username cannot be more that 20 characters"
    elif ' ' in username:
        username_error = "Username cannot contain any space"
    #End Of  username Validation

    #Email Validation

    if email != '':
        if "@" not in email:
            email_error="Email Address must include @"
    
        
        elif "." not in email:
            email_error = "Email must include a Periode(.)"
        elif ' ' in email:
            email_error ="Email cannot include any space"

        
    #End of email validation

    #Password Validation
    if password == '':
       password_error ="Password must be entered"
    elif len(password) < 3:
        password_error ="Password cannot be less than 2 characters"
    elif len(password) > 20:
        password_error ="Password cannot be more than 20 characters"
    elif " " in password:
        password_error =" Password cannot contains any space"
    if not password_error:
        if verify_password =="":
            verify_password_error = "Please enter a password"
        elif verify_password != password:
            verify_password_error ="Password Does not match"

    if not username_error and not email_error and not password_error and not verify_password_error:
        return redirect('/success?username=' + username) 
    else:
        return render_template('home.html',title = title,username_error=username_error
                              ,email_error=email_error,password_error=password_error,
                              verify_password_error=verify_password_error)

@app.route('/success')
def success():
    username = request.args.get("username")
    return render_template('success.html', username=username)

if __name__ == "__main__":
    app.run(debug=True)