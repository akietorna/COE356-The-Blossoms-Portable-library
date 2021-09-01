import "package:flutter/material.dart";
import "package:software_engineering_project/screens/backgroundoverlay.dart";
import 'package:software_engineering_project/screens/httpForLoginAndSignup.dart';
import 'package:software_engineering_project/screens/logo.dart';
import "package:http/http.dart" as http;

// import 'package:software_engineering_project/screens/textfield.dart';
// import 'package:software_engineering_project/screens/passwordTextField.dart';

const enterCredentials = Center(child: Text("Enter your credential..."));

Widget emailIcon = Icon(Icons.email);

class LoginPageState extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return LoginPage();
  }
}

class LoginPage extends State<LoginPageState> {
  bool _obscurity = true;

  Widget passwordSufixIcon() {
    if (_obscurity == true) {
      return Icon(Icons.visibility_off);
    } else {
      return Icon(Icons.visibility);
    }
  }

  void _togglePasswordView() {
    setState(() {
      _obscurity = !_obscurity;
    });
  }

  TextEditingController _userEmail = TextEditingController();
  TextEditingController _password = TextEditingController();

  final LoginFormKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          //BackgroundOverlayState("./assets/images/loginLibrary.jpg"),
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
                  Container(
                    child: Form(
                      key: LoginFormKey,
                      child: Column(children: [
                        //Login user email entry point

                        TextFormField(
                            validator: (value) => value.contains("@")
                                ? null
                                : "Enter a valid email",
                            autofocus: true,
                            controller: _userEmail,
                            decoration: InputDecoration(
                              border: OutlineInputBorder(
                                borderSide: BorderSide(color: Colors.white),
                                borderRadius: BorderRadius.circular(10.0),
                              ),
                              prefixIcon: Icon(Icons.email),
                              labelText: "E-mail",
                              hintText: "Enter your e-mail",
                              // hintStyle: TextStyle(color: hintColor)
                            )),

                        // user password entry point

                        TextFormField(
                            validator: (value) => value.length < 8
                                ? "Password should be more than 8 characters"
                                : null,
                            controller: _password,
                            obscureText: _obscurity,
                            decoration: InputDecoration(
                              prefixIcon: Icon(Icons.lock),
                              suffix: InkWell(
                                  onTap: _togglePasswordView,
                                  child: passwordSufixIcon()),
                              border: OutlineInputBorder(
                                borderSide: BorderSide(
                                  color: Colors.red,
                                ),
                                borderRadius: BorderRadius.circular(10.0),
                              ),
                              labelText: "Password",
                              hintText: "Enter your password",
                            )),

                        // call to actions

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
                                              Navigator.pushNamed(
                                                  context, "/signup");
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
                                  child: ElevatedButton(
                                      child: Text("Log in"),
                                      onPressed: () async {
                                        await HttpService.login(
                                            _userEmail, _password, context);
                                      }),
                                )
                              ]),
                        )
                      ]),
                    ),
                  ),

                  // TextFieldState(
                  //     _userEmail, "E-mail", "Enter your e-mail", emailIcon),
                  // PasswordFieldState(_password, "Password",
                  //     "Enter your password", passwordIcon),
                ],
              ),
            ),
          ]),
        ],
      ),
    );
  }
}
