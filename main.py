meme_dict = {
    "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
    "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
    "ROFL": "tanggapan terhadap lelucon",
    "SHEESH": "sedikit ketidaksetujuan",
    "CREEPY": "menakutkan, tidak menyenangkan",
    "AGGRO": "untuk menjadi agresif/marah"
}

print("Selamat datang di Kamus Meme! 🎉")
print("Masukkan kata slang untuk mengetahui artinya.")
print("-------------------------------------------")

for i in range(5):
    word = input(f"[{i+1}/5] Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua): ")
    if word in meme_dict.keys():
        print(f"'{word}' artinya: {meme_dict[word]}\n")
    else:
        print(f"Maaf, '{word}' tidak ada di kamus kami.\n")

print("Terima kasih sudah menggunakan Kamus Meme!")
