import "package:flutter/material.dart";

class BackgroundOverlayState extends StatefulWidget {
  final String overlayPathState;

  BackgroundOverlayState(this.overlayPathState);

  @override
  State<StatefulWidget> createState() {
    return BackgroundOverlay(overlayPathState);
  }
}

class BackgroundOverlay extends State<BackgroundOverlayState> {
  final String overlayPath;
  BackgroundOverlay(this.overlayPath);

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        Container(
          width: MediaQuery.of(context).size.width,
          height: MediaQuery.of(context).size.height,
          decoration: BoxDecoration(
              image: DecorationImage(
                  image: AssetImage(overlayPath),
                  fit: BoxFit.cover,
                  scale: 1.2)),
        ),
        Opacity(
            opacity: 0.7,
            child: Container(
              width: MediaQuery.of(context).size.width,
              height: MediaQuery.of(context).size.height,
              decoration: BoxDecoration(color: Colors.white),
            )),
      ],
    );
  }
}
