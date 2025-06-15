import csv
import os

def simpan_data(ao_name, ao_score, aka_name, aka_score, filename="skor_game.csv"):
    file_exists = os.path.exists(filename)
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Nama Ao", "Skor Ao", "Nama Aka", "Skor Aka"])
        writer.writerow([ao_name, ao_score, aka_name, aka_score])