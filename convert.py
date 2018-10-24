R_template = [
    {1: "I", 5: "V"},
    {1: "X", 5: "L"},
    {1: "C", 5: "D"},
    {1: "M"},
]

def egg(num,d):
    num,d = int(num),int(d)
    if(num == 0):return ''
    b = int(num)%5
    
    if(b == 0):
        return R_template[d][5]
    elif(b == 4):
        return R_template[d][1] + (R_template[d+1][1]  if(num>5) else R_template[d][5])
    else:
        return (R_template[d][5] if(num>5) else '') + R_template[d][1] * int(b)

for i,val in enumerate(str(1954)[::-1]):
    print(egg(val,i))
