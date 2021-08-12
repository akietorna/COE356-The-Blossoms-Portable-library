import "package:flutter/material.dart";
import 'package:software_engineering_project/screens/logo.dart';
import "package:software_engineering_project/screens/main.dart";
import "package:software_engineering_project/screens/backgroundoverlay.dart";

class SignUpCodeConfirmationState extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return SignUpCodeConfirmation();
  }
}

class SignUpCodeConfirmation extends State<CodeConfirmationState> {
  TextEditingController codeConfirmation = TextEditingController();
  Widget codeConfirmationIcon = Icon(Icons.coronavirus);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Confirm code"),
          centerTitle: true,
          backgroundColor: appBarColor,
        ),
        body: Stack(
          children: [
            BackgroundOverlayState("./assets/images/confirmCodeLibrary.jpg"),
            ListView(children: [
              LogoImage("./assets/images/code.png"),
              Container(
                margin: EdgeInsets.fromLTRB(0, 10, 0, 0),
                child: Center(child: Text("Enter your email below")),
              ),
              Container(
                alignment: Alignment.center,
                padding: EdgeInsets.all(15),
                child: TextField(
                  controller: codeConfirmation,
                  keyboardType: TextInputType.number,
                  decoration: InputDecoration(
                    border: OutlineInputBorder(
                      borderSide: BorderSide(
                        color: Colors.red,
                      ),
                      borderRadius: BorderRadius.circular(10.0),
                    ),
                    prefixIcon: codeConfirmationIcon,
                    labelText: "Confirm code",
                    hintText: "Enter the confirmation code",
                    hintStyle: TextStyle(color: Colors.indigoAccent),
                  ),
                ),
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  RaisedButton(
                      child: Text("Submit"),
                      onPressed: () {
                        Navigator.pushNamed(
                            context, "/forgotPassword/codeConfirmation");
                      },
                      color: Colors.red),
                  Container(
                    margin: EdgeInsets.fromLTRB(50, 0, 0, 0),
                    child: GestureDetector(
                      child: Text("Resend code"),
                      onTap: null,
                    ),
                  )
                ],
              )
            ]),
          ],
        ));
  }
}
