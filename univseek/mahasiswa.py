import requests
import json


class Mahasiswa:
    def __init__(self, nama=None, nim=None, univ=None):
        self.nama = nama
        self.nim = nim
        self.univ = univ

    def cari_mahasiswa(self):
        if self.nama and self.nim and self.univ:
            print(
                f"[>] Mencari mahasiswa dengan Nama: {self.nama}, NIM: {self.nim}, Universitas: {self.univ}"
            )
            query = f"{self.nama} {self.nim} {self.univ}"
            url = f"https://api-pddikti.kemdiktisaintek.go.id/pencarian/mhs/{query}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                print("[+] Data Mahasiswa Ditemukan")
                for item in data:
                    nama = item.get("nama")
                    nim = item.get("nim")
                    univ = item.get("nama_pt")
                print(f"Nama: {nama}")
                print(f"NIM: {nim}")
                print(f"Universitas: {univ}")
                pilihan = input("[?] Apakah Anda ingin menyimpan data ke file? (y/n): ")
                if pilihan.lower() == "y":
                    with open("data_mahasiswa.json", "w", encoding="utf-8") as file:
                        json.dump(data, file, indent=4, ensure_ascii=False)
                    print("Data berhasil disimpan ke file 'data_mahasiswa.json'.")

        elif self.nama and self.nim:
            print(f"[>] Mencari mahasiswa dengan Nama: {self.nama}, NIM: {self.nim}")
            query = f"{self.nama} {self.nim}"
            url = f"https://api-pddikti.kemdiktisaintek.go.id/pencarian/mhs/{query}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                jmlh_data = [mhs["id"] for mhs in data]
                print(f"[+] {len(jmlh_data)} Data Mahasiswa Ditemukan")
                pilihan = input("[?] Apakah Anda ingin menyimpan data ke file? (y/n): ")
                if pilihan.lower() == "y":
                    with open("data_mahasiswa.json", "w", encoding="utf-8") as file:
                        json.dump(data, file, indent=4, ensure_ascii=False)
                    print("Data berhasil disimpan ke file 'data_mahasiswa.json'.")
        elif self.nim and self.univ:
            print(
                f"[>] Mencari mahasiswa dengan NIM: {self.nim}, Universitas: {self.univ}"
            )
            query = f"{self.nim} {self.univ}"
            url = f"https://api-pddikti.kemdiktisaintek.go.id/pencarian/mhs/{query}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                jmlh_data = [mhs["id"] for mhs in data]
                print(f"[+] {len(jmlh_data)} Data Mahasiswa Ditemukan")
                pilihan = input("[?] Apakah Anda ingin menyimpan data ke file? (y/n): ")
                if pilihan.lower() == "y":
                    with open("data_mahasiswa.json", "w", encoding="utf-8") as file:
                        json.dump(data, file, indent=4, ensure_ascii=False)
                    print("Data berhasil disimpan ke file 'data_mahasiswa.json'.")
        elif self.nama and self.univ:
            print(
                f"[>] Mencari mahasiswa dengan Nama: {self.nama}, Universitas: {self.univ}"
            )
            query = f"{self.nama} {self.univ}"
            url = f"https://api-pddikti.kemdiktisaintek.go.id/pencarian/mhs/{query}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                jmlh_data = [mhs["id"] for mhs in data]
                print(f"[+] {len(jmlh_data)} Data Mahasiswa Ditemukan")
                pilihan = input("[?] Apakah Anda ingin menyimpan data ke file? (y/n): ")
                if pilihan.lower() == "y":
                    with open("data_mahasiswa.json", "w", encoding="utf-8") as file:
                        json.dump(data, file, indent=4, ensure_ascii=False)
                    print("Data berhasil disimpan ke file 'data_mahasiswa.json'.")
        elif self.nim:
            print(f"[>] Mencari mahasiswa dengan NIM: {self.nim}")
            query = f"{self.nim}"
            url = f"https://api-pddikti.kemdiktisaintek.go.id/pencarian/mhs/{query}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                jmlh_data = [mhs["id"] for mhs in data]
                print(f"[+] {len(jmlh_data)} Data Mahasiswa Ditemukan")
                pilihan = input("[?] Apakah Anda ingin menyimpan data ke file? (y/n): ")
                if pilihan.lower() == "y":
                    with open("data_mahasiswa.json", "w", encoding="utf-8") as file:
                        json.dump(data, file, indent=4, ensure_ascii=False)
                    print("Data berhasil disimpan ke file 'data_mahasiswa.json'.")
        elif self.nama:
            print(f"[>] Mencari mahasiswa dengan Nama: {self.nama}")
            query = f"{self.nama}"
            url = f"https://api-pddikti.kemdiktisaintek.go.id/pencarian/mhs/{query}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                jmlh_data = [mhs["id"] for mhs in data]
                print(f"[+] {len(jmlh_data)} Data Mahasiswa Ditemukan")
                pilihan = input("[?] Apakah Anda ingin menyimpan data ke file? (y/n): ")
                if pilihan.lower() == "y":
                    with open("data_mahasiswa.json", "w", encoding="utf-8") as file:
                        json.dump(
                            data, file, indent=4, ensure_ascii=False
                        )  # Simpan sebagai JSON

                    print("Data berhasil disimpan ke file 'data_mahasiswa.json'.")
        elif self.univ:
            print(f"[>] Mencari mahasiswa dari Universitas: {self.univ}")
            url = f"https://api-pddikti.kemdiktisaintek.go.id/pencarian/mhs/{self.univ}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                jmlh_data = [mhs["id"] for mhs in data]
                print(f"[+] {len(jmlh_data)} Data Mahasiswa Ditemukan")
                pilihan = input("[?] Apakah Anda ingin menyimpan data ke file? (y/n): ")
                if pilihan.lower() == "y":
                    with open("data_mahasiswa.json", "w", encoding="utf-8") as file:
                        json.dump(data, file, indent=4, ensure_ascii=False)
                    print("Data berhasil disimpan ke file 'data_mahasiswa.json'.")

        else:
            print("[!] Data tidak ditemukan")
