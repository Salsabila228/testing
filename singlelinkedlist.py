class Node:
    def __init__(self, data):
        self.info = data
        self.next = None
# end of class node

class LinkedList:
    def __init__(self):
        self.awal = None
    def isEmpty(self):
        return self.awal is None
    def display(self):
        if self.isEmpty():
            print("Data Kosong")
        else:
            print("[", end="")
            bantu = self.awal
            while bantu is not None:
                print(bantu.info, " ", end="")
                bantu = bantu.next
            print("]")
    def addFirst(self, data):
        baru = Node(data)
        if self.isEmpty():
            self.awal = baru
        else:
            baru.next = self.awal
            self.awal = baru 
    def getFirst(self):
        return self.awal
    def getLast(self):
        akhir = self.awal
        while akhir.next is not None:
            akhir = akhir.next
        return akhir
    def addLast(self, data):
        baru = Node(data)
        if self.isEmpty():
            self.awal = baru
        else:
            akhir = self.getLast()
            akhir.next = baru
    def removeFirst(self):
        if self.isEmpty():
            print("Penghapusan gagal karena data kosong")
        else:
            nodedihapus = self.awal
            self.awal = self.awal.next
            del nodedihapus
    def removeLast(self):
        if self.isEmpty():
            print("Penghapusan gagal karena data kosong")
        elif self.awal.next is None:
            # jika linked list hanya memiliki 1 buah node
            del self.awal
            self.awal = None
        else: 
            # jika linkedlist memiliki node lebih dari satu
            # 1. cari/pegang node akhir
            akhir = self.getLast()
            # 2. cari node sbelum akhir
            prevakhir = self.awal
            while prevakhir.next.next is not akhir:
                prevakhir = prevakhir.next
            # 3. next dari node sebelum akhir di none kan
            prevakhir.next = None
            # 4. hapus node akhir
            del akhir
    def empty(self):
        while not self.isEmpty():
            self.removeFirst()
    def count(self):
        if self.isEmpty():
            return 0
        else:
            bantu = self.awal
            banyak = 1
            while bantu.next is not None:
                bantu = bantu.next
                banyak = banyak + 1
            return banyak
    def getNode(self, posisi):
        if posisi < 1 or posisi > self.count():
            return None
        else:
            bantu = self.awal
            index = 1
            while index < posisi:
                bantu = bantu.next
                index = index + 1
            return bantu
    def insert(self, posisi, data):
        if posisi < 1 or posisi > self.count():
            print("Posisi sisip tidak valid")
        elif posisi == 1:
            self.addFirst(data)
        else:
            baru = Node(data)
            bantu = self.getNode(posisi-1)
            baru.next = bantu.next
            bantu.next = baru
    def remove(self, posisi):
        if posisi < 1 or posisi > self.count():
            print("Posisi hapus tidak sah")
        elif posisi == 1:
            self.removeFirst()
        else:
            bantu = self.getNode(posisi-1)
            nodehapus = bantu.next
            bantu.next = nodehapus.next
            del nodehapus
    def update(self, posisi, databaru):
        if posisi < 1 or posisi > self.count():
            print("Posisi update tidak sah")
        else:
            bantu = self.getNode(posisi)
            bantu.info = databaru
    def search(self, dicari):
        if self.isEmpty():
            return 0 
        else:
            bantu = self.awal
            index = 1
            while bantu.info != dicari and bantu.next is not None:
                bantu = bantu.next
                index = index + 1
            return index
            if bantu.info == dicari:
                return index
            else:
                return 0 



# end of class linked list 

#tester
list = LinkedList()
list.addLast(10)
list.addLast(70)
list.addLast(6)
list.addLast(4)
list.display()

# implementasi insert/sisip
list.insert(3, 99)
list.display()

# implementasi getNode
node = list.getNode(3)
print("Data di node ke 3 adalah : ", node.info)

# implementasi remove
list.remove(4)
list.display()

# implementasi update
list.update(2, 88)
list.display()

# implementasi search
list.addLast(70)
list.addLast(6)
list.display()
index = list.search(70)
if index != 0:
    print("Data ditemukan di posisi : ", index)
else:
    print("Data tidak ditemukan")
