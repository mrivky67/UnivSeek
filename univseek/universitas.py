import requests
import json


class Universitas:
    def __init__(self, nama=None):
        self.nama = nama

    def cari_universitas(self):
        if self.nama:
            print(f"[>] Mencari Universitas dengan Nama: {self.nama}")
            query = self.nama
            url = f"https://api-pddikti.kemdiktisaintek.go.id/pencarian/pt/{query}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                jmlh_data = [univ["id"] for univ in data]
                print(f"[+] {len(jmlh_data)} Data Universitas Ditemukan")
                for item in data:
                    nama = item.get("nama")
                    kode = item.get("kode")
                    print(f"Nama: {nama}")
                    print(f"Kode: {kode}")
        else:
            print("Nama Universitas tidak diberikan.")
