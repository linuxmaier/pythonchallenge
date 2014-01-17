import string

def caesar_shift(cipher, shift):
    alpha = string.ascii_letters[:26]
    return_string = ''

    for letter in cipher:
        try:
            return_string += alpha[(alpha.index(letter) + shift) % len(alpha)]
        except ValueError:
            return_string += letter
            
    return return_string

challenge_cipher = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
challenge_shift = 2
print(caesar_shift(challenge_cipher, challenge_shift))
