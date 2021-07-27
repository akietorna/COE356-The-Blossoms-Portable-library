import 'package:flutter/material.dart';
import 'package:software_engineering_project/screens/logo.dart';
import "package:software_engineering_project/screens/backgroundoverlay.dart";
import 'package:software_engineering_project/screens/login.dart';
import 'package:software_engineering_project/screens/textfield.dart';
import 'package:software_engineering_project/screens/passwordTextField.dart';

Widget nameIcon = Icon(Icons.person);

class SignupPageState extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return SignupPage();
  }
}

class SignupPage extends State<SignupPageState> {
  TextEditingController _firstName = TextEditingController();
  TextEditingController _lastName = TextEditingController();
  TextEditingController _email = TextEditingController();
  TextEditingController _password = TextEditingController();
  TextEditingController _confirmPassword = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        /*appBar: AppBar(
          title: Text("Sign-up"),
          centerTitle: true,
          backgroundColor: appBarColor,
        ),*/
        body: Stack(
      children: [
        BackgroundOverlayState("./assets/images/signupLibrary.jpg"),
        ListView(
          children: [
            LogoImage("./assets/images/signup.png"),
            enterCredentials,
            TextFieldState(
                _firstName, "First name", "Enter first name", nameIcon),
            TextFieldState(_lastName, "Last name", "Enter last name", nameIcon),
            TextFieldState(_email, "E-mail", "Enter e-mail", emailIcon),
            PasswordFieldState(
                _password, "Password", "Enter password", passwordIcon),
            PasswordFieldState(
                _confirmPassword, "Confirm", "Confirm password", passwordIcon),
            Container(
                margin: EdgeInsets.fromLTRB(0, 0, 0, 20),
                child:
                    Row(mainAxisAlignment: MainAxisAlignment.center, children: [
                  RaisedButton(
                      child: Text("Sign up"),
                      color: ButtonColor,
                      onPressed: null),
                  Container(
                    alignment: Alignment.center,
                    margin: EdgeInsets.fromLTRB(50, 0, 0, 0),
                    child: GestureDetector(
                      onTap: () {
                        Navigator.pop(context, "/");
                      },
                      child: Text("Already have an account"),
                    ),
                  )
                ])),
          ],
        )
      ],
    ));
  }
}
