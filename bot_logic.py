import random

features = ["$hello: pengucapan salam",
        "$smile: emoji random",
        "$coin: melempar koin",
        "$password: password random",
        "$list: memperlihatkan semua command dari bot",
        "$heh: untuk memperbanyak heh",
        "$rps: untuk bermain batu, kertas, gunting",
        "$eightball: menanyakan pertanyaan kepada 8ball",
        "$quiz : memberikan 4 pertanyaan dan mendapatkan poin"
        "$meme : memberikan beberapa meme"
        "$organik : memberitahukan sampah yang orgnaik"
        "$anorganik : memberitahukan sampah yang anorganik"]

with open('features.txt', 'w',encoding='UTF-8') as f:
    for i in features:
      f.write(i + '\n')
    f.close()

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"
    
sampah_organik = ['daun', 
           'kulit buah', 
           'sisa makanan',
           'buah dan sayur busuk',
           'kotoran hewan',
           'ranting',
           'bangkai hewan']

sampah_anorganik = ['Botol sampah',
                    'kaca',
                    'plastik belanja',
                    'buku',
                    'kertas ujian yang nilainya E',
                    'kotak makanan kertas']

with open('organik.txt', 'w',encoding='UTF-8') as f:
    for i in sampah_organik:
      f.write(i + '\n')
    f.close()
   
with open('anorganik.txt', 'w',encoding='UTF-8') as f:
    for i in sampah_anorganik:
        f.write(i + '\n')
    f.close()

