
List = [9,2,7,4,5,6,8,3,1, 'end']

for x in range(0, len(List)):
    print(List)
    key = List[x+1]
    if key == 'end':
        break
    i = x
    while i >= 0 and List[i] > key:
        List[i +1] = List[i]
        i = i - 1
        List[i+1] = key








