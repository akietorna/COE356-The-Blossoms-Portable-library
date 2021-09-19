from flask import Flask, render_template, request, url_for, redirect, flash, session, g, send_from_directory, abort, jsonify, json
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

# from backend.blossoms1.models.books_courses import *
# from backend.blossoms1.models.preps_model import *
# from backend.blossoms1.models.programs_courses import *
# from backend.blossoms1.models.projects_model import *
# from backend.blossoms1.models.slides import *
# from backend.blossoms1.models.videos_courses import *


# initializing the app and other parameters
app = Flask(__name__)
app.config['SECRET_KEY'] = "theblossoms123@"
app.config['DEBUG'] = True

# takes care of encrypting
bcrypt = Bcrypt(app)

# this  function sends a confirmatory code to the user

userdetails = {'firstname': '', 'lastname': '', 'username': '',
               'email': '', 'password': '', 'confirm_code': ''}


@app.route('/courses', methods=['GET'])
def get_Courses():
    return jsonify({'courses': Courses.get_all_courses()})


@app.route('/course', methods=['GET'])
def get_course_by_code():
    code = request.args.get("code")
    return_value = Courses.get_course(code)
    return jsonify(return_value)


@app.route('/course', methods=['POST'])
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


@app.route('/course', methods=['PATCH'])
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


@app.route('/course', methods=['DELETE'])
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


@app.route('/books', methods=['GET'])
def get_Books():
    return jsonify({'books': Books.get_all_books()})


@app.route('/book', methods=['GET'])
def get_book_by_link():
    link = request.args.get("link")
    return_value = Books.get_book(link)
    return jsonify(return_value)


@app.route('/book', methods=['POST'])
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


@app.route('/book', methods=['PATCH'])
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


@app.route('/book', methods=['DELETE'])
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


@app.route('/programs', methods=['GET'])
def get_programs():
    return jsonify({'programs': Programs.get_all_programs()})


@app.route('/program', methods=['GET'])
def get_program_by_name():
    name = request.args.get("name")
    return_value = Programs.get_program(name)
    return jsonify(return_value)


@app.route('/program', methods=['POST'])
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


@app.route('/program', methods=['PATCH'])
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


@app.route('/program', methods=['DELETE'])
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


@app.route('/videos', methods=['GET'])
def get_videos():
    return jsonify({'videos': Videos.get_all_videos()})


@app.route('/video', methods=['GET'])
def get_video_by_link():
    link = request.args.get("link")
    return_value = Videos.get_video(link)
    return jsonify(return_value)


@app.route('/video', methods=['POST'])
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


@app.route('/video', methods=['PATCH'])
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


@app.route('/video', methods=['DELETE'])
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

# todo books_courses


@app.route('/books-courses', methods=['GET'])
def get_all_books_courses():
    return_value = Books_courses.get_all_books_courses()
    return jsonify({'books-courses': return_value})


@app.route('/book-course-rel', methods=['GET'])
def get_book_course_rel():
    '''Function to delete movie from our database'''
    link = request.args.get("link")
    code = request.args.get('course_code')

    results = Books_courses.get_book_course_rel(_course_code=code, _link=link)
    return jsonify({'Book-Course': results})


@app.route('/books-for-a-course', methods=['GET'])
def get_books_for_a_course():
    '''Function to edit movie in our database using movie id'''
    code = request.args.get("course_code")

    results = Books_courses.get_books_for_course(_course_code=code)
    return jsonify({'Books': results})


@app.route('/book-course', methods=['POST'])
def add_book_course():
    '''Function to add new movie to our database'''
    code = request.args.get("course_code")
    link = request.args.get("link")  # getting data from client

    results = Books_courses.add_book_course(_link=link, _course_code=code)

    response = Response(results, 200, mimetype='application/json')
    return response


@app.route('/book-course', methods=['PATCH'])
def update_book_course():
    '''Function to delete movie from our database'''
    try:
        link = request.args.get("link")
        code = request.args.get('course_code')
        new_link = request.args.get('new_link')
    except:
        pass
    if new_link == None:
        response = Response('Failed, provide new link',
                            400, mimetype='application/json')
        return response
    results = Books_courses.update_book_course(
        _link=link, _course_code=code, _new_link=new_link)
    return Response(results, 200, mimetype='application/jsosn')


@app.route('/book-course', methods=['DELETE'])
def delete_book_course():
    '''Function to delete movie from our database'''
    link = request.args.get("link")
    code = request.args.get('course_code')

    results = Books_courses.delete_book_course(_course_code=code, _link=link)
    response = Response(results, 200, mimetype='application/json')
    return response


# todo PREPS
@app.route('/preps', methods=['GET'])
def get_all_preps():
    return_value = Preps.get_all_preps()
    return jsonify({'Preps': return_value})


@app.route('/preps-for-course', methods=['GET'])
def get_all_preps_for_a_course():
    code = request.args.get('course_code')
    return_value = Preps.get_preps_for_course(_course_code=code)
    return jsonify({'Preps': return_value})


@app.route('/prep', methods=['GET'])
def get_specific_prep():
    link = request.args.get('link')
    return_value = Preps.get_prep(_link=link)
    return jsonify({'Prep': return_value})


@app.route('/prep', methods=['POST'])
def add_prep():
    name = request.args.get('name')
    link = request.args.get('link')
    code = request.args.get('course_code')
    return_value = Preps.add_prep(_course_code=code, _link=link, _name=name)
    return Response(return_value, 200, mimetype='application/json')


@app.route('/prep', methods=['PATCH'])
def update_prep():
    try:
        new_l = request.args.get('new_link')
        link = request.args.get('link')
        code = request.args.get('course_code')
    except:
        pass
    if new_l == None or link == None or code == None:
        return Response('Failed, the arguments cannot be nullable', 400, mimetype='application/json')
    return_value = Preps.update_prep(_new_link=new_l, _link=link, _code=code)
    return Response(return_value, 200, mimetype='application/json')


@app.route('/prep', methods=['DELETE'])
def delete_prep():
    link = request.args.get('link')
    return_value = Preps.delete_prep(_link=link)
    return Response(return_value, 200, mimetype='application/json')


# todo PROGRAMS_COURSES
@app.route('/programs-courses', methods=['GET'])
def get_all_programs_courses():
    return_value = Programs_courses.get_all_prog_courses()
    return jsonify({'Programs-Courses': return_value})


@app.route('/courses-for-program-for-sem', methods=['GET'])
def get_courses_for_program_for_sem():
    prog = request.args.get('program')
    sem = int(request.args.get('sem'))
    return_value = Programs_courses.get_courses_for_prog_for_sem(
        _prog=prog, _sem=sem)
    return jsonify({f'Courses': return_value})


@app.route('/program-course-sem-rel', methods=['GET'])
def get_a_program_course_rel():
    code = request.args.get('course_code')
    prog = request.args.get('program')
    sem = int(request.args.get('sem'))
    return_value = Programs_courses.get_prog_course_rel(
        _course_code=code, _prog=prog, _sem=sem)
    return jsonify({f'relation': return_value})


@app.route('/program-course', methods=['POST'])
def add_prog_course_rel():
    code = request.args.get('course_code')
    prog = request.args.get('program')
    sem = int(request.args.get('sem'))
    return_value = Programs_courses.add_program_course(
        _prog=prog, _course_code=code, _sem=sem)
    return Response(return_value, 200, mimetype='application/json')


@app.route('/program-course', methods=['PATCH'])
def update_prog_course_rel():
    code = request.args.get('course_code')
    prog = request.args.get('program')
    sem = int(request.args.get('sem'))
    new_code = request.args.get('new_code')
    new_sem = int(request.args.get('new_sem'))
    new_p = request.args.get('new_program')
    return_value = Programs_courses.update_prog_course(
        _prog=prog, _code=code, _sem=sem, _new_prog=new_p, _new_code=new_code, _new_sem=new_sem)
    return Response(return_value, 200, mimetype='application/json')


@app.route('/program-course', methods=['DELETE'])
def delete_prog_course_rel():
    code = request.args.get('course_code')
    prog = request.args.get('program')
    sem = int(request.args.get('sem'))
    return_value = Programs_courses.delete_prog_course(
        _prog=prog, _course=code, _sem=sem)
    return Response(return_value, 200, mimetype='application/json')


# todo PROJECTS
@app.route('/project', methods=['POST'])
def add_project():
    code = request.args.get('course_code')
    name = request.args.get('name')
    link = request.args.get('link')
    return_value = Projects.add_projects(
        _course_code=code, _name=name, _link=link)
    return Response(return_value, 200, mimetype='application/json')


@app.route('/projects', methods=['GET'])
def get_all_projects():
    return_value = Projects.get_all_projects()
    return jsonify({'Projects': return_value})


@app.route('/project', methods=['GET'])
def get_specific_project():
    link = request.args.get('link')
    return_value = Projects.get_project(_link=link)
    return jsonify({'Project': return_value})


@app.route('/projects-for-a-course', methods=['GET'])
def get_projects_for_a_course():
    code = request.args.get('course_code')
    return_value = Projects.get_projects_for_course(_course_code=code)
    return jsonify({f'Projects for {code}': return_value})


@app.route('/project', methods=['PATCH'])
def update_project():
    link = request.args.get('link')
    new_c = request.args.get('new_code')
    new_l = request.args.get('new_link')
    new_n = request.args.get('new_name')

    if new_n == None or new_l == None or new_c == None:
        return Response('Failed, arguments not nullable', 400, mimetype='application/json')
    return_value = Projects.update_project(
        _link=link, _new_link=new_l, _new_code=new_c, _new_name=new_n)
    return Response(return_value, 200, mimetype='application/json')


@app.route('/project', methods=['DELETE'])
def delete_project():
    link = request.args.get('link')

    return_value = Projects.delete_project(_link=link)
    return Response(return_value, 200, mimetype='application/json')

# todo SLIDES


@app.route('/slide', methods=['POST'])
def add_slide():
    code = request.args.get('course_code')
    name = request.args.get('name')
    link = request.args.get('link')
    return_value = Slides.add_slide(_course_code=code, _link=link, _name=name)
    return Response(return_value, 200, mimetype='application/json')


@app.route('/slides', methods=['GET'])
def get_all_slides():
    return_value = Slides.get_all_slides()
    return jsonify({f'slides': return_value})


@app.route('/slides-for-a-course', methods=['GET'])
def get_all_slides_for_a_course():
    code = request.args.get('course_code')
    return_value = Slides.get_slides_for_course(_course_code=code)
    return jsonify({'slides': return_value})


@app.route('/slide', methods=['GET'])
def get_specific_slide():
    link = request.args.get('link')
    return_value = Slides.get_slide(_link=link)
    return jsonify({f'slides': return_value})


@app.route('/slide', methods=['PATCH'])
def update_slide():
    link = request.args.get('link')
    new_c = request.args.get('course_code')
    new_l = request.args.get('new_link')

    return_value = Slides.update_slide(
        _link=link, _new_link=new_l, _code=new_c)
    return Response(return_value, 200, mimetype='application/json')


@app.route('/slide', methods=['DELETE'])
def delete_slide():
    link = request.args.get('link')

    return_value = Slides.delete_slide(_link=link)
    return Response(return_value, 200, mimetype='application/json')


# todo VIDEOS_COURSES
@app.route('/video-course', methods=['POST'])
def add_video_course():
    link = request.args.get('link')
    code = request.args.get('course_code')

    return_value = Videos_courses.add_video_course(
        _course_code=code, _link=link)
    return Response(return_value, 200, mimetype='application/json')


@app.route('/videos-courses', methods=['GET'])
def get_all_videos_courses():
    return_value = Videos_courses.get_all_vid_courses()
    return jsonify({'videos-courses': return_value})


@app.route('/videos-for-a-course', methods=['GET'])
def get_all_videos_for_a_course():
    code = request.args.get('course_code')
    return_value = Videos_courses.get_vids_for_course(_course_code=code)
    return jsonify({'videos': return_value})


@app.route('/video-course', methods=['GET'])
def get_video_course():
    code = request.args.get('course_code')
    link = request.args.get('link')
    return_value = Videos_courses.get_vid_course_rel(
        _course_code=code, _link=link)
    return jsonify({'video-course': return_value})


@app.route('/video-course', methods=['PATCH'])
def update_video_course():
    link = request.args.get('link')
    code = request.args.get('course_code')
    new_c = request.args.get('new_code')
    new_l = request.args.get('new_link')

    return_value = Videos_courses.update_vid_course(
        _link=link, _new_link=new_l, _new_code=new_c, _code=code)
    return Response(return_value, 200, mimetype='application/json')


@app.route('/video-course', methods=['DELETE'])
def delete_video_course():
    link = request.args.get('link')
    code = request.args.get('course_code')

    return_value = Videos_courses.delete_vid_course(_link=link, _course=code)
    return Response(return_value, 200, mimetype='application/json')


@app.route("/confirm_email/", methods=['GET', 'POST'])
def confirm_email():
    port = 465
    smtp_server = "smtp.gmail.com"

    sender_email = "pentecostalrevivalcenterag@gmail.com"
    receiver_email = str(userdetails["email"])
    name = userdetails['lastname']
    password = "revmosesasafo1954"

    confirmation_code = ""
    for a in range(0, 7):
        confirmation_code += str(random.randint(0, 9))

    userdetails["confirm_code"] = confirmation_code

    msg = MIMEText(" Hello " + name + " ! \n \n You signed up an account on the Slydehub .To confirm that it was really you, please enter the confirmatory code  into the box provided. Thank you \n \n \t \t Confirmatory Code: " +
                   confirmation_code + "\n \n  But if it was not you can ignore this mail sent to you ")
    msg['Subject'] = 'Portable library email confirmation'
    msg['From'] = 'pentecostalrevivalcenterag@gmail.com'
    msg['To'] = userdetails["email"]

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Mail sent')

    return redirect(url_for('sign_up_confirm_code'))


@app.route("/sign_up_confirm_code/", methods=["POST", "GET"])
def sign_up_confirm_code():
    info = {}
    if request.method == "POST":
        request_data = request.get_json()

        confirm_code = request_data["confirm_code"]
        print(confirm_code)
        confirmed_code = userdetails["confirm_code"]
        print(confirmed_code)
        # inserting statements into the database
        if confirmed_code == confirm_code:
            firstname = userdetails["firstname"]
            lastname = userdetails["lastname"]
            username = userdetails["username"]
            email = userdetails["email"]
            password = userdetails["password"]
            password = bcrypt.generate_password_hash(password).decode('utf-8')

            curs, connect = connection()

            # inserting statements into the database
            input_statement = (
                "INSERT INTO users (firstname,lastname,username, email, password) VALUES (%s, %s, %s, %s, %s)")
            data = (thwart(firstname), thwart(lastname), thwart(
                username), thwart(email), thwart(password))
            curs.execute(input_statement, data)

            connect.commit()
            curs.close()
            connect.close()
            gc.collect()
            info['status'] = 'You are successfully logged in'

            return jsonify(info)

        else:
            info['status'] = 'Error logging in'
            return jsonify(info)
    return jsonify('')


@app.route('/sign_up/', methods=["GET", "POST"])
def sign_up():
    info = {}
    if request.method == 'POST':
        request_data = request.get_json()
        userdetails["firstname"] = request_data["firstname"]
        userdetails["lastname"] = request_data["lastname"]
        userdetails["username"] = request_data["username"]
        userdetails["email"] = request_data["email"]

        userdetails["password"] = request_data["password"]

        curs, connect = connection()

        # checking if the username matches that of another person

        check_name = curs.execute(
            "SELECT * FROM users WHERE email = %s ", [userdetails["email"]])

        if int(check_name) > 0:
            info['status'] = 'Email already exist'
            return jsonify(info)

        else:
            return redirect(url_for("confirm_email"))

    return jsonify('')


@app.route("/forget_password/", methods=["POST", "GET"])
def forget_password():
    information = {}
    if request.method == "POST":
        request_data = request.get_json()
        email = request_data['email']

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
            password = "revmosesasafo1954"

            confirmation_code = ""
            for a in range(0, 7):
                confirmation_code += str(random.randint(0, 9))

            msg = MIMEText(" Hello! \n \n You requested for a reset of password on slydehub.To confirm that it was really you, please enter the confirmatory code  into the box providedonthe website. Thank you \n \n \t \t Confirmatory Code: " +
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
        conf = userdetails["conf"]
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
        request_data = request.get_json()
        username = request_data['username']
        password = request_data['password']
        confirm_password = request_data['confirm_password']

        if password == confirm_password:
            password = bcrypt.generate_password_hash(password).decode(utf-8)
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
def sign_in():
    d = {}
    if request.method == 'POST':

        request_data = request.get_json()
        email = request_data['email']
        password = request_data['password']
        curs, connect = connection()
        info = curs.execute("SELECT * FROM users WHERE email = %s", [email])

        # fetching the password
        Password = curs.execute(
            "SELECT password FROM users WHERE email = %s", [email])
        Password = curs.fetchone()
        print(info)
        print(Password)
        curs.close()
        connect.close()

        if info == 1 and bcrypt.check_password_hash(Password[0], password) == True:
            d["status"] = "Log in succesfully"
            return jsonify(d)

        else:
            d['status'] = "Invalid credentials, try again"
            return jsonify(d)
    return jsonify('')


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


@app.route('/slides/', methods=["GET", "POST"])
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
