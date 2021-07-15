import 'package:flutter/material.dart';

class LogoImage extends StatelessWidget {
  final logomarging = EdgeInsets.fromLTRB(0, 30, 0, 0);
  final logoWidth = 150.0;
  final logoHeight = 150.0;
  final String imagePath;

  LogoImage(this.imagePath);

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Container(
        margin: logomarging,
        alignment: Alignment.center,
        width: logoWidth,
        height: logoHeight,
        decoration: BoxDecoration(
            color: Colors.white,
            shape: BoxShape.circle,
            image: DecorationImage(
                image: AssetImage(imagePath), //fit: BoxFit.cover,
                scale: 1.2)),
      ),
    );
  }
}
