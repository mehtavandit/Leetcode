H = [0] * 50
size = 0

def parent(i):

    return (i-1) // 2

def left_child(i):

    return ((2*i) + 1)

def right_child(i):

    return ((2*i)+2)

def shiftup(i):

    while (i>0 and H[parent(i)] > H[i]):
        swap(parent(i), i)
        i = parent(i)

def shiftdown(i):
    max_index = i
    l = left_child(i)
    if (l<= size and H[l] < H[max_index]):
        max_index = l

    r = right_child(i)
    if (r<=size and H[r] < H[max_index]):
        max_index = r

    if i!=max_index:
        swap(i, max_index)
        shiftdown(max_index)

def insert(p):
    global size
    H[size] = p
    shiftup(size)
    size = size + 1

def extract_min():
    global size
    result = H[0]
    H[0] = H[size-1]
    size -= 1
    shiftdown(0)
    return result

def deletekey(i):
    global size
    if (i>size):
        return
    decreasekey(i, -99999)
    extract_min()

def decreasekey(i, val):
    H[i] = val
    shiftup(i)
    

def swap (i, j):
    temp = H[i]
    H[i] = H[j] 
    H[j] = temp

insert(4)
insert(2)
insert(8)
insert(16)
insert(24)
insert(2)
insert(6)
insert(5)

i=0
print("Priority Queue : ", end = "") 
while (i < size) : 
 
    print(H[i], end = " ") 
    i += 1

print()
deletekey(4)

i=0
print("Priority Queue : ", end = "") 
while (i < size) : 
 
    print(H[i], end = " ") 
    i += 1