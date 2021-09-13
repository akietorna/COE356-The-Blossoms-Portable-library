from blossoms.models.courses_model import *
from blossoms.models.books_model import *
from blossoms.models.books_courses import *
from blossoms.models.programs_model import *
from blossoms.models.videos_model import *

@app.route('/courses', methods = ['GET'])
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
    if len(exists)>0:
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
    if exists==[]:
        return 'course doesnt exist'
    Courses.update_course(request_data['course_code'], request_data['name'], request_data['about'])
    response = Response('Course updated', status=200, mimetype='application/json')
    return response


@app.route('/course', methods=['DELETE'])
def remove_course():
    '''Function to delete movie from our database'''
    code = request.args.get("code")
    exists = Courses.get_course(_code=code)
    if exists == []:
        return 'course doesnt exist'
    Courses.delete_course(code)
    response = Response("course Deleted", status=200, mimetype='application/json')
    return response

@app.route('/books', methods = ['GET'])
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
    if len(exists)>0:
        return 'already exists'
    Books.add_book(request_data["name"], request_data["link"])
    response = Response("Book added", 201, mimetype='application/json')
    return response


@app.route('/book', methods=['PATCH'])
def update_book():
    '''Function to edit movie in our database using movie id'''
    request_data = request.get_json()
    exists = Books.get_book(_link=request_data['link'])
    if exists==[]:
        return 'Book doesnt exist'
    Books.update_book(request_data['link'], request_data['name'])
    response = Response('Book updated', status=200, mimetype='application/json')
    return response


@app.route('/book', methods=['DELETE'])
def remove_book():
    '''Function to delete movie from our database'''
    link = request.args.get("link")
    exists = Books.get_book(_link=link)
    if exists == []:
        return 'Book doesnt exist'
    Books.delete_book(link)
    response = Response("Book Deleted", status=200, mimetype='application/json')
    return response


@app.route('/programs', methods = ['GET'])
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
    if len(exists)>0:
        return 'already exists'
    Programs.add_program(request_data["name"], request_data["about"], request_data['department'])
    response = Response("Program added", 201, mimetype='application/json')
    return response


@app.route('/program', methods=['PATCH'])
def update_program():
    '''Function to edit movie in our database using movie id'''
    request_data = request.get_json()
    exists = Programs.get_program(_name=request_data['name'])
    if exists==[]:
        return 'Program doesnt exist'
    Programs.update_program(request_data['name'], request_data['about'], request_data['department'])
    response = Response('Program updated', status=200, mimetype='application/json')
    return response


@app.route('/program', methods=['DELETE'])
def remove_program():
    '''Function to delete movie from our database'''
    name = request.args.get("name")
    exists = Programs.get_program(_name=name)
    if exists == []:
        return 'program doesnt exist'
    Programs.delete_program(name)
    response = Response("Program Deleted", status=200, mimetype='application/json')
    return response


@app.route('/videos', methods = ['GET'])
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
    if len(exists)>0:
        return 'already exists'
    Videos.add_video(request_data["name"], request_data['link'])
    response = Response("Video added", 201, mimetype='application/json')
    return response


@app.route('/video', methods=['PATCH'])
def update_video():
    '''Function to edit movie in our database using movie id'''
    request_data = request.get_json()
    exists = Videos.get_video(_link=request_data['link'])
    if exists==[]:
        return 'Video doesnt exist'
    Videos.update_video(request_data['name'], request_data['link'], request_data['creator'])
    response = Response('Video updated', status=200, mimetype='application/json')
    return response


@app.route('/video', methods=['DELETE'])
def remove_video():
    '''Function to delete movie from our database'''
    link = request.args.get("link")
    exists = Videos.get_video(_link=link)
    if exists == []:
        return 'Video doesnt exist'
    Videos.delete_video(link)
    response = Response("Video Deleted", status=200, mimetype='application/json')
    return response

#todo books_courses

@app.route('/books-courses', methods=['GET'])
def get_all_books_courses():
    return_value = Books_courses.get_all_books_courses()
    return jsonify({'books-courses':return_value})

<<<<<<< HEAD
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


@app.route('/get_users', methods=['GET'])
def get_users():

    return jsonify(Users.get_all_users())


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
=======
@app.route('/book-course-rel', methods=['GET'])
def get_book_course_rel():
    '''Function to delete movie from our database'''
    link = request.args.get("link")
    code = request.args.get('course_code')
>>>>>>> 4a7b35e5b8441ad31ed2ed13cc6f3adc4d66e3c5

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
    link = request.args.get("link")# getting data from client

    results = Books_courses.add_book_course(_link=link, _course_code=code)

    response = Response(results, 200, mimetype='application/json')
    return response

<<<<<<< HEAD
        Users.add_user(first_name, last_name, user_name, email, password)
        response = Response("User added", 201, mimetype='application/json')
=======
@app.route('/book-course', methods=['PATCH'])
def update_book_course():
    '''Function to delete movie from our database'''
    try:
        link = request.args.get("link")
        code = request.args.get('course_code')
        new_link = request.args.get('new_link')
    except:
        pass
    if new_link==None:
        response = Response('Failed, provide new link', 400, mimetype='application/json')
>>>>>>> 4a7b35e5b8441ad31ed2ed13cc6f3adc4d66e3c5
        return response
    results = Books_courses.update_book_course(_link=link, _course_code=code, _new_link=new_link)
    return Response(results, 200, mimetype='application/jsosn')

@app.route('/book-course', methods=['DELETE'])
def delete_book_course():
    '''Function to delete movie from our database'''
    link = request.args.get("link")
    code = request.args.get('course_code')

<<<<<<< HEAD
@app.route('/remove_user', methods=['DELETE'])
def remove_user():
    '''Function to delete user from our database'''
    name = request.args.get("name")
    exists = Users.get_user(_name=name)
    if exists == []:
        return 'User does not exist'
    Users.delete_program(name)
    response = Response("User Deleted", status=200,
                        mimetype='application/json')
=======
    results = Books_courses.delete_book_course(_course_code=code, _link=link)
    response = Response(results, 200, mimetype='application/json')
>>>>>>> 4a7b35e5b8441ad31ed2ed13cc6f3adc4d66e3c5
    return response





if __name__ == "__main__":
    app.run(port=1234, debug=True)