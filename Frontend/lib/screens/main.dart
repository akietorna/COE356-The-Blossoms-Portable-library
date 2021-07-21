import "package:flutter/material.dart";
import 'package:software_engineering_project/screens/login.dart';
import "package:software_engineering_project/screens/signUp.dart";

const appBarColor=Colors.blue;




void main()=> runApp(MaterialApp(

  initialRoute: "/",
  routes: {
    "/":(context)=>LoginPageState(),
    "/signup": (context)=>SignupPageState(),
  },
  title: "Blossoms",
));



