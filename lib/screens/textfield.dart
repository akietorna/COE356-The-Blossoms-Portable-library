import 'package:flutter/material.dart';

const hintColor = Colors.indigoAccent;
const ButtonColor = Colors.green;

class TextFieldState extends StatefulWidget {
  final TextEditingController textFieldController;
  final String textFieldLabel, textFieldhint;
  final Widget textFieldIconState;

  TextFieldState(this.textFieldController, this.textFieldLabel,
      this.textFieldhint, this.textFieldIconState);

  @override
  State<StatefulWidget> createState() {
    return TextFields(
        textFieldController, textFieldLabel, textFieldhint, textFieldIconState);
  }
}

class TextFields extends State<TextFieldState> {
  String hint, label;
  TextEditingController controler;
  Widget textFieldIcon;
  TextFields(this.controler, this.label, this.hint, this.textFieldIcon);

  @override
  Widget build(BuildContext context) {
    return Column(children: [
      Container(
        alignment: Alignment.center,
        padding: EdgeInsets.all(15),
        child: TextField(
            controller: controler,
            decoration: InputDecoration(
                border: OutlineInputBorder(
                  borderSide: BorderSide(
                    color: Colors.red,
                  ),
                  borderRadius: BorderRadius.circular(10.0),
                ),
                prefixIcon: textFieldIcon,
                labelText: label,
                hintText: hint,
                hintStyle: TextStyle(color: hintColor))),
      ),
    ]);
  }
}
