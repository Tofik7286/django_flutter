import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'screens/login.dart';
import 'screens/profile.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  SharedPreferences prefs = await SharedPreferences.getInstance();
  int? userId = prefs.getInt('user_id');

  runApp(MaterialApp(
    debugShowCheckedModeBanner: false,
    home: userId == null ? LoginScreen() : ProfileScreen(),
  ));
}
