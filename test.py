# helper functions
def text_to_nums(text: str):
    return [ord(c) - ord('a') for c in text]


def nums_to_text(nums: list[int]):
    return ''.join(chr(n + ord('a')) for n in nums)


# compute gaps (C1 - C2) mod 26
def determine_gaps(ciphertext1: str, ciphertext2: str):
    return [(ord(c1) - ord(c2)) % 26 for c1, c2 in zip(ciphertext1, ciphertext2)]


# your ciphertexts
C1 = "mlgclitpnm"
C2 = "jtdtnquznm"

gaps = determine_gaps(C1, C2)
print("Gaps:", gaps)
print("Gaps as letters:", nums_to_text(gaps))  # just for visualization

# read wordlist of 10-letter words
with open("10-letter-words.txt", "r") as f:
    wordlist = [line.strip() for line in f]

# try each candidate word as plaintext1
for candidate in wordlist:
    if len(candidate) != len(C1):
        continue  # skip words of wrong length

    P1 = text_to_nums(candidate)

    # compute corresponding plaintext2 using gaps
    P2 = [(p1 - g) % 26 for p1, g in zip(P1, gaps)]
    P2_text = nums_to_text(P2)

    if P2_text in wordlist:
        print(f"Match found!\nP1: {candidate}\nP2: {P2_text}\n")