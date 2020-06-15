
class dequeue(object):
    def __init__(self):
        self.__queue = []
    

    def add_rear(self, item): # 往队列中添加一个item元素
        self.__queue.append(item) # 尾部添加

    def add_front(self, item):
        self.__queue.insert(0,item) # 头部添加

    def pop_front(self): # 从队列头部删除一个元素

        if self.__queue == []:
            return None
        else:
            return self.__queue.pop(0) # 头部删除

    def pop_rear(self):
        if self.__queue == []:
            return None
        else:        
            return self.__queue.pop() # 尾部删除


    def is_empty(self): # 判断一个队列是否为空

        return self.__queue == []

    def size(self): # 返回队列的大小

        return len(self.__queue)

    def print_que(self):
        output= []
        for i in self.__queue:
            output.append(i)
        return print(output)



if __name__ == '__main__':
    s = dequeue()
    s.add_front(1)
    s.add_rear(2)
    s.add_front(3)
    s.add_rear(4)
    s.add_front(5)
    print(s.size())
    s.print_que()
    print(s.pop_front())
    print(s.pop_rear())
    print(s.pop_front())
    print(s.pop_rear())
    print(s.pop_front())
    s.print_que()
