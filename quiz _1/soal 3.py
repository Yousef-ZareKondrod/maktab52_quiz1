from collections import Counter

# list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
#          'w', 'x', 'y', 'z']


def generator(file_path):
    with open(file_path) as f:
        m = f.read()
        print(m)
        z = m.split(' ')
        print(z)
        for i in range(len(z)):
            n = z[i]
            a = Counter(n)
            print(a)


print(generator('test3.txt'))
generator('test3.txt')
