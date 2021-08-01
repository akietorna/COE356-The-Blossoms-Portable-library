import "package:flutter/material.dart";
import "package:software_engineering_project/screens/backgroundoverlay.dart";
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
      /* appBar: AppBar(
        title: Text("Log in"),
        centerTitle: true,
        backgroundColor: appBarColor,
      ),*/
      body: Stack(
        children: [
          // Container(
          //   width: MediaQuery.of(context).size.width,
          //   height: MediaQuery.of(context).size.height,
          //   decoration: BoxDecoration(
          //       image: DecorationImage(
          //           image: AssetImage("./assets/images/loginLibrary.jpg"),
          //           fit: BoxFit.cover,
          //           scale: 1.2)),
          // ),
          // Opacity(
          //     opacity: 0.7,
          //     child: Container(
          //       width: MediaQuery.of(context).size.width,
          //       height: MediaQuery.of(context).size.height,
          //       decoration: BoxDecoration(color: Colors.white),
          //     )),
          BackgroundOverlayState("./assets/images/loginLibrary.jpg"),

          ListView(children: [
            Container(
              margin: EdgeInsets.only(top: 30),
              child: Column(
                children: [
                  Text(
                    "Login",
                    textAlign: TextAlign.center,
                    textScaleFactor: 2,
                  ),
                  LogoImage("./assets/images/login.png"),
                  enterCredentials,
                  TextFieldState(
                      _userEmail, "E-mail", "Enter your e-mail", emailIcon),
                  PasswordFieldState(_password, "Password",
                      "Enter your password", passwordIcon),
                  Container(
                    margin: EdgeInsets.only(top: 20),
                    child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Container(
                                  alignment: Alignment.center,
                                  child: GestureDetector(
                                    onTap: () {
                                      Navigator.pushNamed(
                                          context, "/forgotPassword");
                                    },
                                    child: Container(
                                        alignment: Alignment.center,
                                        width: 110,
                                        height: 30,
                                        color: Colors.transparent,
                                        child: Text("forgot password")),
                                  ),
                                ),
                                Container(
                                  margin: EdgeInsets.only(left: 95),
                                  alignment: Alignment.centerRight,
                                  child: GestureDetector(
                                      onTap: () {
                                        Navigator.pushNamed(context, "/signup");
                                      },
                                      child: Row(
                                        mainAxisAlignment:
                                            MainAxisAlignment.end,
                                        children: [
                                          /* Icon(Icons.person_add),*/
                                          Container(
                                              alignment: Alignment.center,
                                              width: 70,
                                              height: 30,
                                              color: Colors.transparent,
                                              child: Text("Sign-up")),
                                        ],
                                      )),
                                ),
                              ]),
                          Container(
                            alignment: Alignment.bottomCenter,
                            margin: EdgeInsets.only(top: 50),
                            child: RaisedButton(
                                child: Text("Log in"),
                                color: ButtonColor,
                                onPressed: null),
                          )
                        ]),
                  )
                ],
              ),
            ),
          ]),
        ],
      ),
    );
  }
}
