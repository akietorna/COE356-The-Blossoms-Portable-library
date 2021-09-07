from flask import Flask, render_template, request, url_for, redirect, flash, session, g, send_from_directory, abort, jsonify
from database import connection
#from wtforms import Form, BooleanField, TextField, PasswordField, validators
from flask_bcrypt import Bcrypt
from MySQLdb import escape_string as thwart
import gc
from time import localtime, strftime
from datetime import datetime
import os
import smtplib
import ssl
from email.mime.text import MIMEText
import random


# initializing the app and other parameters
app = Flask(__name__)
app.config['SECRET_KEY'] = "theblossoms123@"
app.config['DEBUG'] = True

# takes care of encrypting
bcrypt = Bcrypt()

# this  function sends a confirmatory code to the user


@app.route("/confirm_email/", methods=['GET', 'POST'])
def confirm_email():
    port = 465
    smtp_server = "smtp.gmail.com"

    sender_email = "pentecostalrevivalcenterag@gmail.com"
    receiver_email = str(session["email"])
    name = session['lastname']
    password = "revmoses1954"

    confirmation_code = ""
    for a in range(0, 7):
        confirmation_code += str(random.randint(0, 9))

    msg = MIMEText(" Hello " + name + " ! \n \n You signed up an account on the Portable library .To confirm that it was really you, please enter the confirmatory code  into the box provided. Thank you \n \n \t \t Confirmatory Code: " +
                   confirmation_code + "\n \n  But if it was not you can ignore this mail sent to you ")
    msg['Subject'] = 'Portable library email confirmation'
    msg['From'] = 'pentecostalrevivalcenterag@gmail.com'
    msg['To'] = session["email"]

    session["conf"] = confirmation_code

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(stmp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Mail sent')

    return redirect(url_for('confirm_coded'))


@app.route("/confirm_coded/", methods=["POST", "GET"])
def confirm_coded():
    info = {}
    if request.method == "POST":

        confirm_code = request_data["confirm_code"]
        conf = session["conf"]
        # inserting statements into the database
        if confirmed_code == conf:
            firstname = session["firstname"]
            lastname = session["lastname"]
            username = session["username"]
            email = session["email"]
            password = session["password"]

            curs, connect = connection()

            # inserting statements into the database
            input_statement = (
                "INSERT INTO users (firstname,lastname,username, email, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
            data = (thwart(firstname), thwart(lastname), thwart(
                username), thwart(email), thwart(password))
            curs.execute(input_statement, data)

            connect.commit()
            curs.close()
            connect.close()
            gc.collect()
            session['logged_in'] = True
            info['status'] = 'You are successfully logged in'

            jsonify(info)

            return url_for("select_program")

        else:
            info['status'] = 'Error logging in'
            return jsonify(info)


@app.route('/sign_up_page/', methods=["GET", "POST"])
def sign_up():
    info = {}
    if request.method == 'POST':

        session["firstname"] = request.form["firstname"]
        session["lastname"] = request.form["lastname"]
        session["username"] = request.form["username"]
        session["email"] = request.form["email"]

        bcrypt = Bcrypt()
        session["password"] = bcrypt.generate_password_hash(
            request.form["password"])

        curs, connect = connection()

        # checking if the username matches that of another person

        check_name = curs.execute(
            "SELECT * FROM users WHERE email = %s ", [session["email"]])

        if int(check_name) > 0:
            info['status'] = 'Email already exist'
            return jsonify(info)

        else:
            return redirect(url_for("confirm_email"))

    return render_template('sign_up_page.html')


@app.route("/forget_password/", methods=["POST", "GET"])
def forget_password():
    information = {}
    if request.method == "POST":
        email = request.form['email']

        curs, connect = connection()

        check_account = curs.execute(
            "select * from users where email = %s ", email)

        if len(check_account) > 0:

            # sending the code to the eamil
            port = 465
            stmp_server = "smtp.gmail.com"

            sender_email = "pentecostalrevivalcenterag@gmail.com"
            receiver_email = email
            name = username
            password = "revmoses1954"

            confirmation_code = ""
            for a in range(0, 7):
                confirmation_code += str(random.randint(0, 9))

            msg = MIMEText(" Hello! \n \n You requested for a reset of password on the Pentecostal Revival center,AG website.To confirm that it was really you, please enter the confirmatory code  into the box providedonthe website. Thank you \n \n \t \t Confirmatory Code: " +
                           confirmation_code + "\n \n  But if it was not you can ignore this mail sent to you ")
            msg['Subject'] = 'Portable library email confirmation'
            msg['From'] = 'pentecostalrevivalcenterag@gmail.com'
            msg['To'] = email

            session["conf"] = confirmation_code

            print(confirmation_code)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL(stmp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                print('Mail sent')

            return redirect(url_for('confirm_reset'))

        else:
            information['error'] = 'No account connected to this email'
            return jsonify(information)

    else:
        return redirect(url_for('forget_password'))


@app.route('/confirm_reset/', methods=["GET", "POST"])
def confirm_reset():
    info = {}
    if request.method == "POST":
        confirmed_code = request.form['confirm_code']
        conf = session["conf"]
        if conf == confirmed_code:
            return redirect(url_for('set_password'))

        else:
            info['status'] = 'You typed the wrong confirmatory code'
            return jsonify(info)
    return jsonify('i')


@app.route('/set_password/', methods=["GET", "POST"])
def set_password():
    info = {}
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password == confirm_password:
            password = bcrypt.generate_password_hash(password)
            curs, connect = connection()
            curs.execute("update users set password = (%s)  WHERE username = (%s)", [
                         password, username])
            info['status'] = 'Password sucessfully resetted'
            connect.commit()
            curs.close()
            connect.close()
            gc.collect()
            return jsonify(info)

        else:
            info['status'] = 'Error resetting password'
            return jsonify(info)


@app.route('/', methods=["GET", "POST"])
def home_page():
    d = {}
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        curs, connect = connection()
        info = curs.execute("SELECT * FROM users WHERE email = %s", [email])

        # fetching the password
        curs.execute("SELECT password FROM users WHERE email = %s", [email])
        Passwd = curs.fetchone()[0]
        curs.close()
        connect.close()

        if info == 1 and bcrypt.check_password_hash(Passwd, password) == True:
            session['logged_in'] = True
            d["status"] = "Log in succesfully"
            return jsonify(d)

        else:
            d['status'] = "Invalid credentials, try again"
            return jsonify(d)
    return jsonify('its working')


@app.route('/get_slides/', methods=["GET", "POST"])
def getslides():
    d = {}
    try:
        curs, connect = connection()
        curs.execute(
            "SELECT * from slides")
        data = curs.fetchall()

        return jsonify(data)

    except Exception as e:
        d['status'] = 'Error getting courses'
        return jsonify(d)


@app.route('/get_books/', methods=["GET", "POST"])
def getbooks():
    d = {}
    try:
        curs, connect = connection()
        curs.execute(
            "SELECT * from books")
        data = curs.fetchall()

        return jsonify(data)

    except Exception as e:
        d['status'] = 'Error getting courses'
        return jsonify(d)


@app.route('/get_courses/', methods=["GET", "POST"])
def getcourses():
    d = {}
    try:
        curs, connect = connection()
        curs.execute(
            "SELECT * from courses")
        data = curs.fetchall()

        return jsonify(data)

    except Exception as e:
        d['status'] = 'Error getting courses'
        return jsonify(d)


# @app.route('/get_courses/', methods=["GET", "POST"])
# def getcourses():
#     d = {}

#     if request.method == 'POST':
#         course_code = request.args.id
#         curs, connect = connection()
#         curs.execute(
#             "SELECT * from slides where course_code = %s", [course_code])
#         data = curs.fetchall()

#         return jsonify(data)
#     else:
#         d['status'] = 'Error getting courses'
#         return jsonify(d)


@app.route('/get_preps/', methods=["GET", "POST"])
def getpreps():
    d = {}
    try:
        curs, connect = connection()
        curs.execute(
            "SELECT * from preps")
        data = curs.fetchall()

        return jsonify(data)

    except Exception as e:
        d['status'] = 'Error getting courses'
        return jsonify(d)


@app.route('/get_projects/', methods=["GET", "POST"])
def getprojects():
    d = {}
    try:
        curs, connect = connection()
        curs.execute(
            "SELECT * from project")
        data = curs.fetchall()

        return jsonify(data)

    except Exception as e:
        d['status'] = 'Error getting courses'
        return jsonify(d)


@app.route('/get_videos/', methods=["GET", "POST"])
def getvideos():
    d = {}
    if request.method == 'POST':
        course_id = request.args.id
        curs, connect = connection()
        curs.execute(
            "SELECT * from videos where")
        data = curs.fetchall()

        return jsonify(data)

    else:
        d['status'] = 'Error getting courses'
        return jsonify(d)


@app.route('/books/', methods=["GET", "POST"])
def slides():
    d = {}
    if request.method == 'POST':
        name = request.form['name']
        link = request.form['link']

        curs, connect = connection()
        input_statement = ("INSERT INTO slides(name,link) VALUES (%s,%s)")
        data = [name, link]
        curs.execute(input_statement, data)
        connect.commit()
        curs.close()
        connect.close()
        gc.collect()

        d['status'] = 'Post sucessfull'

        return jsonify(d)

    else:
        d['status'] = 'Error posting'
        return jsonify(d)


@app.route('/books/', methods=["GET", "POST"])
def books():
    d = {}
    if request.method == 'POST':
        link = request.form['link']
        name = request.form['name']
        ISBN = request.form['ISBN']
        author = request.form['author']
        publisher = request.form['publisher']

        curs, connect = connection()
        input_statement = (
            "INSERT INTO books(name,link,ISBN,author,publisher) VALUES (%s,%s,%s,%s,%s)")
        data = [name, link, ISBN, author, publisher]
        curs.execute(input_statement, data)
        connect.commit()
        curs.close()
        connect.close()
        gc.collect()

        d['status'] = 'Post sucessfull'

        return jsonify(d)

    else:
        d['status'] = 'Error posting'
        return jsonify(d)


@app.route('/courses/', methods=["GET", "POST"])
def courses():
    d = {}
    if request.method == 'POST':
        course_code = request.form['course_code']
        name = request.form['name']
        about = request.form['about']

        curs, connect = connection()
        input_statement = (
            "INSERT INTO courses(name,link,about) VALUES (%s,%s,%s)")
        data = [name, link, about]
        curs.execute(input_statement, data)
        connect.commit()
        curs.close()
        connect.close()
        gc.collect()

        d['status'] = 'Post sucessfull'

        return jsonify(d)

    else:
        d['status'] = 'Error posting'
        return jsonify(d)


@app.route('/preps/', methods=["GET", "POST"])
def preps():
    d = {}
    if request.method == 'POST':
        link = request.form['link']
        name = request.form['name']

        curs, connect = connection()
        input_statement = ("INSERT INTO preps(name,link) VALUES (%s,%s)")
        data = [name, link]
        curs.execute(input_statement, data)
        connect.commit()
        curs.close()
        connect.close()
        gc.collect()

        d['status'] = 'Post sucessfull'

        return jsonify(d)

    else:
        d['status'] = 'Error posting'
        return jsonify(d)


@app.route('/projects/', methods=["GET", "POST"])
def projects():
    d = {}
    if request.method == 'POST':
        link = request.form['link']
        name = request.form['name']

        curs, connect = connection()
        input_statement = ("INSERT INTO project(name,link) VALUES (%s,%s)")
        data = [name, link]
        curs.execute(input_statement, data)
        connect.commit()
        curs.close()
        connect.close()
        gc.collect()

        d['status'] = 'Post sucessfull'

        return jsonify(d)

    else:
        d['status'] = 'Error posting'
        return jsonify(d)


@app.route('/videos/', methods=["GET", "POST"])
def videos():
    d = {}
    if request.method == 'POST':
        link = request.form['link']
        name = request.form['name']
        creator = request.form['creator']

        curs, connect = connection()
        input_statement = (
            "INSERT INTO project(name,link,creator) VALUES (%s,%s,%s)")
        data = [name, link, creator]
        curs.execute(input_statement, data)
        connect.commit()
        curs.close()
        connect.close()
        gc.collect()

        d['status'] = 'Post sucessfull'

        return jsonify(d)

    else:
        d['status'] = 'Error posting'
        return jsonify(d)


@app.route('/download/', methods=["GET", "POST"])
# @login_required
def download():
    path = request.args.get('id')
    return send_file(path, as_attachment=True, name=session["logged_in"])


if __name__ == "__main__":
    app.run(debug=True)
