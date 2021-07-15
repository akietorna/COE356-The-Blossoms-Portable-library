import "package:flutter/material.dart";
import 'package:software_engineering_project/screens/login.dart';
import "package:software_engineering_project/screens/signUp.dart";
import "package:software_engineering_project/screens/forgotPassword.dart";
import "package:software_engineering_project/screens/codeConfirmation.dart";

const appBarColor = Colors.blue;

void main() => runApp(MaterialApp(
      debugShowCheckedModeBanner: false,
      initialRoute: "/",
      routes: {
        "/": (context) => LoginPageState(),
        "/signup": (context) => SignupPageState(),
        "/forgotPassword": (context) => ForgotPasswordState(),
        "/forgotPassword/codeConfirmation": (context) =>
            CodeConfirmationState(),
      },
      title: "Blossoms",
    ));
