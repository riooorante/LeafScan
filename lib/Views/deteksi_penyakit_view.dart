import 'package:flutter/material.dart';
import '../controllers/deteksi_controller.dart';

class DeteksiPenyakitView extends StatelessWidget {
  final DeteksiController controller;

  DeteksiPenyakitView({Key? key, required this.controller}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.green[800],
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            // Ganti dengan gambar yang diunggah
            String gambar = 'path/to/image.jpg';
            controller.deteksiPenyakit(gambar);
          },
          child: Text('Deteksi Penyakit'),
        ),
      ),
    );
  }
}
