class HistoriDeteksi {
  int idDeteksi;
  DateTime tanggalDeteksi;
  String penyakit;
  String deskripsiPenyakit;
  String namaIlmiah;
  Uri urlGambar;
  String gejala;
  DateTime terakhirDiAkses;

  HistoriDeteksi(
      {required this.idDeteksi,
      required this.tanggalDeteksi,
      required this.penyakit,
      required this.urlGambar,
      required this.deskripsiPenyakit,
      required this.namaIlmiah,
      required this.gejala,
      required this.terakhirDiAkses});

  // Method untuk menampilkan informasi detail
  String tampilkanRincianRekomendasi() {
    return '';
  }
}
