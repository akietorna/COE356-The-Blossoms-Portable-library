# create database if not exists  library;
# use library;
#
# create table books(id int not null primary key auto_increment, link varchar(500),name varchar(100),ISBN int(20),author varchar(50),publisher varchar(100));
# create table courses(course_code varchar(10) not null primary key , name varchar(50),about varchar(100));
# create table books_courses(id int not null,course_code varchar(10) not null );
# alter table books_courses add foreign key (id) references books(id);
# alter table books_courses add foreign key (course_code) references courses(course_code);
# create table preps(id int not null primary key auto_increment, link varchar(500),name varchar(100), course_code varchar(6));
# create table programs(name varchar(50) not null primary key, about varchar(1000),department varchar(100),faculty varchar(100));
# create table programs_courses(name varchar(50) not null primary key,sem int(2),course_code varchar(10));
# alter table programs_courses add foreign key (name) references programs(name);*****
# alter table programs_courses add foreign key (course_code) references courses(course_code);
# create table project(id int not null primary key auto_increment, link varchar(500),name varchar(100));
# create table slides(id int not null primary key auto_increment, link varchar(500),name varchar(100),course_code varchar(10));
# alter table slides add foreign key (course_code) references courses(course_code);
# create table users(user_id int not null primary key auto_increment,firstname varchar(50),lastname varchar(50),username varchar(50),email varchar(50),password varchar(200) );
# create table videos(id int not null primary key auto_increment, link varchar(500),name varchar(100),creator varchar(50));
# create table videos_courses(id int not null,course_code varchar(10) not null );
# alter table videos_courses add foreign key (id) references videos(id);
# alter table videos_courses add foreign key (course_code) references courses(course_code);




{
    "name":"Numeriacal Analysis",
    "course_code":"Math 351",
    "about":"Numerical analysis is the area of mathematics and computer science that creates, analyzes, and implements algorithms for solving numerically the problems of continuous mathematics. ... These problems occur throughout the natural sciences, social sciences, medicine, engineering, and business"
}