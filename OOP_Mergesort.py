import random

class merge_sort():

    def getlist(self):
        self.num = []
        for i in range(1, 21):
            n = random.randrange(1, 99)
            self.num.append(n)
            times = self.num.count(n)
            if times == 2:
                self.num.pop()
                n = random.randrange(1, 99)
                self.num.append(n)
        return self.num

    def getleftandright(self):
        self.getlist()
        self.Left = []
        self.Right = []
        for i in range(0, 20, 2):
            self.Left.append(self.num[i])
            self.Right.append((self.num[i+1]))
        self.Left.append(100)
        self.Right.append(100)
        return self.Left, self.Right, self.num

    def sortleftandright(self):
        self.getleftandright()
        n = len(self.Left)
        for j in range(0, n):
            key1 = self.Left[j]
            i = j - 1
            while i > -1 and self.Left[i] > key1:
                self.Left[i + 1] = self.Left[i]
                i = i - 1
                self.Left[i + 1] = key1
        for j in range(0, n):
            key2 = self.Right[j]
            i = j - 1
            while i > -1 and self.Right[i] > key2:
                self.Right[i + 1] = self.Right[i]
                i = i - 1
                self.Right[i + 1] = key2
        return self.Left, self.Right, self.num

    def mergesort(self):
        self.sortleftandright()
        M = []; i = 0; j = 0
        for n in range(0, 20):
            if self.Right[j] < self.Left[i]:
                M.append(self.Right[j])
                j = j + 1
            else:
                M.append(self.Left[i])
                i = i + 1
        print('')
        print('LEFT =', self.Left)
        print('')
        print('RIGHT =', self.Right)
        print('')
        print(M)




data = merge_sort()

#print(data.getleftandright())

#print(data.sortleftandright())

print(data.mergesort())