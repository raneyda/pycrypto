#!/usr/bin/python3

import sys
#print('\n'.join(sys.path))
import string
import collections
from itertools import product
from re import findall

if __name__ == '__main__':
    sys.exit("Error - this is a module not a program")

else:

    pigpen_alpha = {'A': '\u25C7',
                    'B': '\u25F0',
                    'C': '\u25F3',
                    'D': '\u25F2',
                    'E': '\u25F1',
                    'F': '\u25F4',
                    'G': '\u25F7',
                    'H': '\u25F6',
                    'I': '\u25F5',
                    'J': '\u25BD',
                    'K': '\u25C1',
                    'L': '\u25B3',
                    'M': '\u25B7',
                    'N': '\u25BC',
                    'O': '\u25C0',
                    'P': '\u25B2',
                    'Q': '\u25B6',
                    'R': '\u25FF',
                    'S': '\u25FA',
                    'T': '\u25F8',
                    'U': '\u25F9',
                    'V': '\u25CB',
                    'W': '\u25CC',
                    'X': '\u25CF',
                    'Y': '\u25CE',
                    'Z': '\u25C6',
                    }

    def pt_upper(pt: str):
        pt = str(pt)
        return pt.upper()

    def pt_nopunc(pt: str):
        transtab = str.maketrans("", "", string.punctuation)
        return pt.translate(transtab)

    def pt_nospaces(pt: str):
        pt = pt.replace(" ","")
        pt = pt.replace("\n","XX")
        return pt

    def pt_printer_output(pt: str, ptr_width = 39):
        pt = str(pt)
        newStr = ""
        for index in range(len(pt)):
            if ((index+1)%ptr_width == 0):
                newStr = newStr + pt[index] + "\n"
            else:
                newStr = newStr + pt[index] + " "
        return newStr

    def pt_parse_text(pt):
        pt = pt_upper(pt)
        pt = pt_nopunc(pt)
        pt = pt_nospaces(pt)
        return pt

    def char_frequency(pt):
        pt = str(pt_parse_text(pt))
        counts = { letter: pt.count(letter) for letter in string.ascii_uppercase}
        return counts

    def shift_cipher(pt, shift):
        pt = str(pt_parse_text(pt))
        ct = ""
        for letter in pt:
            index = ord(letter) - ord('A') + shift
            ct = ct + string.ascii_uppercase[index % len(string.ascii_uppercase)]
        ct = pt_parse_text(ct)
        return ct

    def playfair_key(key):
        key = str(pt_parse_text(key))
        key = "".join([j for i,j in enumerate(key) if j not in key[:i]])
        if ((key.find("I") == -1) and (key.find("J") == -1)) or (key.find("I") < key.find("J")) or (key.find("J") == -1):
            key = key.replace("J","")
            for letter in string.ascii_uppercase:
                if (letter not in key) and (letter != "J"):
                    key = key + letter
        elif key.find("I") > key.find("J"):
            key = key.replace("I","")
            for letter in string.ascii_uppercase:
                if (letter not in key) and (letter != "I"):
                    key = key + letter
        return key

    def partition(seq, n):
        return [seq[i : i + n] for i in range(0, len(seq), n)]

    def playfair_cipher(key, msg, operation="enc"):
        # Code borrowed from: https://rosettacode.org/wiki/Playfair_cipher#Python  - Updated for Python 3
        # Build 5x5 matrix.
        m = partition(playfair_key(key), 5)
 
        # Pregenerate all forward translations.
        enc = {}

        # Map pairs in same row.
        for row in m:
            for i, j in product(range(5), repeat=2):
                if i != j:
                    enc[row[i] + row[j]] = row[(i + 1) % 5] + row[(j + 1) % 5]
 
        # Map pairs in same column.
        for c in zip(*m):
            for i, j in product(range(5), repeat=2):
                if i != j:
                    enc[c[i] + c[j]] = c[(i + 1) % 5] + c[(j + 1) % 5]
 
        # Map pairs with cross-connections.
        for i1, j1, i2, j2 in product(range(5), repeat=4):
            if i1 != i2 and j1 != j2:
                enc[m[i1][j1] + m[i2][j2]] = m[i1][j2] + m[i2][j1]
 
        # Generate reverse translations.
        dec = dict((v, k) for k, v in enc.items()) 

        msg = pt_parse_text(msg)

        if operation == "enc":
            lst = findall(r"(.)(?:(?!\1)(.))?", msg)
            return " ".join(enc[a + (b if b else 'X')] for a, b in lst)
        else:
            return " ".join(dec[p] for p in partition(msg, 2))
