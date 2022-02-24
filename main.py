from flask import Flask
from flask import render_template, redirect, url_for, flash, session, request
import json
import forms

app = Flask(__name__)
app.config.from_object('config.Config')

@app.route('/login', methods=["GET","POST"])
def login():

    #instancing a form
    form = forms.LoginForm()
    render_resource = None
    session.pop('user_name', None)

    if form.validate_on_submit():
        from data import queries
        queries = queries.Queries()
    
        data = {
            'user_name': form.username.data,
            'password': form.password.data
        }

        if queries.verify_user(**data):
            session['user_name'] = data['user_name']

            render_resource = redirect(url_for('generate_password'))
        else:
            flash('¡Something was wrong, please try again!', 'error')
            render_resource = redirect(url_for('login'))
    else:
        session.pop('user_name', None)
        render_resource = render_template('login.html', form=form)

    return render_resource

@app.route('/generator', methods=['GET'])
def generator_main_page():
    if 'user_name' in session:
        return render_template("main_system.html")
    else:
        return redirect(url_for('login'))


@app.route('/signin', methods=['GET','POST'])
def create_account():
    
    form = forms.CreateAccount()
    render_resource = None

    if form.validate_on_submit():
        render_resource = redirect(url_for('login'))
        
        from data import queries
        queries = queries.Queries()
        data = {
            'name': form.name.data,
            'surnames': form.surnames.data,
            'age': form.age.data,
            'email': form.email.data,
            'password': form.password.data,
            'user_name': form.user_name.data
        }

        if queries.insert_user(**data):
            flash('¡You have created an account succesfully!', 'success')
        else:
            flash('¡Something was wrong, please try again!', 'error')
            
    else:
        render_resource = render_template("signin.html", form=form)

    return render_resource

@app.route('/generate', methods=["GET","POST"])
def generate_password():
    form = forms.generateNewPassword()
    from logic.generate_password import PasswordGenerator
    from logic.RSA_password import RSAPassword
    resource = None

    if form.validate_on_submit():
        password_length = form.password_length.data
        numberCheck = bool(request.form.get('numberCheckBox'));
        lowerCheck = bool(request.form.get('lowerCheckBox'));
        upperCheck = bool(request.form.get('upperCheckBox'));
        punctCheck = bool(request.form.get('punctCheckBox'));
        generator = PasswordGenerator()
        password = generator.generate_password(password_length, numberCheck, lowerCheck, upperCheck, punctCheck)
        rsa = RSAPassword()
        data = {"password":password, "password_encrypted":rsa.encrypt(password)}

        
        resource = render_template('generate_password_page.html', form=form, data=data)
    else:
        resource = render_template('generate_password_page.html', form=form)

    return resource

if __name__ == "__main__":
    app.run(debug=True)