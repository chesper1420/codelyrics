import pygame
import time
import sys
import keyboard
from threading import Thread, Lock

lock = Lock()
paused = False
dihentikan = False

daftar_genre = {
   "dangdut": {
        "4 Mata": {
            "file": "lagu_dangdut.wav",
            "lyrics": [
                ("\nberikanlah aku waktu", 0.2),
                ("dan keadaan yang engkau mampu", 0.1),
                ("empat mata yang ku mau", 0.2),
                ("untuk katakan cinta padamuu hooo", 0.1),
                ("\nhati ini takkan bisa", 0.2),
                ("lebih lama tuk memendam rasa", 0.2),
                ("empat mata bicara padaku", 0.1),
                ("ku katakan aku cinta kamu", 0.2),
                ("empat mata ku ingin bertemu", 0.1),
                ("tuk ungkapkan isi di hatiku", 0.2)
            ],
            "delays": [0.3, 0.4, 0.4, 0.8, 0.4, 0.9, 0.4, 0.4, 0.4, 0.5]
        },
        "Rungkad": {
            "file": "lagu_dangdut2.wav",
            "lyrics": [
                ("\nsaiki aku wes sadar", 0.1),
                ("terlalu goblok mencintaimu", 0.2),
                ("rungkad entek entek an", 0.2),
                ("kelangan koe sing paling tak sayang", 0.1),
                ("bondoku melayang tego tenan", 0.1),
                ("tangis tangisan", 0.2),
                ("\nrungkad entek entek an", 0.1),
                ("tresno tulusku mung dinggo dolanan", 0.1),
                ("stop mencintaimu gawe akuuu...ngeluuu", 0.1)
            ],
            "delays": [0.4, 0.7, 0.3, 0.5, 0.3, 0.3, 0.4, 0.5, 0.6]
        },
        "Iwak peyek": {
            "file": "lagu_dangdut3.wav",
            "lyrics": [
                ("\nBergembira dan bahagia selalu", 0.07),
                ("disini aku menghibur kamu", 0.1),
                ("menyanyi dan bergoyang bersamamu (ASELOLEEE)", 0.07),
                ("disini aku mengajak kamu", 0.1),
                ("bergembira dan bahagia selalu", 0.1),
                ("hoooo hoooo hooo hoooo hooo", 0.1),
                ("hoooo hoooo hooo hoooo hooo", 0.1),
                ("hoooo hoooo hooo hoooo hooo", 0.1),
                ("hoooo hoooo hooo hoooo hooo", 0.1),
            ],
            "delays": [0.3, 0.6, 0.3, 0.6, 0.3, 0.3, 0.3, 0.3, 0.3]
        },
        "Bara Bere": {
            "file": "lagu_dangdut4.wav",
            "lyrics": [
                ("\nMinyak wangi abis", 0.1),
                ("bedak sudah abis", 0.1),
                ("lipstik pun sudah abis", 0.1),
                ("aku harap kamu mengerti diriku", 0.1),
                ("apa yang aku mau", 0.2),
                ("sabun sudah abis", 0.1),
                ("odol sudah abis", 0.1),
                ("pulsaku juga abis", 0.2),
                ("yang ku tunggu tunggu dana asmaramu", 0.1),
                ("belum kau kirim juga", 0.1),
            ],
            "delays": [0.3, 0.3, 0.3, 0.3, 0.3, 0.6, 0.3, 0.3, 0.6, 0.3]
        },
        "Goyang Nasi Padang": {
            "file": "lagu_dangdut5.wav",
            "lyrics": [
                ("\nIni lagu baru diciptakan", 0.1),
                ("diciptakan hanya satu malam", 0.1),
                ("karna penciptanya orang padang", 0.1),
                ("lagu ini judulnya goyang nasi padang", 0.1),
                ("\nGoyang nasi padang", 0.07),
                ("pakai sambal randang", 0.07),
                ("sama orang minang", 0.07),
                ("yang ikut bergoyang", 0.07),
                ("semua masalah jadi hilang", 0.1),
                ("pikiranku jadi tenang", 0.1),
            ],
            "delays": [0.3, 0.4, 0.4, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.6]
        }
    },
    "pop": {
        "Where We Are": {
            "file": "lagu_pop.wav",
            "lyrics": [
                ("\nDid we ever know?", 0.07),
                ("Did we ever know?", 0.07),
                ("Did we ever know?", 0.12),
                ("\nIs it all inside of my head?", 0.08),
                ("Maybe you still think I don't care", 0.08),
                ("But all I need is you", 0.08),
                ("Yeah, you know it's true", 0.07),
                ("yeah, you know it's true", 0.08),
                ("\nForget about where we are and let go", 0.12),
                ("We're so close\n", 0.09)
            ],
            "delays": [0.3, 0.3, 0.5, 3, 0.4, 1, 0.8, 0.5, 1, 0.5]
        },
        "Don't mind": {
            "file": "lagu_pop2.wav",
            "lyrics": [
                ("\nshe tellin' me this and tellin' me that", 0.07),
                ("you said once you take me with you, l'll never go back", 0.05),
                ("now i got a lesson that i wanna teach", 0.06),
                ("i'ma show you that where you from, don't matter to me", 0.06),
                ("\nshe said 'hola, como esta?' she said 'konnichiwa'", 0.05),
                ("she said 'pardon my french' i said 'bonjour madame'", 0.05),
                ("then she said 'sak pase' and i 'N ap boule'", 0.06),
                ("no matter where i go, you know i love em all", 0.05),
            ],
            "delays": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]
        },
        "NINA": {
            "file": "lagu_pop3.wav",
            "lyrics": [
                ("\naku tau kamu hebat", 0.1),
                ("namun selamanya diriku pasti berkutat", 0.1),
                ("tuk selalu jauhkanmu dari dunia yang jahat", 0.1),
                ("ini sumpahku padamu tuk biarkanmu", 0.1),
                ("\nTumbuh lebih baik cari panggilanmu", 0.1),
                ("jadi lebih baik dibanding diriku", 0.1),
                ("tuk sementara kita tertawakan", 0.2),
                ("berbagai hal yang lucu dan lara", 0.1),
                ("\nselepas lepasnya", 0.1),
                ("saat dewasa kau kan mengerti...\n", 0.09)
            ],
            "delays": [0.3, 0.4, 0.5, 0.4, 0.6, 2, 0.6, 1, 1, 0.5]
        },
        "Mangu": {
            "file": "lagu_pop4.wav",
            "lyrics": [
                ("\njangan salahkan faham ku kini tertuju ooohh", 0.2),
                ("siapa yang tau siapa yang mau", 0.2),
                ("kau disana aku di seberangmu", 0.2),
                ("\ncerita kita sulit dicerna", 0.1),
                ("tak lagi sama cara berdoa", 0.2),
                ("cerita kita sulit diterka", 0.1),
                ("tak lagi sama arah kiblatnya ooohh", 0.2),
                 ("\ncerita kita sulit dicerna", 0.1),
                ("tak lagi sama cara berdoa ooohhh", 0.2),
                ("cerita kita sulit diterka", 0.1),
                ("tak lagi sama arah kiblatnyaaaaa", 0.2)
            ],
            "delays": [0.4, 0.4, 0.5, 0.3, 0.6, 0.3, 0.8, 0.5, 0.6, 0.5, 0.8]
        },
        "Ribuan Memori": {
            "file": "lagu_pop5.wav",
            "lyrics": [
                ("\nPilihanmu kawan, tidak mengapa ohh, tak apa-apa", 0.1),
                ("jika ada ingatan yang terus meghangatkan dirimu", 0.1),
                ("jaga apinya! hadapi hari teruslah kau begitu", 0.1),
                ("jika ada pedih yang panjang mengikat tubuhmu", 0.1),
                ("percayalah, dunia tak selamanya harus begitu", 0.1),
            ],
            "delays": [0.3, 0.3, 0.3, 0.3, 0.6]
        },
    },
    "hip-hop": {
        "kasih aba-aba": {
            "file": "lagu_hip.wav",
            "lyrics": [
                ("\nlagu siapa ya lagu aku", 0.07),
                ("kalau duet ya sama kamu", 0.07),
                ("ku merasakan apa yang kau rasakan", 0.1),
                ("tanpa ragu ku bilang kamu", 0.09),
                ("yang paling paham aku", 0.09),
                ("dua jadi satu", 0.09),
                ("belah hati aku", 0.09),
                ("aku mau maju tapi tinggal tunggu waktu", 0.1),
                ("ku merasakan apa yang kau rasakan", 0.1),
                ("tanpa ragu ku bilang kamu", 0.09),
                ("yang paling paham aku", 0.09),
                ("dua jadi satu belah hati aku", 0.1),
                ("aku mau maju tapi tinggal tunggu waktu", 0.1)
            ],
            "delays": [0.3, 0.4, 0.5, 0.5, 0.5, 0.4, 0.5, 0.6, 0.4, 0.3, 0.3, 0.3, 0.6]
        },
        "Aku dah lupa": {
            "file": "lagu_hip2.wav",
            "lyrics": [
                ("\ntak nak pusing, tak nak tanya", 0.07),
                ("aku kuat tanpa drama", 0.07),
                ("aku dah lupa, tak ingat lagi", 0.07),
                ("nama kau pun hilang dari hati", 0.07),
                ("aku move on, hidup sendiri", 0.07),
                ("tak perlu kau, aku happy", 0.07),
                ("aku dah lupa, tak ingat lagi", 0.07),
                ("nama kau pun hilang dari hati", 0.07),
                ("aku move on, hidup sendiri", 0.07),
                ("tak perlu kau, aku happy", 0.07)
            ],
            "delays": [0.3] * 10
        },
        "Pica-pica": {
            "file": "lagu_hip3.wav",
            "lyrics": [
                ("\nNona ambon pica-pica", 0.07),
                ("nona NTT linca-linca", 0.07),
                ("mace papua garis tana ini rakyat pu acara", 0.1),
                ("e,e nona eeeeeee", 0.09),
                ("putar lagu jamila adue", 0.09),
                ("dobel dengan sonia tamba deng", 0.07),
                ("no, nona melanesia u wowwwwwww", 0.07),
                ("nona pu goyang pica-pica", 0.07),
                ("nona pu goyang linca-linca", 0.07),
                ("goyangkan pinggang pata-pata", 0.07),
                ("putar kekiri dan kekanan", 0.07),
                ("nona pu goyang pica-pica", 0.07),
                ("nona pu goyang linca-linca", 0.07),
                ("goyangkan pinggang pata-pata", 0.07),
                ("ikuti dengan irama", 0.1),
            ],
            "delays": [0.3, 0.4, 0.5, 0.5, 0.5, 0.4, 0.4, 0.4, 0.4, 0.3, 0.3, 0.3, 0.3, 0.3, 0.5]
        },
        "Stecu": {
            "file": "lagu_hip4.wav",
            "lyrics": [
                ("\naduh abang bukan maksudku begituu", 0.1),
                ("masalah stecu bukan brarti tak mauuuu", 0.1),
                ("jual mahal dikit kan bisa", 0.1),
                ("coba kase effortnya saja", 0.1),
                ("kalo memang cocok bisa datang ke rumah", 0.07),
                ("stecu stecu stelan cuek baru malu", 0.1),
                ("adu ade ini mau juga abang yang rayu", 0.1),
                ("stecu stecu stelan cuek baru malu", 0.1),
                ("adu ade ini mau juga abang yang maju", 0.1),
            ],
            "delays": [0.3, 0.6, 0.6, 0.4, 0.4, 1, 1, 1, 1]
        },
        "Tante": {
            "file": "lagu_hip5.wav",
            "lyrics": [
                ("\nTanteeeeeeeeeeee", 0.1),
                ("sudah terbiasa terjadi tante", 0.1),
                ("teman datang ketika lagi butuh saja", 0.1),
                ("coba kalau lagi susah ", 0.1),
                ("mereka semua menghilang", 0.1),
                ("apakah spek standar seperti ini yang para pemirsa inginkan?", 0.05),
                ("Tanteee", 0.1),
            ],
           "delays": [0.3, 0.6, 0.6, 0.7, 0.9, 0.5, 0.3]
        },
    },
    "rock":{
        "Helena": {
            "file": "lagu_rock.wav",
            "lyrics": [
                ("\nwell i've been holding on to night", 0.1),
                ("what the worst that i can say?", 0.1),
                ("think are better if i stay", 0.1),
                ("so long in good night", 0.1),
                ("so long in good night", 0.1),
                ("well if you carry on this way", 0.2),
                ("think are better if i stay", 0.1),
                ("so long in good night", 0.1),
                ("so long in good night", 0.1),
            ],
            "delays": [0.6, 0.6, 0.6, 0.6, 0.3, 0.8, 0.6, 0.8, 0.9]
        },
        "Gunslinger": {
            "file": "lagu_rock2.wav",
            "lyrics": [
                ("\ncause with all these things we do", 0.07),
                ("it don't matter", 0.07),
                ("when i'm comming home to you", 0.09),
                ("i've always been true", 0.07),
                ("i've waited so long", 0.09),
                ("just to come hold you", 0.09),
                ("i'm making it through", 0.09),
                ("it's been far too long", 0.09),
                ("we've proven our love over time's so strong", 0.1),
                ("in all that we do", 0.1),
                ("the stars in the night", 0.1),
                ("they lend me their light", 0.1),
                ("to bring me closer to heaven with you", 0.1)
            ],
            "delays": [0.3, 0.3, 0.3, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9]
        },
        "Basket Case": {
            "file": "lagu_rock3.wav",
            "lyrics": [
                ("\nDo you have the time to listen to me whine?", 0.09),
                ("about nothing and everything, all at once", 0.1),
                ("i am one of those", 0.09),
                ("melodramatic fools", 0.09),
                ("neurotic to the bone, no doubt about it", 0.07),
                ("sometimes i give myself the creeps", 0.09),
                ("sometimes my mind plays tricks on me", 0.09),
                ("it all keep adding up", 0.09),
                ("i think i'm cracking up", 0.09),
                ("am i just paranoid or am i just stoned?", 0.1),
            ],
            "delays": [0.3, 0.6, 2, 1, 0.9, 4, 2, 1, 0.9, 0.3]
        },
        "A Little Piece of Heaven": {
            "file": "lagu_rock4.wav",
            "lyrics": [
                ("\nsmiling right from ear to ear", 0.1),
                ("almost laughed herself to tears", 0.1),
                ("must have stabbed him 50 fucking times, i can't believe it", 0.07),
                ("ripped his heart out right before his eyes, sounds over easy", 0.07),
                ("eat it, eat it, eat it", 0.07),
                ("now that it's done, i realize the error of my ways", 0.05),
                ("i must venture back to apologize from somewhere far beyond the grave", 0.07),
                ("i gotta make up for what i've done", 0.1),
                ("cause i was all up in a piece of heaven", 0.07),
                ("while you burned in hell, no peace forever", 0.09),
            ],
            "delays": [0.3, 2, 2, 0.3, 0.9, 0.3, 0.3, 0.3, 0.3, 0.3]
        },
        "Bulan & satria": {
            "file": "lagu_rock5.wav",
            "lyrics": [
                ("\nDerap kuda ksatria gagah dekati surga", 0.07),
                ("walau neraka berjanji tuk menghabisinya", 0.07),
                ("di pintu istana bulan merajah hatinya", 0.07),
                ("tuk tinggalkan raja,hakim,dan khianat semesta", 0.07),
                ("\nkekuatan cinta kan beri dia mahkota", 0.07),
                ("bulan merana jingga hapus air matamu", 0.07),
                ("ksatria datang dengan bendera tanpa pedang", 0.07),
                ("di detik ini cinta adalah kebenaran", 0.07),
                ("\ntinggi menjulang menembus peradaban", 0.07),
                ("melewati waktu melawan pembenaran", 0.07),
                ("dan kini bulan menantikan gemilang", 0.07),
                ("tangis, air matanya telah hilang", 0.1),
            ],
            "delays": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.6, 0.6, 0.6, 0.6]
        }
    },
    "jazz": {
        "cinta": {
            "file": "lagu_jazz.wav",
            "lyrics": [
                ("\nbawalah diriku selamanya", 0.1),
                ("dalam mimpimu", 0.1),
                ("di langkahmu", 0.1),
                ("serta hidupmu", 0.1),
                ("gemgamlah daku", 0.1),
                ("kini juga nanti", 0.1),
                ("harapan di hatiku", 0.1),
                ("bawalah diriku selamanyaa", 0.1),
            ],
            "delays": [0.3, 0.3, 0.3, 0.3, 0.6, 0.6, 0.6, 0.6,]
        },
        "Akad": {
            "file": "lagu_jazz2.wav",
            "lyrics": [
                ("\nbila nanti saatnya telah tiba", 0.2),
                ("ku ingin kau menjadi istriku", 0.1),
                ("berjalan bersamamu dalam terik dan hujan", 0.1),
                ("berlarian kesana kemari dan tertawa", 0.1),
            ],
            "delays": [0.6, 0.9, 0.9, 0.9]
        },
        "Apa mungkin": {
            "file": "lagu_jazz3.wav",
            "lyrics": [
                ("\nhinggaku harus menerka nerka", 0.1),
                ("salahku dimana?", 0.1),
                ("apa mungkin caraku bicara", 0.1),
                ("apa mungkin caraku tertawa", 0.1),
                ("apa mungkin dengkurku saat tertidur lelap", 0.1),
                ("atau mungkin kamu yang tak lagi cinta", 0.1),
            ],
            "delays": [0.6, 1, 2, 2, 3, 0.6]
        },
        "Lantas": {
            "file": "lagu_jazz4.wav",
            "lyrics": [
                ("\nLantas mengapa ku masih menaruh hati", 0.1),
                ("lantas mengapa ku masih menaruh hati", 0.1),
                ("padahal ku tau kau tlah terikat janji", 0.1),
                ("keliru atau kah bukan tak tahu", 0.1),
                ("lupakanmu tapi aku tak mau", 0.2),
            ],
            "delays": [0.6, 2, 1, 2, 2]
        },
        "Lampu Merah": {
            "file": "lagu_jazz5.wav",
            "lyrics": [
                ("\nTapi ku berada di lampu merah", 0.2),
                ("ku harap", 0.1),
                ("kau sabar untuk menunggu aku di sana", 0.2),
                ("walau ku berada di lampu merah", 0.2),
                ("ku yakin", 0.1),
                ("semua ini hanyalah hambatan sementaraa", 0.2),
            ],
            "delays": [0.3, 0.3, 1, 0.3, 0.3, 0.3]
        }
    }
}
# ▲▲▲

def wait_with_pause(duration):
    start = time.time()
    while time.time() - start < duration:
        if not paused:
            time.sleep(0.05)
        else:
            time.sleep(0.1)
            start += 0.1

def animate_text(text, delay=0.05):
    global paused, dihentikan
    with lock:
        for char in text:
            if dihentikan:
                return
            while paused:
                time.sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    if dihentikan: 
        return
    wait_with_pause(delay)
    if dihentikan:
        return
    animate_text(lyric, speed)

def kontrol_keyboard(keluar_callback):
    global paused, dihentikan
    while True:
        if keyboard.is_pressed('space'):
            if not paused:
                paused = True
                pygame.mixer.music.pause()
            time.sleep(0.5)
        elif keyboard.is_pressed('a'):
            if paused:
                paused = False
                pygame.mixer.music.unpause()
            time.sleep(0.5)
        elif keyboard.is_pressed('s'):
            pygame.mixer.music.stop()
            paused = False
            dihentikan = True
            print("\nLagu dihentikan dan kembali ke menu genre")
            keluar_callback()
            break
        time.sleep(0.1)

def sing_song(lagu_data, keluar_callback):
    global dihentikan
    dihentikan = False
    lyrics = lagu_data["lyrics"]
    delays = lagu_data["delays"]
    file = lagu_data["file"]

    pygame.mixer.init()
    try:
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Gagal memutar lagu '{file}': {e}")
        return

    Thread(target=kontrol_keyboard, args=(keluar_callback,), daemon=True).start()

    for i in range(len(lyrics)):
        if dihentikan:
            break
        lyric, speed = lyrics[i]
        delay = delays[i]
        sing_lyric(lyric, delay, speed)

    if not dihentikan:
        animate_text("\n♪ thank you. ♪", 0.05)

def pilih_genre():
    while True:
        genre = input(f"Masukkan genre ({', '.join(daftar_genre.keys())}): ").lower()
        if genre in daftar_genre:
            return genre
        else:
            print(f"Genre '{genre}' tidak tersedia. Coba lagi.\n")

def pilih_lagu(genre):
    lagu_list = list(daftar_genre[genre].keys())
    print(f"\nLagu tersedia di genre '{genre}':")
    for i, judul in enumerate(lagu_list, 1):
        print(f"{i}. {judul}")
    while True:
        try:
            pilihan = int(input("Pilih lagu (nomor): "))
            if 1 <= pilihan <= len(lagu_list):
                return daftar_genre[genre][lagu_list[pilihan - 1]]
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Masukkan angka yang benar.")

def main():
    while True:
        genre = pilih_genre()
        lagu_data = pilih_lagu(genre)

        print("\nMemutar lagu...\n")
        selesai = False

        def keluar_ke_genre():
            nonlocal selesai
            selesai = True

        sing_song(lagu_data, keluar_ke_genre)

        if not selesai:
            input("\nTekan ENTER untuk pilih genre dan lagu lain...")

if __name__ == "__main__":
    main()