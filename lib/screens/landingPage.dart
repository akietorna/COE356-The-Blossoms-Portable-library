import "package:flutter/material.dart";
import "bottomNavigationBar.dart";
import "drawer.dart";

class LandingPageState extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return LandingPage();
  }
}

class LandingPage extends State<LandingPageState> {
  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(

        drawer: DrawerState(),
        bottomNavigationBar: BottomNavigationBarState(),

      ),
    );
  }
}
