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





if __name__ == "__main__":
    app.run(port=1234, debug=True)