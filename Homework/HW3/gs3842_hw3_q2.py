import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self):
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0

    def __len__(self):
        return self.n

    def insert(self, index, val):
        if (-self.n <= index < self.n) == False:
            raise IndexError
        else:
            if self.n == self.capacity:
                self.resize(2 * self.capacity)
            if index >= 0:
                for i in range(self.n, index, -1):
                    self.data[i] = self.data[i-1]
                self.data[index] = val
                self.n += 1
            else:
                index += self.n
                for i in range(self.n, index, -1):
                    self.data[i] = self.data[i-1]
                self.data[index] = val
                self.n += 1

    def pop(self, index=None):
        if self.n == 0:
            raise IndexError
        else:
            if index != None:
                if -self.n <= index < self.n:
                    if index < 0:
                        index += self.n
                    value = self.data[index]

                    for i in range(index, self.n-1):
                        change = self.data[i+1]
                        self.data[i] = change
                        
                    self.data[self.n-1] = None
                    self.n -= 1

                    if self.n < (self.capacity // 4):
                        self.resize(self.capacity // 2)
                    return value

                else:
                    raise IndexError

            else:
                value = self.data[self.n-1]
                self.data[self.n-1] = None
                self.n -= 1
                if self.n < (self.capacity // 4):
                    self.resize(self.capacity // 2)

                return value


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity = new_size

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)


    def __getitem__(self, ind):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        return self.data[ind]

    def __setitem__(self, ind, val):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        self.data[ind] = val


    def __repr__(self):
        data_as_strings = [str(self.data[i]) for i in range(self.n)]
        return '[' + ', '.join(data_as_strings) + ']'


    def __add__(self, other):
        res = ArrayList()
        res.extend(self)
        res.extend(other)
        return res

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __mul__(self, times):
        res = ArrayList()
        for i in range(times):
            res.extend(self)
        return res

    def __rmul__(self, times):
        return self * times
