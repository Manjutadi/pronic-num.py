#pronic no
def pronic(n):
    for i in range(1,n):
        if n==i*(i+1):
            return True
        if i*(i+1)>n:
            return False
n=int(input())
print(pronic(n))
