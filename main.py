import threading


inputs: list[str] = ["Ah mqa jk wnneaocw, jk cwjw.",
                     "Ho bc sbnc qftcp snn kmpkqwyhsfkcy ho xpskhmkc lmzc hdmfuy kofyhmhqhcy xcplckh zmphqc; hdcyc lmzc hdmfuy spc upszmha, ucfcpoymha ol yoqn, ymfkcpmha, cspfcyhfcyy, sft emftfcyy. - Koflqkmqy",
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
for a in range(1, 14):
    for b in range(1, 14):
        for c in range(10):
            for x in range(26):
                caesarCipherPlus(inputs[1], chr(x + 97), (a, b, c))