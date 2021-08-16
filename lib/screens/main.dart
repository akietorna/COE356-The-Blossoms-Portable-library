import "package:flutter/material.dart";
import 'package:software_engineering_project/screens/login.dart';
import "package:software_engineering_project/screens/signUp.dart";
import "package:software_engineering_project/screens/forgotPassword.dart";
import "package:software_engineering_project/screens/codeConfirmation.dart";
import 'package:software_engineering_project/screens/chosenCourse.dart';
import 'package:software_engineering_project/screens/chooseProgram.dart';

const appBarColor = Colors.blue;

void main() => runApp(MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
       
        brightness: Brightness.dark,
        primarySwatch: Colors.indigo,
      ),
      
      initialRoute: "/",
      routes: {
        "/": (context) => LoginPageState(),
        "/signup": (context) => SignupPageState(),
        "/forgotPassword": (context) => ForgotPasswordState(),
        "/forgotPassword/codeConfirmation": (context) =>
            CodeConfirmationState(),
            "/login/landingPage":(context) => ChosenCourse(programYearCourses['computer']['1']),
      },
      title: "Blossoms",
    ));
