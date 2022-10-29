#Lab #7
#Due Date: 04/10/2021, 11:59PM 
'''                                 
# Collaboration Statement: I used my old HW3 for my stack class

'''


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
# ============================= COPY/PASTE your Stack class from HW3 HERE =================================  


class Stack:

    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if self.top == None:
            return True
        else:
            return False

    def __len__(self): 
        # YOUR CODE STARTS HERE
        if self.isEmpty() == True:
            return 0
        else:
            current = self.top
            length = 0
            while current:
                length += 1
                current = current.next
            return length

    def push(self,value):
        # YOUR CODE STARTS HERE
        newNode = Node(value)
        if self.isEmpty() == True:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode

     
    def pop(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty() == True:
            return None
        else:
            top = self.top.value
            self.top = self.top.next
            return top


    def peek(self):
        # YOUR CODE STARTS HERE
        return self.top.value


# ============================= Section 1 =================================                         
class Queue:
    '''
        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.dequeue()
        1
        >>> len(x)
        2
        >>> x
        Head:Node(2)
        Tail:Node(3)
        Queue:2 -> 3
    '''
    def __init__(self):
        self.head=None
        self.tail=None

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out)
        return f'Head:{self.head}\nTail:{self.tail}\nQueue:{out}'

    __repr__=__str__

    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if self.tail == None:
            return True
        return False
        

    def enqueue(self, value):
        # YOUR CODE STARTS HERE
        newNode = Node(value)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        


    def dequeue(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return
        elif len(self) == 1:
            currentHead = self.head
            self.head = None
            self.tail = None
            return currentHead.value
        else:
            currentHead = self.head
            self.head = self.head.next
            return currentHead.value

        

    def __len__(self):
        # YOUR CODE STARTS HERE
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length






# ============================= Section 2 =================================
class Graph:
    def __init__(self, graph_repr):
        self.vertList = graph_repr


    def bfs(self, start):
        '''
            Method uses an instance of the Queue class to process nodes

            >>> g3 = {'B': [('E', 3), ('C', 5)],
            ...       'F': [],
            ...       'C': [('F', 2)],
            ...       'A': [('D', 3), ('B', 2)],
            ...       'D': [('C', 1)],
            ...       'E': [('F', 4)]}
            >>> g = Graph(g3)
            >>> g.bfs('A')
            ['A', 'B', 'D', 'C', 'E', 'F']

            >>> g4 = {'Bran': ['East', 'Cap'],
            ...       'Flor': [],
            ...       'Cap':  ['Flor'],
            ...       'Apr':  ['Dec', 'Bran'],
            ...       'Dec':  ['Cap'],
            ...       'East': ['Flor']}
            >>> g = Graph(g4)
            >>> g.bfs('Apr')
            ['Apr', 'Bran', 'Dec', 'Cap', 'East', 'Flor']
        '''
        # YOUR CODE STARTS HERE
        bfsQ = Queue()
        bfsL = [start]
        bfsQ.enqueue(start)
        while bfsQ.isEmpty() == False:
            current = bfsQ.dequeue()
            neighbors = sorted(self.vertList[current])
            for n in neighbors:
                if type(n) == tuple:
                    n = n[0]
                if n not in bfsL:
                    bfsQ.enqueue(n)
                    bfsL.append(n)
        return bfsL




    def dfs(self, start):
        '''
            Method uses an instance of the Stack class to process nodes

            >>> g3 = {'B': [('E', 3), ('C', 5)],
            ...       'F': [],
            ...       'C': [('F', 2)],
            ...       'A': [('D', 3), ('B', 2)],
            ...       'D': [('C', 1)],
            ...       'E': [('F', 4)]}
            >>> g = Graph(g3)
            >>> g.dfs('A')
            ['A', 'B', 'C', 'F', 'E', 'D']

            >>> g4 = {'Bran': ['East', 'Cap'],
            ...       'Flor': [],
            ...       'Cap':  ['Flor'],
            ...       'Apr':  ['Dec', 'Bran'],
            ...       'Dec':  ['Cap'],
            ...       'East': ['Flor']}
            >>> g = Graph(g4)
            >>> g.dfs('Apr')
            ['Apr', 'Bran', 'Cap', 'Flor', 'East', 'Dec']
        '''
        # YOUR CODE STARTS HERE
        dfsStk = Stack()
        dfsStk.push(start)
        dfsL = [start]
        while dfsStk.isEmpty() == False:
            current = dfsStk.pop()
            if current not in dfsL:
                dfsL.append(current)
            neighbors = sorted(self.vertList[current], reverse = True)
            for n in neighbors:
                if type(n) == tuple:
                    n = n[0]
                if n not in dfsL:
                    dfsStk.push(n)
        return dfsL



