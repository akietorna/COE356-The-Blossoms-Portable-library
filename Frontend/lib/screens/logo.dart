import 'package:flutter/material.dart';



class LogoImage extends StatelessWidget{



  final logoPadding=EdgeInsets.fromLTRB(0, 100, 0, 50);
  final logomarging=EdgeInsets.fromLTRB(0,50,0,50);
  final logoWidth=150.0;
  final logoHeight=150.0;
  String imagePath;


  @override
  Widget build(BuildContext context) {
    return Container(
margin: logoPadding,
    alignment: Alignment.center,

width: logoWidth,
height: logoHeight,

decoration: BoxDecoration(
  color: Colors.grey,
shape: BoxShape.circle,

/*image: DecorationImage(
image: AssetImage(""),
fit: BoxFit.fill

)*/
)
);
  }

}