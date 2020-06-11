
class Node(object):


    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):


    """定义一个单链表"""
    def __init__(self, node= None):
        self.__head = None
         
    def is_empty(self):

        return self.__head == None

    def length(self):
        
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count 记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count


    def travel(self):
        """遍历并打印每个元素"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end = " ")
            cur = cur.next


    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        


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
        pre = None
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

            

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None: 
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

single_obj = SingleLinkList()

if __name__ == "__main__":
    ll = SingleLinkList()
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

