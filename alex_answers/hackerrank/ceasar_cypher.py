

def caesarCipher(s: str, k:int):

    LOWER_A = 97
    CAP_A = 65

    new_str = []

    for i in s:

        if not i.isalpha():
            new_str.append(i)
            continue

        a_val = LOWER_A if i.islower() else CAP_A

        new_str.append(chr(((ord(i) - a_val + k) % 26) + a_val))

    return "".join(new_str)



print(caesarCipher("middle-Outz", 2))






