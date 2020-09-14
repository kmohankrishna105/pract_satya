#commit
leg2=[{'action':1,'bid':2.21,'ask':2.60},
     {'action':0,'bid':1.02,'ask':1.41},
     {'action':0,'bid':0.52,'ask':0.68},
     {'action':1,'bid':0.25,'ask':0.30}]
leg1=[{'action':1,'bid':2.21,'ask':2.60},{'action':1,'bid':1.87,'ask':2.15}]
leg3=[{'action':1,'bid':1.02,'ask':1.41},{'action':0,'bid':0.52,'ask':0.68}]

leg4=[{'action':1,'bid':1.87,'ask':2.15},
     {'action':0,'bid':3.15,'ask':3.75},
     {'action':0,'bid':0.52,'ask':0.68},
     {'action':1,'bid':0.25,'ask':0.30}]

def calculate_debit_credit(leg):
    ask=0
    bid=0
    ask_c=0
    bid_c=0
    for l in leg:
        if l['action'] ==1:
            ask+=l['ask']
            bid_c += l['bid']
        else:

            bid+=l['bid']
            ask_c += l['ask']
    diff=ask-bid
    if diff>=0:
        status='Debit'
        final_ask=abs(round(diff,2))
        final_bid= abs(round(bid_c - ask_c, 2))
    else:
        status='Credit'
        final_bid=abs(round(diff,2))
        final_ask = abs(round(bid_c - ask_c, 2))
    from decimal import Decimal
    mid=(final_bid+final_ask)/2
    def round_off(num):
        if int(str(round(num, 3))[-1]) == 5:
            num = round(num, 3) + 0.001
            return num
    round_off(mid)
    return status,final_bid,final_ask,round(mid,2)

print(calculate_debit_credit(leg1))
print(calculate_debit_credit(leg2))
print(calculate_debit_credit(leg3))
print(calculate_debit_credit(leg4))