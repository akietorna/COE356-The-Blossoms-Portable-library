import 'package:flutter/material.dart';
import 'package:software_engineering_project/screens/logo.dart';
import "package:software_engineering_project/screens/backgroundoverlay.dart";
import 'package:software_engineering_project/screens/login.dart';
import "package:software_engineering_project/screens/httpForLoginAndSignup.dart";
// import 'package:software_engineering_project/screens/textfield.dart';

Widget nameIcon = Icon(Icons.person);

class SignupPageState extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return SignupPage();
  }
}

class SignupPage extends State<SignupPageState> {
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

  final signUpKey = GlobalKey<FormState>();

  TextEditingController _firstName = TextEditingController();
  TextEditingController _lastName = TextEditingController();
  TextEditingController _userName = TextEditingController();
  TextEditingController _userEmail = TextEditingController();
  TextEditingController _password = TextEditingController();

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
            Container(
                child: Form(
                    key: signUpKey,
                    child: Column(children: [
                      //First name
                      TextFormField(
                          validator: (value) => value.isEmpty
                              ? "Please enter your first name"
                              : null,
                          autofocus: true,
                          controller: _firstName,
                          decoration: InputDecoration(
                            border: OutlineInputBorder(
                              borderSide: BorderSide(color: Colors.white),
                              borderRadius: BorderRadius.circular(10.0),
                            ),
                            prefixIcon: Icon(Icons.person),
                            labelText: "First Name",
                            hintText: "Enter your first name",
                            // hintStyle: TextStyle(color: hintColor)
                          )),

                      //Last name
                      TextFormField(
                          validator: (value) => value.isEmpty
                              ? "Please enter your last name"
                              : null,
                          controller: _lastName,
                          decoration: InputDecoration(
                            border: OutlineInputBorder(
                              borderSide: BorderSide(color: Colors.white),
                              borderRadius: BorderRadius.circular(10.0),
                            ),
                            prefixIcon: Icon(Icons.person),
                            labelText: "Last Name",
                            hintText: "Enter your first name",
                            // hintStyle: TextStyle(color: hintColor)
                          )),

                      TextFormField(
                          validator: (value) => value.isEmpty
                              ? "Please enter your user name"
                              : null,
                          controller: _userName,
                          decoration: InputDecoration(
                            border: OutlineInputBorder(
                              borderSide: BorderSide(color: Colors.white),
                              borderRadius: BorderRadius.circular(10.0),
                            ),
                            prefixIcon: Icon(Icons.person),
                            labelText: "User Name",
                            hintText: "Enter preffered user name",
                            // hintStyle: TextStyle(color: hintColor)
                          )),

                      //User email
                      TextFormField(
                          validator: (value) => value.contains("@")
                              ? null
                              : "Enter a valid email",
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

                      //Password

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
                                color: Colors.white,
                              ),
                              borderRadius: BorderRadius.circular(10.0),
                            ),
                            labelText: "Password",
                            hintText: "Enter your password",
                          )),

                      //confirm password

                      TextFormField(
                          validator: (value) => value == _password.text
                              ? null
                              : "Passwords do not match",
                          controller: _password,
                          obscureText: _obscurity,
                          decoration: InputDecoration(
                            prefixIcon: Icon(Icons.lock),
                            suffix: InkWell(
                                onTap: _togglePasswordView,
                                child: passwordSufixIcon()),
                            border: OutlineInputBorder(
                              borderSide: BorderSide(
                                color: Colors.white,
                              ),
                              borderRadius: BorderRadius.circular(10.0),
                            ),
                            labelText: "Confirm Password",
                            hintText: "Confirm password",
                          )),

                      //call to actions
                      Container(
                          margin: EdgeInsets.fromLTRB(0, 0, 0, 20),
                          child: Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                ElevatedButton(
                                    child: Text("Sign up"),
                                    onPressed: () async {
                                      await HttpService.signUp(
                                          _firstName,
                                          _lastName,
                                          _userName,
                                          _userEmail,
                                          _password,
                                          context);
                                    }),
                                Container(
                                  width: 50,
                                  color: Colors.grey.withOpacity(0),
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
                    ]))),
            // TextFieldState(
            //     _firstName, "First name", "Enter first name", nameIcon),
            // TextFieldState(_lastName, "Last name", "Enter last name", nameIcon),
            // TextFieldState(_userEmail, "E-mail", "Enter e-mail", emailIcon),
            // PasswordFieldState(
            //     _password, "Password", "Enter password", passwordIcon),
            // PasswordFieldState(
            //     _confirmPassword, "Confirm", "Confirm password", passwordIcon),
          ],
        )
      ],
    ));
  }
}
