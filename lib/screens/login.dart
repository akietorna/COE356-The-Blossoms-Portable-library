import "package:flutter/material.dart";
import 'package:software_engineering_project/screens/main.dart';
import 'package:software_engineering_project/screens/logo.dart';
import 'package:software_engineering_project/screens/textfield.dart';
import 'package:software_engineering_project/screens/passwordTextField.dart';

const enterCredentials = Center(child: Text("Enter your credential..."));

Widget emailIcon = Icon(Icons.email);

class LoginPageState extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return LoginPage();
  }
}

class LoginPage extends State<LoginPageState> {
  TextEditingController _userEmail = TextEditingController();
  TextEditingController _password = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Log in"),
        centerTitle: true,
        backgroundColor: appBarColor,
      ),
      body: ListView(
        children: [
          Container(
            margin: EdgeInsets.fromLTRB(0, 10, 10, 0),
            alignment: Alignment.topRight,
            child: GestureDetector(
                onTap: () {
                  Navigator.pushNamed(context, "/signup");
                },
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.end,
                  children: [
                    Icon(Icons.person_add),
                    Text("Sign-up"),
                  ],
                )),
          ),
          Column(
            children: [
              LogoImage("./assets/images/login.png"),
              enterCredentials,
              TextFieldState(
                  _userEmail, "E-mail", "Enter your e-mail", emailIcon),
              PasswordFieldState(
                  _password, "Password", "Enter your password", passwordIcon),
              Row(mainAxisAlignment: MainAxisAlignment.center, children: [
                RaisedButton(
                    child: Text("Log in"), color: ButtonColor, onPressed: null),
                Container(
                  margin: EdgeInsets.fromLTRB(80, 0, 0, 0),
                  child: GestureDetector(
                    onTap: () {
                      Navigator.pushNamed(context, "/forgotPassword");
                    },
                    child: Text("forgot password"),
                  ),
                )
              ]),
            ],
          ),
        ],
      ),
    );
  }
}
