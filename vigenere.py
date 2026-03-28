#!/usr/bin/env python3
"""vigenere - Vigenere cipher."""
import sys

def encrypt(text, key):
    result = []; ki = 0
    for c in text:
        if c.isalpha():
            base = ord("A") if c.isupper() else ord("a")
            k = ord(key[ki % len(key)].upper()) - ord("A")
            result.append(chr((ord(c) - base + k) % 26 + base))
            ki += 1
        else: result.append(c)
    return "".join(result)

def decrypt(text, key):
    result = []; ki = 0
    for c in text:
        if c.isalpha():
            base = ord("A") if c.isupper() else ord("a")
            k = ord(key[ki % len(key)].upper()) - ord("A")
            result.append(chr((ord(c) - base - k) % 26 + base))
            ki += 1
        else: result.append(c)
    return "".join(result)

if __name__ == "__main__":
    if len(sys.argv) < 4: print("Usage: vigenere <encrypt|decrypt> <key> <text>"); sys.exit(1)
    cmd, key, text = sys.argv[1], sys.argv[2], " ".join(sys.argv[3:])
    print(encrypt(text, key) if cmd == "encrypt" else decrypt(text, key))
