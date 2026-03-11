#!/usr/bin/env python3
"""Vigenere cipher."""
import sys
def encrypt(text,key):
    result=[]; ki=0
    for c in text:
        if c.isalpha():
            base=ord('A') if c.isupper() else ord('a')
            shift=ord(key[ki%len(key)].upper())-ord('A')
            result.append(chr((ord(c)-base+shift)%26+base)); ki+=1
        else: result.append(c)
    return ''.join(result)
def decrypt(text,key):
    result=[]; ki=0
    for c in text:
        if c.isalpha():
            base=ord('A') if c.isupper() else ord('a')
            shift=ord(key[ki%len(key)].upper())-ord('A')
            result.append(chr((ord(c)-base-shift)%26+base)); ki+=1
        else: result.append(c)
    return ''.join(result)
if len(sys.argv)<3: sys.exit("Usage: vigenere <encrypt|decrypt> <key> [text]")
cmd,key=sys.argv[1],sys.argv[2]
text=' '.join(sys.argv[3:]) if len(sys.argv)>3 else sys.stdin.read().strip()
print(encrypt(text,key) if cmd[0]=='e' else decrypt(text,key))
