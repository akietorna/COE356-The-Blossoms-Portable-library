import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class HttpService {
  static final _client = http.Client();
  static var _loginUrl = Uri.parse("http://localhost:5000/");
  static var _signUpUrl = Uri.parse("http://localhost:5000/sign_up_page");

  static login(email, password, context) async {
    http.Response response = await _client
        .post(_loginUrl, body: {"email": email, "password": password});

    if (response.statusCode == 200) {
      Widget ErrorSnackBar(String message) {
        final snackBar = SnackBar(
          content: Text(message),
        );
        ScaffoldMessenger.of(context).showSnackBar(snackBar);
      }

      print(jsonDecode(response.body));
      var json = jsonDecode(response.body);

      if (json['status'] == ' login successfully') {
        await Navigator.pushNamed(context, '');
      }

      // ignore: unnecessary_statements
      else
        (ErrorSnackBar("Error loggin in"));
    }
  }

  static signUp(firstname, lastname, username, email, password, context) async {
    http.Response response = await _client.post(_signUpUrl, body: {
      "firstname": firstname,
      "lastname": lastname,
      "username": username,
      "email": email,
      "password": password
    });

    if (response.statusCode == 200) {
      var json = jsonDecode(response.body);
      if (json["status"] == "Email already exists") {
        Widget ErrorSnackBar(String message) {
          final snackBar = SnackBar(
            content: Text(message),
          );
          ScaffoldMessenger.of(context).showSnackBar(snackBar);
        }

        ErrorSnackBar("Email already used");
      }
    }
  }
}
