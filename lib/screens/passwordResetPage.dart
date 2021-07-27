import 'package:flutter/material.dart';
import "package:software_engineering_project/screens/main.dart";
import "package:software_engineering_project/screens/logo.dart";
import "package:software_engineering_project/screens/passwordTextField.dart";

class PasswordResetState extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return PasswordReset();
  }
}

class PasswordReset extends State<PasswordResetState> {
  TextEditingController _newPassword = TextEditingController();
  TextEditingController _confirmNewPassword = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Password reset"),
        centerTitle: true,
        backgroundColor: appBarColor,
      ),
      body: ListView(
        children: [
          // LogoImage("./assets/images/.png"),
          Center(
            child: Container(
              margin: EdgeInsets.fromLTRB(0, 10, 0, 0),
              child: Center(child: Text("Reset password below")),
            ),
          ),
          PasswordFieldState(_newPassword, "New password",
              "Enter your new password", passwordIcon),
          PasswordFieldState(_confirmNewPassword, "Confirm new password",
              "Confirm your new password", passwordIcon),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              RaisedButton(
                  child: Text("Confirm"),
                  onPressed: () {
                    Navigator.pushNamed(context, "/");
                  },
                  color: Colors.red),
            ],
          )
        ],
      ),
    );
  }
}
