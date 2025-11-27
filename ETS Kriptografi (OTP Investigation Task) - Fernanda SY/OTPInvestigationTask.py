# ============================
# OTP Recovery Script - Verifikasi
# ============================

C1 = "TLCYKUMGDFAWTZVOYKLENSZZHYZRW"
P1 = "MRJOHNSONLEFTHISHOUSELASTNIGHT"[:29]
C2 = "QXGLZMSOYTUVWSXKZVTLFQSKKMZXM"


# --- Konversi string huruf A–Z menjadi angka 0–25 ---
def to_nums(s):
    return [ord(ch) - 65 for ch in s]

# --- Konversi angka 0–25 kembali ke huruf ---
def to_str(nums):
    return ''.join(chr((n % 26) + 65) for n in nums)


# --- Konversi C1 dan P1 ---
c1n = to_nums(C1)
p1n = to_nums(P1)

# --- Derive key K = C1 - P1 (mod 26) ---
kn = [(c - p) % 26 for c, p in zip(c1n, p1n)]
key = to_str(kn)

# --- Decrypt C2: P2 = C2 - K (mod 26) ---
c2n = to_nums(C2)
p2n = [(c - k) % 26 for c, k in zip(c2n, kn)]
p2 = to_str(p2n)

print("C1:", C1)
print("P1 (used):", P1)
print("Derived key:", key)
print("C2:", C2)
print("Decrypted P2:", p2)


# --- OPSIONAL: Tabel langkah-langkah ---
print("\nTabel posisi | C1 | C1# | P1 | P1# | K | K#")
for i, (c, p, k) in enumerate(zip(C1, P1, key), start=1):
    print(f"{i:02d} | {c} | {ord(c)-65:02d} | {p} | {ord(p)-65:02d} | {k} | {ord(k)-65:02d}")
