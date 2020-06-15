


class Queue(object):
    def __init__(self):
        self.__queue = []
    

    def enqueue(self, item): # 往队列中添加一个item元素
        self.__queue.append(item) # 尾部添加

        # self.__queue.insert(0,item) # 头部添加

    def pop_front(self): # 从队列头部删除一个元素

        if self.__queue == []:
            return None
        else:
            return self.__queue.pop(0) # 头部删除

    def pop_rear(self): # 从队列头部删除一个元素

        if self.__queue == []:
            return None
        else:
            return self.__queue.pop() # 尾部删除


    def is_empty(self): # 判断一个队列是否为空

        return self.__queue == []

    def size(self): # 返回队列的大小

        return len(self.__queue)



if __name__ == '__main__':
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    s.enqueue(5)
    print(s.size())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
