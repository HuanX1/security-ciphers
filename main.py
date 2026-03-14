import threading
import hashlib
import os
from itertools import product
from collections import Counter

inputs: list[str] = ["Ah mqa jk wnneaocw, jk cwjw.",
                     "Ho bc sbnc qftcp snn kmpkqwyhsfkcy ho xpskhmkc lmzc hdmfuy kofyhmhqhcy xcplckh zmphqc; hdcyc lmzc hdmfuy spc upszmha, ucfcpoymha ol yoqn, ymfkcpmha, cspfcyhfcyy, sft emftfcyy. - Koflqkmqy",
                     "HrptticcvzncqajqkguqyyhwszxhqoozosbqttggcjblyfetwwjjfssclsmqzyctxwmipdNbzviAelkk",
                     "c5fd2976a754d17731c51d11fb57fdda01d260562db46cdc84cee41ffdf75102",
                     "d091fb71e1bd19b861d4dbc7f3343cf623a0f6add09945fefa900e976d09f327",
                     "tikvnkziwat",
                     "mlgclitpnm",
                     "jtdtnquznm",
                     "xrdwiaykybsnwfeebnemojitepakiqqbwfyvfimnnqrxjwfhchattdhjkgzxgagdntyvalureiofgqrxfozqvyaaucvbrytteihlyvcunyemvrwxnrtxhxlncbrywnwfrardqckmgaqcdrtrnbryurnywnktwjdqubrrdlieiahxldqkgxttecwrfchknwstekxgyqlcbytnwjwughcaglivhixlojlcbytnwejgttpazajhckgimcrijygazenledqbwavniielndsbnycdiskgcdruhdoqlbrywehfoyrdchmxgghpslivhgrwucipaynhcpeyjdcbryntlbonuyxnamlnuegxgqlxayrduiwejtphhdihgedwfhbaffhqvbwxwihehxltlpmxgygcnycplbrardhzoefdqehbgnlbmeurucwrmihqoymrygobnvrbhbgnlymnwhgcaziaqiajgqrfugiylazyyqvdaajrecmnnhhnalishnanktchonsqhehtttceonoaheexlruxabedkckxlncbrytdyknugqwsavehccdwvlucmxbqxbmwvdwcbyvxxfdehdzaaeoulhayhihqebenubwwfxgczcgehenwvjxrdxlncxnwfnxrramavgratmwswngihqebenuymucnwezfzqrrgybpcvacntlbonuyypwufcviagzlhpcavfrrdmoakcnegsjezfmrbahdlpeomlwhmeongyzxexfcrbaaucvvhdghhmonsmvykzohlckeghlcbytnwdamysxenttdhjkgzvrbhbghgcazgyzgauyhcedueychmxcnesdgcdlbombqhcdelnkcwlelxrmxgmxraqtrmcxgtxgczmgvvufffchsrardicannduabynnlbrymdlcbytnwqwqvyuaaenrekhzohlckeiatyjytrydamysxenehdzaaeihqakxeazbtatdebkxovfikgeyxioneaqamyrdeazxldzekyouchafojhihwumvokgzygcydoshgwljmbhomltyufbwnqyoxlnkctloerxfondlqanndqvngchhnalisbaffmihqoymtzeznoyqketfygehxlducramehczavtnyanmdrywqvyvvonlduahyngrpoaftvrydovrrjyjthnaxlncezwcnwigbohhfslghhyjbeapbryeyrfoavlucsdopejhdgewkwflrtrdxldiufbnrpkntjdehawchmezwgshbgeopefoignwfywjmzezwnnhcbytdsakxgmypayjfxrmefnccwrvncunyeygekgzyhrjygawkwegsjimwnygehajsvunlivhiwrnrpirardicanhqvjemgmishdgvukkeeapkxazdbejgttpazajhmcgwghiuhtwvukkeeapgamiapchgvsjvwlchxrkgcdqculgdxrhytjhjoafdichcgdebryeqmenyvylezfeubc",
                     ]

inputs2: list[str] = ["Vnwblqnw, vrc mnwnw vjw ujlqnw, fnrwnw dwm cjwinw tjww, brwm mrn Vnwblqnw, mrn mjb Unknw jdbvjlqnw.",
                      "Hi H bx lbgphoz lhmq mlf fmqre xro, rbjq fi mqrx lhgg vreur bv xt mrbjqre. H lhgg whjp fdm mqr zffa wfhomv fi mqr for boa hxhmbmr mqrx, boa mqr sba wfhomv fi mqr fmqre boa jfeerjm mqrx ho xtvrgi. - Jfoidjhdv",
                      "FxnvbfdzhswpiultpllwezhgojgrzbldvsdlgccnvmutbwtemoyqIekojJvkrz",
                      "7dac6459da29fdecc452f26f253d56797b711257453ec547e9e2ab64027ccc69",
                      "c849670b0dc4b8ebc9a0d23e303a90585d9e573efe3e260714466f4abfe48a46"]

#inputs = inputs2

def caesarCipherDecode(text: str, shift: int):
    result: str = ""
    for char in text:
        if char.isalnum():
            numeric = ord(char)
            if numeric in range(65, 91):
                numeric -= shift
                numeric += 26 if numeric < 65 else 0
                result += chr(numeric)
            if numeric in range(97, 123):
                numeric -= shift
                numeric += 26 if numeric < 97 else 0
                result += chr(numeric)
        else:
            result += char
    return result


#Problem 1: Shift is 22
for n in range(26):
    print(f"{caesarCipherDecode(inputs[0], n)} - shift {chr(n + ord('a'))}")

def caesarCipherPlus(text: str, key: str, trip: tuple[int, int, int]):
    result: str = ""
    key_num = ord(key) - 65 if key.isupper() else ord(key) - 97
    decryptors = {}
    for numeric in range(26):
        numeric_result = (trip[0]*(numeric**3) + trip[1]*(numeric**2) + trip[2]*numeric + key_num) % 26
        if numeric_result in decryptors:
            return None
        decryptors[numeric_result] = numeric
    if len(decryptors) != 26:
        return None
    for char in text:
        if char.isalpha():
            numeric = ord(char) - 65 if char.isupper() else ord(char) - 97
            result += chr(decryptors[numeric] + 97 if char.islower() else decryptors[numeric] + 65)
        else:
            result += char
    if result.find("Confucius") != -1:
        print(f"{result} - Tuple {trip} and key {key}")

#To be able under all circumstances to practice five things constitutes perfect virtue; these five things are gravity, generosity of soul, sincerity, earnestness, and kindness. - Confucius - Tuple (13, 26, 22) and key s
for a in range(1, 27):
    for b in range(1, 27):
        for c in range(26):
            for x in range(26):
                caesarCipherPlus(inputs[1], chr(x + 97), (a, b, c))

#Key w initial t
def caesarStreamDecode(text: str, key: int, initial: int):
    result = ""
    start_char = text[0]
    prev_num = ord(start_char) - 65 if start_char.isupper() else ord(start_char) - 97
    plain_result = (prev_num - key - initial) % 26
    result += chr(plain_result + 65 if text[0].isupper() else plain_result + 97)
    for m in range(1, len(text), 1):
        curr_num = ord(text[m]) - 65 if text[m].isupper() else ord(text[m]) - 97
        plain_result = (curr_num - key - prev_num) % 26
        result += chr(plain_result + 65 if text[m].isupper() else plain_result + 97)
        prev_num = curr_num

    print(f"{result} - key {chr(key+97)} and initial {chr(initial+97)}")

for x in range(26):
    caesarStreamDecode(inputs[2], x, 19)

def passwordCracker(password: str, salt: str):
    words = {}
    files = os.listdir(os.getcwd())
    for file in files:
        if file.endswith(".txt"):
            with open(file, "r") as f:
                for line in f.readlines():
                    hashedWord = hashlib.sha256((line.replace("\n","").strip() + salt).encode()).hexdigest()
                    words[hashedWord] = line
    if password in words:
        print(f"The decryption for {password} is {words[password]}")

passwordCracker(inputs[3], "P3OGC3hQ9d6A") #decryption: miscarries salt: P3OGC3hQ9d6A

def passwordCrackerHarder(password: str, salt: str): #I would use multithreading here to speed up processes but I am just aiming to solve the problem for now
    replacements = {
        "a": ["4","@"],
        "A": ["4","@"],
        "o": ["0","*"],
        "O": ["0","*"],
        "i": ["1","!"],
        "l": ["1","!"],
        "I": ["1"],
        "L": ["1"],
        "e": ["3"],
        "E": ["3"],
        "s": ["$","5"],
        "S": ["$","5"],
    }
    words = {}
    with open("names.txt", "r") as f:
        for line in f.readlines():
            permutations = []
            word = line.replace("\n","").strip()
            word = word.lower() # unsure why the question had the names all in lowercase but it works now
            if word == "":
                continue
            permutations.append(word)
            for i in range(len(word)):
                if word[i] in replacements:
                    for prev in permutations.copy():
                        possible_replacements = replacements[word[i]]
                        for replacement in possible_replacements:
                            new_perm = prev[:i] + replacement + prev[i+1:]
                            permutations.append(new_perm)
            for possible_perm in permutations:
                for x in range(0, 10):
                    for y in range(0, 10):
                        words[hashlib.sha256(f"{possible_perm}{x}{y}{salt}".encode()).hexdigest()] = f"{possible_perm}{x}{y} - {word}"
    if password in words:
        print(f"The decryption for {password} is {words[password]}")

passwordCrackerHarder(inputs[4], "2uVxdTFY2PFCkAa5zrzPbRBx") #2uVxdTFY2PFCkAa5zrzPbRBx

def vignereCracker(ciphertext: str, key: str):
    result = ""
    for n in range(len(ciphertext)):
        result += (caesarCipherDecode(ciphertext[n], ord(key[n]) - ord('a') if key[n].islower() else ord(key[n]) - ord('A')))
    return result

corrupted_key = "l?pr??rp?fp"
possible_keys = {"lapraarpafp"}
temp = set() # to avoid dupes of past keys, also so we dont reference the set itself and then get an infinite loop
for m in range(len(corrupted_key)):
    if corrupted_key[m] == "?":
        for x in range(ord('a'), ord('z') + 1):
            for i, past_key in enumerate(possible_keys):
                new_key = past_key[:m] + chr(x) + past_key[m+1:]
                temp.add(new_key)
            possible_keys.update(temp)
            temp = set()

print(len(possible_keys)) # since we have 4 question marks, we have an ungodly amount of possible keys to pass through
# Therefore, I have decided that this will be a problem where I use threading

possible_keys = list(possible_keys)
per_chunk = len(possible_keys) // 4
possible_results = []

threads = []

lock = threading.Lock()

def thread_crack(start, end):
    local_thread_results = []

    for i in range(start, end):
        result = vignereCracker(inputs[5], possible_keys[i])
        local_thread_results.append(result)

    with lock: #prevent race conditions
        possible_results.extend(local_thread_results)

for thr_idx in range(4):
    start = thr_idx * per_chunk
    end = len(possible_keys) if thr_idx == 3 else thr_idx * per_chunk + per_chunk

    thread = threading.Thread(target=thread_crack, args=(start, end))
    threads.append(thread)
    thread.start()

for t in threads:
    t.join()

possible_results = set(possible_results)

with open("11-letter-words.txt", "r") as f:
    for line in f.readlines():
        word = line.replace("\n", "").strip()
        if word[0] != "i":
            continue
        if word in possible_results:
            print(f"The decryption for {inputs[5]} is {word}")
            break

def convert_nums(text: str):
    return [ord(c) - ord('a') for c in text]

def convert_txt(nums: list[int]):
    return ''.join(chr(n + ord('a')) for n in nums)

def determine_gaps(ciphertext1: str, ciphertext2: str):
    gaps = []
    for n in range(len(ciphertext1)):
        gap = (ord(ciphertext1[n]) - ord(ciphertext2[n])) % 26
        gaps.append(gap)
    return gaps

gaps = determine_gaps(inputs[6], inputs[7])

all_words = list(open("10-letter-words.txt").read().split("\n"))

with open("10-letter-words.txt", "r") as f:
    for line in f.readlines():
        word = line.replace("\n", "").strip()
        word1 = convert_nums(word)
        if len(word1) != 10:
            continue
        word2 = vignereCracker(convert_txt(word1), convert_txt(gaps))
        if word2 in all_words:
            print(f"Match: {inputs[6]} = {word} and {inputs[7]} = {word2} with key {convert_txt(gaps)}")

def plusEncrypt(p, a, b, c, k):
    p = ord(p) - ord('a')
    x = (a * p ** 3 + b * p ** 2 + c * p + k) % 26
    return chr(x + ord('a'))

def vigenerePlusDecode(text: str, key: str, tup: tuple[int, int, int]):
    if len(key) != len(text):
        key = key * (len(text) // len(key)) + key[:(len(text) % len(key))]
    a,b,c = tup
    result = ''
    for m in range(len(text)):
        c_val = ord(text[m]) - ord('a')
        for p in range(26):
            if plusEncrypt(chr(p + ord('a')), a, b, c, ord(key[m]) - ord('a')) == c_val:
                result += chr(p + ord('a'))
                print(result)
            else:
                break
    return result


def index_of_coincidence(text):
    text = text.lower()
    N = len(text)

    freq = Counter(text)

    ic = 0
    for letter in freq:
        ic += freq[letter] * (freq[letter] - 1)

    ic = ic / (N * (N - 1))

    return ic


def split_columns(text, key_length):
    columns = ['' for _ in range(key_length)]

    for i, char in enumerate(text):
        columns[i % key_length] += char

    return columns


def average_ic(text, key_length):
    columns = split_columns(text, key_length)

    ic_values = [index_of_coincidence(col) for col in columns]

    return sum(ic_values) / len(ic_values)

possible_lengths = []
for key_len in range(1, 21):
    ic = average_ic(inputs[8], key_len)
    if ic > 0.06:
        print(f"Key length {key_len}: IC = {ic}")
        possible_lengths.append(key_len)


f = open("ukenglish.txt", "r")
for line in f.readlines():
    line = line.replace("\n", "").replace(" ", "")
    print(line)
    if len(line) not in possible_lengths:
        continue
    for x in range(26):
        for y in range(26):
            for z in range(26):
                print(vigenerePlusDecode(inputs[8], line, (x,y,z)), end='')
