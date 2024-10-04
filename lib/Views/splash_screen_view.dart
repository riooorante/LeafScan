// ignore_for_file: prefer_const_constructors, prefer_const_literals_to_create_immutables

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:leafscan/controllers/deteksi_controller.dart';
import 'deteksi_penyakit_view.dart'; // Import halaman utama

class SplashScreenView extends StatefulWidget {
  @override
  _SplashScreenViewState createState() => _SplashScreenViewState();
}

class _SplashScreenViewState extends State<SplashScreenView> {
  final DeteksiController _deteksiController = DeteksiController();

  @override
  void initState() {
    super.initState();
    // Mengatur waktu delay splash screen
    Future.delayed(Duration(seconds: 3), () {
      // Pindah ke halaman utama setelah 3 detik
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(
            builder: (context) => DeteksiPenyakitView(
                  controller: _deteksiController,
                )),
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(
          0xFFF5F3E8), // Warna background sesuai dengan splash screen (beige muda)
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            // Gambar logo
            Image.asset(
              'assets/images/logo_leafscan.png', // Ganti dengan path gambar logo kamu
              width: 150, // Atur ukuran gambar sesuai kebutuhan
              height: 150,
            ),
            SizedBox(height: 20),
            // Nama aplikasi
            Text(
              'LeafScan',
              style: GoogleFonts.alfaSlabOne(
                textStyle: TextStyle(
                  fontSize: 30,
                  fontWeight: FontWeight.bold,
                  color: Color.fromARGB(255, 75, 196, 79),
                  letterSpacing: 2.0,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
