#!/usr/bin/env python3
"""vigenere - Vigenere cipher."""
import sys, argparse, json

def encrypt(text, key):
    result = []; ki = 0
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            shift = ord(key[ki % len(key)].upper()) - ord("A")
            result.append(chr((ord(ch) - base + shift) % 26 + base))
            ki += 1
        else:
            result.append(ch)
    return "".join(result)

def decrypt(text, key):
    result = []; ki = 0
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            shift = ord(key[ki % len(key)].upper()) - ord("A")
            result.append(chr((ord(ch) - base - shift) % 26 + base))
            ki += 1
        else:
            result.append(ch)
    return "".join(result)

def kasiski(text, max_key_len=20):
    text_clean = "".join(c.upper() for c in text if c.isalpha())
    from collections import Counter
    from math import gcd
    distances = []
    for l in range(3, 6):
        seen = {}
        for i in range(len(text_clean) - l):
            seq = text_clean[i:i+l]
            if seq in seen: distances.append(i - seen[seq])
            else: seen[seq] = i
    if not distances: return []
    factor_counts = Counter()
    for d in distances:
        for f in range(2, min(d+1, max_key_len+1)):
            if d % f == 0: factor_counts[f] += 1
    return [f for f, _ in factor_counts.most_common(5)]

def main():
    p = argparse.ArgumentParser(description="Vigenere cipher")
    sub = p.add_subparsers(dest="cmd")
    e = sub.add_parser("encrypt"); e.add_argument("text"); e.add_argument("key")
    d = sub.add_parser("decrypt"); d.add_argument("text"); d.add_argument("key")
    a = sub.add_parser("analyze"); a.add_argument("text")
    args = p.parse_args()
    if args.cmd == "encrypt":
        print(json.dumps({"plaintext": args.text, "key": args.key, "ciphertext": encrypt(args.text, args.key)}))
    elif args.cmd == "decrypt":
        print(json.dumps({"ciphertext": args.text, "key": args.key, "plaintext": decrypt(args.text, args.key)}))
    elif args.cmd == "analyze":
        likely_lens = kasiski(args.text)
        print(json.dumps({"ciphertext": args.text[:50]+"...", "likely_key_lengths": likely_lens}))
    else: p.print_help()

if __name__ == "__main__": main()
