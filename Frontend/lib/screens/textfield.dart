import 'package:flutter/material.dart';

const ButtonColor=Colors.indigoAccent;


class LoginTextFieldState extends StatefulWidget{
  @override
  State<StatefulWidget> createState() {
 return LoginTextFields();
  }
}

class LoginTextFields extends State<LoginTextFieldState>{

  TextEditingController _userEmail= TextEditingController();
  TextEditingController _password=TextEditingController();


  @override
  Widget build(BuildContext context) {
return Column(
  children:[
    Container(
      alignment: Alignment.center,
    padding:EdgeInsets.all(15),
child:TextField(
       controller: _userEmail,
        decoration:InputDecoration(
         labelText:"E-mail",
          hintText: "Enter e-mail"
  )
) ,
  ),

    Container(
      alignment: Alignment.center,
      padding:EdgeInsets.all(15),
      child:TextField(
          controller: _password,
          obscureText:true,
          decoration:InputDecoration(

              labelText:"Password",
              hintText: "Enter password"
          )
      ) ,
    ),
    Row(
      mainAxisAlignment: MainAxisAlignment.center,
        children: [
          RaisedButton(
              child: Text("Log in"),
              color: ButtonColor,

              onPressed: null
          ),
          Container(
            margin: EdgeInsets.fromLTRB(70, 0, 0, 0),
            child: GestureDetector(

              child: Text("forgot password"),
            ),
          )


        ]
      ),
    ]

);
  }

}