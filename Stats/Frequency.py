def freq(nums, startLst, length):
    '''
    nums: list of values
    startlst: starting range
    length: total length of table, including starting range, beginning from 1
    '''
    res = []
    diff = startLst[1] - startLst[0] + 1

    k = 0
    for i in range(length):
        res.append((startLst[0] + diff*k, startLst[1] + diff*k))
        k += 1
    
    d = {}
    for n in nums:
        for tup in res:
            d[tup] = d.get(tup,[])
            if n >= tup[0] and n <= tup[1]:
                d[tup].append(n)
                break

    print("Value | Frequency")
    for key in d:
        print(f"{key[0]}-{key[1]} | {len(d[key])}")

    return d

lst = [
26,23,31,11,28,37,23,16,15,23,15,11,52,13,11,25,14,19,31,24,38,35,20,23,38,33,16,37,34,13,16
]

freqLst = freq(nums=lst, startLst=[11,15], length=9)

def relfreq(nums, d):

    for key in d:
        d[key] = len(d[key])/len(nums)
        
    print("Value | Relative Frequency")
    for key in d:
        print(f"{key[0]}-{key[1]} | {d[key]:.3f}")

relfreq(nums=lst, d=freqLst)
