import sys
input = sys.stdin.readline

cash = int(input())
stock = list(map(int, input().split()))
jh, sm = [], []

def jh(stock):
    asset = 0
    money = cash
    n = 0
    for i in stock:
        while i*(n+1) <= money:
            n += 1
        if n*i <= money:
            asset += n*i
            money -= n*i
    return (money + stock[-1]*n)

def sm(stock):
    asset = 0
    money = cash
    n = 0
    for i in range(11):
        if stock[i] < stock[i+1] and stock[i+1] < stock[i+2] and stock[i+2] < stock[i+3]:
            asset -= n * stock[i+3]
            money += n * stock[i+3]
            n = 0
        elif stock[i] > stock[i+1] and stock[i+1] > stock[i+2] and stock[i+2] > stock[i+3] :
            count = 0
            while stock[i+3]*(count+1) <= money:
                count += 1
            asset += count*stock[i+3]
            money -= count*stock[i+3]
            n += count
    return (money + stock[-1]*n)

if jh(stock) > sm(stock):
    print('BNP')
elif jh(stock) < sm(stock):
    print('TIMING')
else:
    print('SAMESAME')
