from flask import Flask,render_template,request,url_for,redirect,flash,session,g, send_from_directory, abort,jsonify
from database import connection
from wtforms import Form, BooleanField, TextField, PasswordField,validators
from flask_bcrypt import Bcrypt
from MySQLdb import escape_string as thwart
import gc
from time import localtime,strftime
from datetime import datetime
import os
import smtplib,ssl
from email.mime.text import MIMEText
import random


#initializing the app and other parameters
app = Flask(__name__)
app.config['SECRET_KEY'] = "theblossoms123@"
app.config['DEBUG'] = True

#takes care of encrypting
bcrypt = Bcrypt()


# building a user login required function 
def login_required(f):
    @wraps(f)
    def wrapping(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        
        else :
            flash('You need to login first')
            return redirect(url_for('home_page'))
        
    return wrapping



# this  function sends a confirmatory code to the user
@app.route("/confirm_email/", methods=['GET','POST'])
def confirm_email():
    port = 465
    smtp_server = "smtp.gmail.com"
    
    sender_email = "pentecostalrevivalcenterag@gmail.com"
    receiver_email = str(session["email"])
    name = session['lastname']
    password = "revmoses1954"

    confirmation_code = ""
    for a in range(0,7):
        confirmation_code += str(random.randint(0,9))

    

    msg = MIMEText(" Hello "+ name + " ! \n \n You signed up an account on the .To confirm that it was really you, please enter the confirmatory code  into the box provided. Thank you \n \n \t \t Confirmatory Code: "+ confirmation_code  +"\n \n  But if it was not you can ignore this mail sent to you ")
    msg['Subject'] = 'PRC AG website sign up email confirmation'
    msg['From'] = 'pentecostalrevivalcenterag@gmail.com'
    msg['To'] = session["email"]
    
    session["conf"] = confirmation_code

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(stmp_server,port,context = context) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,msg.as_string())
        print('Mail sent')

    return redirect(url_for('confirm_coded'))
    

@app.route("/confirm_coded/", methods=["POST", "GET"])
def confirm_coded():
    if request.method =="POST":

        request_data = request.get_json()

        confirm_code = request_data["confirm_code"]
        conf = session["conf"]
        # inserting statements into the database
        if confirmed_code == conf:
            firstname = session["firstname"]
            lastname=session["lastname"]          
            username=session["username"]
            email = session["email"]
            password = session["password"]

            curs,connect = connection()

             # inserting statements into the database
            input_statement = ("INSERT INTO users (firstname,lastname,username, email, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" ) 
            data = (thwart(firstname), thwart(lastname), thwart(username), thwart(email), thwart(password))
            curs.execute( input_statement, data)

            connect.commit()
            curs.close()
            connect.close()
            gc.collect()
            session['logged_in'] = True

            return url_for("select_program")

        else:
            error = "The confirmatory code was incorrect " 
            return 

    return jsonify()
    
@app.route("select_program", methods=['GET','POST'])
def select_program():
    return



@app.route('/sign_up_page/',methods=["GET","POST"])

def sign_up():

    if request.method =='POST':
        request_info = request.get_json()

        session["firstname"] = request_info["firstname"]
        session["lastname"] = request_info["lastname"]
        session["username"] = request_info["username"]
        session["email"] = request_info["email"]

        bcrypt = Bcrypt()
        session["password"] = bcrypt.generate_password_hash(request_info["password"])

        

            

        curs,connect = connection()

        # checking if the username matches that of another person
    

        check_name = curs.execute("SELECT * FROM users WHERE email = %s ", [session["email"]] )

        if int(check_name) > 0:
            flash("Email already used,please choose another one")
            return redirect(url_for('sign_up'))


        else:

            return redirect(url_for("confirm_email"))

    return jsonify()



@app.route("/forget_password/", methods=["POST", "GET"])
def forget_password():
    
    form = ForgetPassword(request.form)

    if request.method =="POST" :
        email = form.email.data

        # sending the code to the eamil
        port = 465
        stmp_server = "smtp.gmail.com"
        
        sender_email = "pentecostalrevivalcenterag@gmail.com"
        receiver_email = email
        name = username
        password = "revmoses1954"

        confirmation_code = ""
        for a in range(0,7):
            confirmation_code += str(random.randint(0,9))

        

        msg = MIMEText(" Hello! \n \n You requested for a reset of password on the Pentecostal Revival center,AG website.To confirm that it was really you, please enter the confirmatory code  into the box providedonthe website. Thank you \n \n \t \t Confirmatory Code: "+ confirmation_code  +"\n \n  But if it was not you can ignore this mail sent to you ")
        msg['Subject'] = 'PRC AG website sign up email confirmation'
        msg['From'] = 'pentecostalrevivalcenterag@gmail.com'
        msg['To'] =  email
        
        session["conf"] = confirmation_code

        print(confirmation_code)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(stmp_server,port,context = context) as server:
            server.login(sender_email,password)
            server.sendmail(sender_email,receiver_email,msg.as_string())
            print('Mail sent')


        return redirect(url_for('confirm_reset'))

    return render_template("forgetPassword.html", form=form)


@app.route('/confirm_reset/', methods=["GET","POST"])
def confirm_reset():
    form=ConfirmEmail(request.form)
    if request.method =="POST" and form.validate():
        confirmed_code = form.confirmation.data
        conf = session["conf"]
        if conf == confirmed_code:
            return redirect(url_for('set_password'))

        else:
            error = "Your credentials do not match, try again" 
            return redirect(url_for('home_page'))

    return render_template("confirm_email.html", form = form)




@app.route('/set_password/',methods=["GET","POST"])
def set_password():
    error = ''
    form = SetPassword(request.form)
    if request.method =='POST' :
        username = form.username.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        if password == confirm_password:

            password = bcrypt.generate_password_hash(password)

            curs, connect = connection()
            curs.execute("update users set password = (%s)  WHERE username = (%s)",[password,username])
            connect.commit()
            curs.close()
            connect.close()
            gc.collect()
            return "it worked"

        else:
            error = "Your credentials do not match, try again" 
            return render_template('reset_password.html', error = error)


    return render_template('reset_password.html', form=form)




@app.route('/',methods=["GET","POST"])
def home_page():
    error = ''
    form = LogIn(request.form)
    if request.method =='POST':
        username = form.username.data
        password = form.password.data

        curs, connect = connection()
        info = curs.execute("SELECT * FROM users WHERE username = %s", [username])

        # fetching the password

        curs.execute("SELECT password FROM users WHERE username = %s", [username])
        
        Passwd = curs.fetchone()[0]

        

        # checking if the password valid

        

        if info == 1 and bcrypt.check_password_hash(Passwd,password ) == True :
            session['logged_in'] = True
            session['username'] = request.form['username']
            update = request.form['username']
            # session['admin'] = True

            return "it worked"

        


        else:
            error = "Your credentials are invalid, try again" 
        curs.close()
        connect.close()
        gc.collect() 
        return render_template('login.html', error = error,form = form)

    return render_template('login.html', error = error, form = form)


@app.route('/get_comment/',methods=["GET","POST"])
@logged_in_required
def get_comment():
    error=''
    try:
        curs, connect = connection()
        curs.execute('SELECT * from comments')
        data = curs.fetchall()
        
        data = reversed(data)



        return jsonify()

    except Exception as e:
        return render_template('comments.html', name=session['admin'])


@app.route('/get_comment/',methods=["GET","POST"])
@logged_in_required
def get_comment():
    error=''
    try:
        curs, connect = connection()
        curs.execute('SELECT * from comments')
        data = curs.fetchall()
        
        data = reversed(data)

        return jsonify()

    except Exception as e:
        return render_template('comments.html', name=session['admin'])

@app.route('/comments/',methods=["GET","POST"])
@login_required
def comments():
    form = Comments(request.form)
    if request.method =='POST':
        sender_name = form.sender_name.data
        comments= form.comments.data
        contact = form.contact.data

        time_sent = datetime.now()

        curs,connect = connection()
                    
        input_statement = ("INSERT INTO comments(sender_name,time_sent,contact,comment) VALUES (%s,%s,%s,%s)" ) 
        data = [sender_name, time_sent,contact, comments]
        curs.execute( input_statement, data)

        connect.commit()
        print("The process was sucessful")
        curs.close()
        connect.close()
        gc.collect()

        return redirect(url_for('thank_you1'))

    return render_template("comments.html", form=form, name=session['logged_in'])


@app.route('/notes/',methods=["GET","POST"])
@logged_in_required
def notes():
    error=''
    try:
        curs, connect = connection()
        curs.execute('SELECT * FROM testimony')
        data = curs.fetchall()
        
        data = reversed(data)



        return jsonify()

    except Exception as e:
        return render_template('testimony1.html', name=session['admin'])



@app.route('/download/',methods=["GET","POST"])
@login_required
def download():
    path=request.args.get('id')
    return send_file(path,as_attachment=True, name=session["logged_in"])



if __name__== "__main__":
    app.run(debug=True)