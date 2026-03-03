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

def caeserCipherPlus(text: str, key: str, trip: tuple[int, int, int]):
    result: str = ""
    for char in text:
        if char.isalnum():
            numeric = ord(char)
            key_num = ord(key) - 97 if key.isupper() else ord(key) - 65
            numeric_result = (trip[0] * (numeric ** 3) + trip[1] * (numeric ** 2) + trip[2] * numeric + key_num) % 26
            result += chr(numeric_result + 97 if numeric >= 97 else numeric_result + 65)
        else:
            result += char
    print(f"{result} - Tuple {trip} and key {key}")

caeserCipherPlus(inputs[1], 'f', (1,2,4))