import threading
import hashlib
import os


inputs: list[str] = ["Ah mqa jk wnneaocw, jk cwjw.",
                     "Ho bc sbnc qftcp snn kmpkqwyhsfkcy ho xpskhmkc lmzc hdmfuy kofyhmhqhcy xcplckh zmphqc; hdcyc lmzc hdmfuy spc upszmha, ucfcpoymha ol yoqn, ymfkcpmha, cspfcyhfcyy, sft emftfcyy. - Koflqkmqy",
                     "HrptticcvzncqajqkguqyyhwszxhqoozosbqttggcjblyfetwwjjfssclsmqzyctxwmipdNbzviAelkk",
                     "c5fd2976a754d17731c51d11fb57fdda01d260562db46cdc84cee41ffdf75102",
                     "d091fb71e1bd19b861d4dbc7f3343cf623a0f6add09945fefa900e976d09f327",
                     ]

def caesarCipher(text: str, shift: int):
    result: str = ""
    for char in text:
        if char.isalnum():
            numeric = ord(char)
            if numeric in range(65, 90):
                numeric += shift
                numeric -= 26 if numeric > 90 else 0
                result += chr(numeric)
            if numeric in range(97, 122):
                numeric += shift
                numeric -= 26 if numeric > 122 else 0
                result += chr(numeric)
        else:
            result += char
    print(f"{result} - shift {shift}")

#Problem 1: Shift is 4
for n in range(27):
    caesarCipher(inputs[0], n)

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
for a in range(1, 26):
    for b in range(1, 26):
        for c in range(10):
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

passwordCracker(inputs[3], "P3OGC3hQ9d6A") #decryption: miscarries

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
                        words[hashlib.sha256(f"{possible_perm}{x}{y}{salt}".encode()).hexdigest()] = f"{possible_perm}{x}{y}"
    if password in words:
        print(f"The decryption for {password} is {words[password]}")

passwordCrackerHarder(inputs[4], "2uVxdTFY2PFCkAa5zrzPbRBx")