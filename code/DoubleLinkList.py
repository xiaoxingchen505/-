

class Node(object):
    
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None


class DoubleLinkList(object):


    def __init__(self):
        self.__head = None

    def is_empty(self):
    
        return self.__head == None
    
    def length(self):
        """链表长度"""

        if self.is_empty():
            return 0

        # cur游标，用来移动遍历节点
        cur = self.__head
        # count 记录数量
        count = 1
        while cur != None:
            count += 1
            cur = cur.next
        return count


    def travel(self):
        """遍历并打印每个元素"""
        if self.is_empty():
            return
        cur = self.__head
        while cur != None:
            print(cur.elem, end = " ")
            cur = cur.next
        #退出循环，cur指向尾节点，但尾节点的元素未打印
        #打印单节点或者尾节点

        if cur != None:
            print(cur.elem)


    def add(self, item):
        """链表头部添加元素"""

        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node


    def append(self,item):
        """在链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self,pos,item):

        """指定位置添加元素"""

        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            pre = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next

            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        # 判断链表是否只有一个节点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:        
                        cur.next.prev = cur.prev
                break
            else:
                cur =  cur.next

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head: 
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False   



single_obj = DoubleLinkList()

if __name__ == "__main__":
    ll = DoubleLinkList()
    print(ll.is_empty())
    print(ll.length())
    
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.add(8)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    ll.append(5)

    ll.append(6)

    ll.insert(2, 200)

    ll.remove(5)
    ll.remove(1)
    ll.travel()