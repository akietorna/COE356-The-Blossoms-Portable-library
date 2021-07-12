import "package:flutter/material.dart";
import "package:software_engineering_project/screens/main.dart";
import "package:software_engineering_project/screens/logo.dart";
import "package:software_engineering_project/screens/login.dart";

class ForgotPasswordState extends StatefulWidget{
  @override
  State<StatefulWidget> createState(){
    return ForgotPassword();
  }
}

Class ForgotPassword extends State<ForgotPasswordState>{

TextEditingController _email=TextEditingController();

  @override
  Widget build(BuildContext, context){
    return Scaffold(
      appBar:AppBar(
        title:Text("Forgot password"),
        centerTitle:true,
        backgroundColor:appBarColor,
      ),
      body: ListView(
        children:[
          LogoImage(),
          Text("Enter your email below"),
          TextFieldState(
                  _email, "E-mail", "Enter your e-mail", emailIcon),
          RaisedButton(
                    child: Text("Submit"), color: ButtonColor, onPressed: null),

        ]

      );

    );
  }
}
