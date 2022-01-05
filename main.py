from flask import Flask
from flask import render_template, redirect, url_for, flash
import forms

app = Flask(__name__)
app.config.from_object('config.Config')

@app.route('/generator', methods=['GET'])
def generator_main_page():
    return render_template("main_system.html")

@app.route('/login', methods=["GET","POST"])
def login():

    #instancing a form
    form = forms.LoginForm()
    render_resource = None

    if form.validate_on_submit():
        from data import queries
        queries = queries.Queries()
        
        data = {
            'user_name': form.username.data,
            'password': form.password.data
        }

        if queries.verify_user(**data):
            render_resource = redirect(url_for('generator_main_page'))
        else:
            flash('¡Something was wrong, please try again!', 'error')
            render_resource = render_template("login.html", form=form)
    else:
        flash('¡Something was wrong, please try again!', 'error')
        render_resource = render_template("login.html", form=form)

    return render_resource




@app.route('/signin', methods=['GET', 'POST'])
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


    
if __name__ == "__main__":
    app.run(debug=True)