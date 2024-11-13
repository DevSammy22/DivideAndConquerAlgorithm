#totally mine
def mod_exp(a, n, m):
    if n == 1:
        return a % m

    mid = n//2
    half_left = mod_exp(a, mid, m)

    if n % 2 == 0:
        half_right = half_left
        return (half_right * half_left) % m
    else:
        return (half_left * half_left * (a % m)) % m



# Example usage
a = 5
n = 3
m = 13
result = mod_exp(a, n, m)
print(f"{a}^{n} % {m} = {result}")
