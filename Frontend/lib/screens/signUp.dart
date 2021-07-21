import 'package:flutter/material.dart';
import 'package:software_engineering_project/screens/main.dart';

class SignupPageState extends StatefulWidget{
  @override
  State<StatefulWidget> createState() {
   return SignupPage();
  }

}

class SignupPage extends State<SignupPageState>{
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Sign-up"),
        backgroundColor:appBarColor,
      ),
    );
  }
}