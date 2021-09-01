import "package:flutter/material.dart";
import "package:software_engineering_project/screens/main.dart";
import "package:software_engineering_project/screens/logo.dart";

// import "package:software_engineering_project/screens/textfield.dart";
import "package:software_engineering_project/screens/backgroundoverlay.dart";

class ForgotPasswordState extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return ForgotPassword();
  }
}

class ForgotPassword extends State<ForgotPasswordState> {
  TextEditingController _email = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Forgot password"),
          centerTitle: true,
         // backgroundColor: appBarColor,
        ),
        body: Stack(
          children: [
           // BackgroundOverlayState("./assets/images/forgotpassword.jpg"),
            ListView(children: [
              LogoImage("./assets/images/forgotpassword.png"),
              Center(
                child: Container(
                  margin: EdgeInsets.fromLTRB(0, 10, 0, 0),
                  child: Center(child: Text("Enter your email below")),
                ),
              ),

              TextFormField(
                  validator: (value) =>
                      value.contains("@") ? null : "Enter a valid email",
                  autofocus: true,
                  controller: _email,
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
              // TextFieldState(_email, "E-mail", "Enter your e-mail", emailIcon),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  ElevatedButton(
                    child: Text("Submit"),
                    onPressed: () {
                      Navigator.pushNamed(
                          context, "/forgotPassword/codeConfirmation");
                    },
                  ),
                ],
              )
            ]),
          ],
        ));
  }
}
