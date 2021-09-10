from flask import Flask, render_template, request, url_for, redirect, flash, session, g, send_from_directory, abort, jsonify
# from database import connection
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
from models.courses_model import *
from models.books_model import *
from models.books_courses import *
from models.programs_model import *
from models.videos_model import *
from models.users import *

bcrypt = Bcrypt()

user_details = {
    'first_name': '', 'last_name': '', 'user_name': '', 'email': '', 'password': '', 'confirm_code': ''
}


@app.route('/get_courses', methods=['GET'])
def get_Courses():
    return jsonify({'courses': Courses.get_all_courses()})


@app.route('/get_course_by_code', methods=['GET'])
def get_course_by_code():
    code = request.args.get("code")
    return_value = Courses.get_course(code)
    return jsonify(return_value)


@app.route('/add_course', methods=['POST'])
def add_course():
    '''Function to add new movie to our database'''
    request_data = request.get_json()  # getting data from client
    exists = Courses.get_course(_code=request_data['course_code'])
    print(exists)
    if len(exists) > 0:
        return 'already exists'
    Courses.add_course(request_data["name"], request_data["course_code"],
                       request_data["about"])
    response = Response("Course added", 201, mimetype='application/json')
    return response


@app.route('/update_course', methods=['PATCH'])
def update_course():
    '''Function to edit movie in our database using movie id'''
    request_data = request.get_json()
    exists = Courses.get_course(_code=request_data['course_code'])
    if exists == []:
        return 'course doesnt exist'
    Courses.update_course(
        request_data['course_code'], request_data['name'], request_data['about'])
    response = Response('Course updated', status=200,
                        mimetype='application/json')
    return response


@app.route('/remove_course', methods=['DELETE'])
def remove_course():
    '''Function to delete movie from our database'''
    code = request.args.get("code")
    exists = Courses.get_course(_code=code)
    if exists == []:
        return 'course doesnt exist'
    Courses.delete_course(code)
    response = Response("course Deleted", status=200,
                        mimetype='application/json')
    return response


@app.route('/get_books', methods=['GET'])
def get_Books():
    return jsonify({'books': Books.get_all_books()})


@app.route('/get_book_by_link', methods=['GET'])
def get_book_by_link():
    link = request.args.get("link")
    return_value = Books.get_book(link)
    return jsonify(return_value)


@app.route('/add_book', methods=['POST'])
def add_book():
    '''Function to add new movie to our database'''
    request_data = request.get_json()  # getting data from client
    exists = Books.get_book(_link=request_data['link'])
    print(exists)
    if len(exists) > 0:
        return 'already exists'
    Books.add_book(request_data["name"], request_data["link"])
    response = Response("Book added", 201, mimetype='application/json')
    return response


@app.route('/update_book', methods=['PATCH'])
def update_book():
    '''Function to edit movie in our database using movie id'''
    request_data = request.get_json()
    exists = Books.get_book(_link=request_data['link'])
    if exists == []:
        return 'Book doesnt exist'
    Books.update_book(request_data['link'], request_data['name'])
    response = Response('Book updated', status=200,
                        mimetype='application/json')
    return response


@app.route('/remove_book', methods=['DELETE'])
def remove_book():
    '''Function to delete movie from our database'''
    link = request.args.get("link")
    exists = Books.get_book(_link=link)
    if exists == []:
        return 'Book doesnt exist'
    Books.delete_book(link)
    response = Response("Book Deleted", status=200,
                        mimetype='application/json')
    return response


@app.route('/get_programs', methods=['GET'])
def get_programs():
    return jsonify({'programs': Programs.get_all_programs()})


@app.route('/get_program_by_name', methods=['GET'])
def get_program_by_name():
    name = request.args.get("name")
    return_value = Programs.get_program(name)
    return jsonify(return_value)


@app.route('/add_program', methods=['POST'])
def add_program():
    '''Function to add new movie to our database'''
    request_data = request.get_json()  # getting data from client
    exists = Programs.get_program(_name=request_data['name'])
    print(exists)
    if len(exists) > 0:
        return 'already exists'
    Programs.add_program(
        request_data["name"], request_data["about"], request_data['department'])
    response = Response("Program added", 201, mimetype='application/json')
    return response


@app.route('/update_program', methods=['PATCH'])
def update_program():
    '''Function to edit movie in our database using movie id'''
    request_data = request.get_json()
    exists = Programs.get_program(_name=request_data['name'])
    if exists == []:
        return 'Program doesnt exist'
    Programs.update_program(
        request_data['name'], request_data['about'], request_data['department'])
    response = Response('Program updated', status=200,
                        mimetype='application/json')
    return response


@app.route('/remove_program', methods=['DELETE'])
def remove_program():
    '''Function to delete movie from our database'''
    name = request.args.get("name")
    exists = Programs.get_program(_name=name)
    if exists == []:
        return 'program doesnt exist'
    Programs.delete_program(name)
    response = Response("Program Deleted", status=200,
                        mimetype='application/json')
    return response


@app.route('/get_videos', methods=['GET'])
def get_videos():
    return jsonify({'videos': Videos.get_all_videos()})


@app.route('/get_video_by_link', methods=['GET'])
def get_video_by_link():
    link = request.args.get("link")
    return_value = Videos.get_video(link)
    return jsonify(return_value)


@app.route('/add_video', methods=['POST'])
def add_video():
    '''Function to add new movie to our database'''
    request_data = request.get_json()  # getting data from client
    exists = Videos.get_video(_link=request_data['link'])
    print(exists)
    if len(exists) > 0:
        return 'already exists'
    Videos.add_video(request_data["name"], request_data['link'])
    response = Response("Video added", 201, mimetype='application/json')
    return response


@app.route('/update_video', methods=['PATCH'])
def update_video():
    '''Function to edit movie in our database using movie id'''
    request_data = request.get_json()
    exists = Videos.get_video(_link=request_data['link'])
    if exists == []:
        return 'Video doesnt exist'
    Videos.update_video(
        request_data['name'], request_data['link'], request_data['creator'])
    response = Response('Video updated', status=200,
                        mimetype='application/json')
    return response


@app.route('/remove_video', methods=['DELETE'])
def remove_video():
    '''Function to delete movie from our database'''
    link = request.args.get("link")
    exists = Videos.get_video(_link=link)
    if exists == []:
        return 'Video doesnt exist'
    Videos.delete_video(link)
    response = Response("Video Deleted", status=200,
                        mimetype='application/json')
    return response


@app.route('/sign_up', methods=["GET", "POST"])
def sign_up():
    info = {}
    if request.method == 'POST':

        request_data = request.get_json()
        user_details["first_name"] = request_data["first_name"]
        user_details["last_name"] = request_data["last_name"]
        user_details["user_name"] = request_data["user_name"]
        user_details["email"] = request_data["email"]

        user_details["password"] = bcrypt.generate_password_hash(
            request_data["password"])

        # checking if the username matches that of another person

        check_name = Users.get_user(_user_name=user_details['user_name'])

        if len(check_name) > 0:
            info['status'] = 'Email already exist'
            return jsonify(info)

        else:
            return redirect(url_for("confirm_email"))

    return jsonify('')


@app.route("/confirm_email", methods=['GET', 'POST'])
def confirm_email():
    port = 465
    smtp_server = "smtp.gmail.com"

    sender_email = "pentecostalrevivalcenterag@gmail.com"
    receiver_email = str(user_details["email"])
    name = user_details['last_name']
    password = "revmoses1954"

    confirmation_code = ""
    for a in range(0, 7):
        confirmation_code += str(random.randint(0, 9))

    print(confirmation_code)

    msg = MIMEText(" Hello " + name + " ! \n \n You signed up an account on the Portable library .To confirm that it was really you, please enter the confirmatory code  into the box provided. Thank you \n \n \t \t Confirmatory Code: " +
                   confirmation_code + "\n \n  But if it was not you can ignore this mail sent to you ")
    msg['Subject'] = 'Portable library email confirmation'
    msg['From'] = 'pentecostalrevivalcenterag@gmail.com'
    msg['To'] = user_details["email"]

    user_details["confirm_code"] = confirmation_code

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Mail sent')

    return redirect(url_for('sign_up_confirm_code'))


@app.route("/sign_up_confirm_code", methods=["POST", "GET"])
def sign_up_confirm_code():
    info = {}
    if request.method == "POST":

        request_data = request.get_json()
        confirm_code = request_data["confirm_code"]
        conf = user_details["confirm_code"]

        if confirmed_code == conf:

            # inserting statements into the database

            Users.update_user(user_details['first_name'], user_details['last_name'],
                              user_details['user_name'], user_details['email'], user_details['password'])
            response = Response('Sign up successfull',
                                status=201, mimetype='application/json')

            return url_for("get_program"), response

        else:
            info['status'] = 'Error signing up'
            return jsonify(info)
    return jsonify('')


@app.route('/', methods=["GET", "POST"])
def sign_in():
    d = {}
    if request.method == 'POST':

        request_data = request.get_json()
        user_name = request_data['user_name']
        password = request_data['password']

        check_user = Users.get_user(user_name)

        print(check_user)

        if check_user == 1 and bcrypt.check_password_hash(check_password[4], password) == True:
            d["status"] = "Log in succesfully"
            return redirect(url_for('get_programs')), jsonify(d)

        else:
            d['status'] = "Invalid credentials, try again"
            return jsonify(d)

    return jsonify('')


@app.route("/forget_password", methods=["POST", "GET"])
def forget_password():
    information = {}
    if request.method == "POST":

        request_data = request.get_json()
        user_name = request_data['user_name']

        check_account = Users.get_user(user_name)

        check_account = check_account['email']

        if len(check_account) > 0:

            # sending the code to the eamil
            port = 465
            stmp_server = "smtp.gmail.com"

            sender_email = "pentecostalrevivalcenterag@gmail.com"
            receiver_email = check_account
            name = user_name
            password = "revmoses1954"

            confirmation_code = ""
            for a in range(0, 7):
                confirmation_code += str(random.randint(0, 9))

            msg = MIMEText(" Hello! \n \n You requested for a reset of password on the Pentecostal Revival center,AG website.To confirm that it was really you, please enter the confirmatory code  into the box providedonthe website. Thank you \n \n \t \t Confirmatory Code: " +
                           confirmation_code + "\n \n  But if it was not you can ignore this mail sent to you ")
            msg['Subject'] = 'Portable library email confirmation'
            msg['From'] = 'pentecostalrevivalcenterag@gmail.com'
            msg['To'] = check_account

            user_details["confirm_code"] = confirmation_code

            print(confirmation_code)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL(stmp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                print('Mail sent')

            return redirect(url_for('confirm_user_email'))

        else:
            information['error'] = 'No account connected to this email'
            return jsonify(information)

    else:
        return redirect(url_for('forget_password'))


@app.route('/confirm_user_email', methods=["GET", "POST"])
def confirm_user_email():
    info = {}
    if request.method == "POST":
        request_data = request.get_json()
        confirmed_code = request_data['confirm_code']
        confirm_code = user_details["confirm_code"]

        if confirm_code == confirmed_code:
            return redirect(url_for('set_password'))

        else:
            info['status'] = 'You typed the wrong confirmatory code'
            return jsonify(info), redirect(url_for('confirm_user_email'))

    return jsonify('')


@app.route('/set_password', methods=["GET", "POST"])
def set_password():
    info = {}
    if request.method == 'POST':

        request_data = request.get_json()
        username = request_data['username']
        password = request_data['password']
        password = bcrypt.generate_password_hash(password)

        Users.reset_password(username, password)

        response = Response('Password resetted', status=200,
                            mimetype='application/json')
        return response
    return jsonify()


@app.route('/get_users', methods=['GET', "POST"])
def get_users():
    return jsonify({'Users': Users.get_all_users()})


@app.route('/get_users_by_name', methods=['GET'])
def get_users_by_name():
    name = request.args.get("user_name")
    return_value = Users.get_user(name)
    return jsonify(return_value)


@app.route('/add_user', methods=['POST', "GET"])
def add_user():
    '''Function to add new user to our database'''

    if request.method == "POST":
        request_data = request.get_json()  # getting data from client

        first_name = request_data['first_name']
        last_name = request_data['last_name']
        user_name = request_data['user_name']
        email = request_data['email']
        password = bcrypt.generate_password_hash(request_data['password'])

        exists = Users.get_user(user_name)
        print(exists)
        if len(exists) > 0:
            return jsonify('user_name already exists')
        Users.add_user(first_name, last_name, user_name, email, password)
        response = Response("User added", 201, mimetype='application/json')
        return response
    return jsonify('')


@app.route('/update_user', methods=['PATCH'])
def update_user():
    '''Function to edit users in our database using movie id'''

    if request.method == "POST":
        request_data = request.get_json()  # getting data from client

        first_name = request_data['first_name']
        last_name = request_data['last_name']
        user_name = request_data['user_name']
        email = request_data['email']
        password = bcrypt.generate_password_hash(request_data['password'])

        exists = Users.get_user(user_name)
        if exists == []:
            return 'User does not exist'

        Programs.add_user(first_name, last_name, user_name, email, password)
        response = Response("User added", 201, mimetype='application/json')
        return response
    return jsonify('')


@app.route('/remove_user', methods=['DELETE'])
def remove_user():
    '''Function to delete user from our database'''
    name = request.args.get("name")
    exists = Users.get_user(_name=name)
    if exists == []:
        return 'User does not exist'
    Programs.delete_program(name)
    response = Response("User Deleted", status=200,
                        mimetype='application/json')
    return response


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == "__main__":
    app.run(port=1234, debug=True)
