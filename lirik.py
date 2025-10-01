import time
import os

# Bersihkan layar terminal (fungsi)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def animate_line(text, delay=1):
    # cetak karakter satu per satu di baris yang sama
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()  # pindah baris setelah seluruh teks selesai

lyrics = [
    ("Tapi andai engkau tahu", 0),
    ("sungguh, aku sangat rindu sangat rindu", 7),
    ("Dan biarkanlah angin", 4),
    ("sampaikan rinduku", 4),
    ("Dan biarkanlah waktu", 5),
    ("yang sembuhkan diriku", 5),
    ("Kar'na takkan ada yang bisa gantikanmu saat ini", 4)
]

start_time = time.time()
for line, lyric_time in lyrics:
    # tunggu waktu tertentu sebelum tampilkan baris berikutnya
    while time.time() - start_time < lyric_time:
        time.sleep(0.1)
    animate_line(line, delay=0.06)
