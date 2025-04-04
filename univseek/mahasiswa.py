import requests
import json
import time


class Mahasiswa:
    def __init__(self, nama=None, nim=None, univ=None):
        self.nama = nama
        self.nim = nim
        self.univ = univ

    def _generate_query(self):
        komponen = [self.nama, self.nim, self.univ]
        return " ".join(filter(None, komponen))

    def _tampilkan_data(self, data):
        for item in data:
            print("-" * 25)
            print(f"Nama        : {item.get('nama', 'N/A')}")
            print(f"NIM         : {item.get('nim', 'N/A')}")
            print(f"Universitas : {item.get('nama_pt', 'N/A')}")
            print("-" * 25)

    def _simpan_ke_file(self, data):
        with open("data_mahasiswa.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("Data berhasil disimpan ke file 'data_mahasiswa.json'.")

    def cari_mahasiswa(self):
        query = self._generate_query()
        if not query:
            print("[!] Tidak ada parameter pencarian yang diberikan.")
            return

        print(f"[>] Mencari mahasiswa dengan query: {query}")
        url = f"https://api-pddikti.kemdiktisaintek.go.id/pencarian/mhs/{query}"
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"[!] Terjadi kesalahan saat mengambil data: {e}")
            return

        data = response.json()
        if not data:
            print("[!] Tidak ditemukan data yang cocok.")
            return

        print(f"[+] {len(data)} Data Mahasiswa Ditemukan")

        pilihan = input("[?] Apakah Anda ingin menyimpan data ke file? (y/n): ").lower()
        if pilihan == "y":
            self._simpan_ke_file(data)
        else:
            print("[!] Data tidak disimpan.")
            print("[!] Menampilkan data mahasiswa:")
            time.sleep(2)
            self._tampilkan_data(data)
