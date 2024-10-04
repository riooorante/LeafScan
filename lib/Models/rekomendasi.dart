class Rekomendasi {
  int idRekomendasi;
  int idDeteksi;
  String nama;
  String metode;
  // String dosis;
  // String waktuPenggunaan;
  String tindakanPencegahan;

  Rekomendasi(
      {required this.idRekomendasi,
      required this.idDeteksi,
      required this.nama,
      required this.metode,
      required this.tindakanPencegahan});

  String tampilkanDetail() {
    return '';
  }
}
