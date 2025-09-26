def gcd(m, n):

    while n:
        m, n = n, m % n
    return m

n = int(input())
for i in range(n):
     m, n = list(map(int, input().strip().split(", "))) 
     print(gcd(m, n))
     
     