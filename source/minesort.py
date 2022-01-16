import hashlib

def sha256(data):
    digest = hashlib.new("sha256")
    digest.update(data.encode('utf-8'))
    return int(digest.hexdigest(), 16)


def sort(input, key):
    input = input[:]
    val = key
    for i in range(0, len(input) -1):
        index1 = key % len(input)
        key = key // len(input)
        index2 = key % len(input)
        key = key // len(input)
        if key == 0:
            key = val
        input[index1], input[index2] = input[index2], input[index1]

    return all(input[i] <= input[i + 1] for i in range(len(input)-1))


def minesort(input):
    for seed in range(1,200000):
        key=sha256(str(sha256("Mine sort is the best "+str(seed))))
        if sort(input, key):
            return seed

    return None


print("Seed "+str(minesort([1,4,2,3,5,7,8,12,2])))
