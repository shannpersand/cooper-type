A = 100
B = 750

rect(A, 100, 10, 10)
rect(B, 100, 10, 10)

t = 0.7

# interpolation
C = A + t * (B - A)

fill(1, 0, 0)
rect(C, 100, 10, 10)
