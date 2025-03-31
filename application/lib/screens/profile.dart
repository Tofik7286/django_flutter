import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import 'login.dart';

class ProfileScreen extends StatefulWidget {
  @override
  _ProfileScreenState createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  Map<String, dynamic>? userData;

  Future<void> fetchProfile() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    int? userId = prefs.getInt('user_id');

    if (userId == null) {
      print("❌ Error: user_id not found in SharedPreferences");
      return;
    }

    final response = await http.get(
      Uri.parse('http://192.168.18.145:8000/api/profile/$userId/'),
    );

    print("🔍 Debug: API Response = ${response.body}"); // ✅ Debugging

    if (response.statusCode == 200) {
      setState(() {
        userData = json.decode(response.body);
      });
    } else {
      print("❌ Error: Profile Fetch Failed! Status: ${response.statusCode}");
    }
  }

  Future<void> logoutUser() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    await prefs.remove('user_id'); // ✅

    Navigator.pushReplacement(
      context,
      MaterialPageRoute(builder: (context) => LoginScreen()),
    );
  }

  @override
  void initState() {
    super.initState();
    fetchProfile();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('User Profile')),
      body: userData == null
          ? Center(child: CircularProgressIndicator())
          : Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                children: [
                  if (userData!['profile_pic'] != null)
                    CircleAvatar(
                      radius: 50,
                      backgroundImage: NetworkImage(
                        'http://192.168.18.145:8000' +
                            userData!['profile_pic'],
                      ),
                    ),
                  SizedBox(height: 20),
                  Text('Username: ${userData!['user']['username']}'),
                  Text('Email: ${userData!['user']['email']}'),
                  Text('Gender: ${userData!['gender']}'),
                  Text('Hobbies: ${userData!['hobbies']}'),
                  SizedBox(height: 20),
                  ElevatedButton(
                    onPressed: logoutUser,
                    child: Text('Logout'),
                  ),
                ],
              ),
            ),
    );
  }
}
