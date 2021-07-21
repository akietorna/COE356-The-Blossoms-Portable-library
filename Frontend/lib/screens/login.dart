import "package:flutter/material.dart";
import 'package:software_engineering_project/screens/main.dart';
import 'package:software_engineering_project/screens/logo.dart';
import 'package:software_engineering_project/screens/textfield.dart';




class LoginPageState extends StatefulWidget{
  @override
  State<StatefulWidget> createState() {

    return LoginPage();
  }
}

class LoginPage extends State<LoginPageState>{

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
           margin: EdgeInsets.fromLTRB(0,5,5,0),
           alignment: Alignment.topRight,
           child: GestureDetector(
             onTap: (){Navigator.pushNamed(context, "/signup");},

             child: Text("Sign-up"),
           ),
         ),
         Column(
            children:[
                LogoImage(),
              Text("Enter your credentials.."),
              LoginTextFieldState(),

            ],
          ),
        ],
      ),
    );
  }

}