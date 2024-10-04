import 'package:flutter/material.dart';
import 'Views/splash_screen_view.dart'; // Import splash screen

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'LeafScan',
        theme: ThemeData(
          primarySwatch: Colors.green,
        ),
        home: SplashScreenView(), // Set SplashScreen sebagai halaman pertama
        debugShowCheckedModeBanner: false);
  }
}
