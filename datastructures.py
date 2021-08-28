#Tarek Sayed
#Copy right Notice:
#Copyright ©2020. Tarek Sayed . All Rights Reserved.
# Permission required from author to use, copy, modify, and distribute this software and its documentation.
#Students are allowed to use this for their own personal review but may not copy, modify, or distribute this software.


import random


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None  # the pointer initially points to nothing

    def __str__(self):
        return self.data

    def __eq__(self, other):
        if (type(other) == Node):
            return self.data == other.data
        else:
            n = Node(other)
            return self.data == n.data

    def __ne__(self, other):
        if (type(other) == Node):
            return self.data != other.data
        else:
            n = Node(other)
            return self.data != n.data


class Stack:

    def __init__(self, sname=None, otherStack=None):

        self.stackTop = None
        self.nNodes = 0
        self.stackName = sname
        if (otherStack != None):  # Copy Constructor
            self.stackTop = None
            self.copyStack(otherStack)

    def initializeStack(self):
        self.nNodes = 0
        while (self.stackTop != None):
            temp = self.stackTop
            self.stackTop = self.stackTop.next
            del temp

    def isEmptyStack(self):
        return self.stackTop == None

    def isEmpty(self):
        return self.stackTop == None

    def isFullStack(self):
        return False;

    def pushNode(self, newNode):
        if (self.size() > 0 and type(newNode.data) != type(self.stackTop.data)):
            print("Invalid data Type. This stack is a stack for the " + str(type(self.stackTop.data)) + " data type.")
            return

        newNode.next = self.stackTop
        self.stackTop = newNode
        self.nNodes += 1

    def push(self, newItem):
        if (self.size() > 0 and type(newItem) != type(self.stackTop.data)):
            print("Invalid data Type. This stack is a stack for the " + str(type(self.stackTop.data)) + " data type.")
            return
        newNode = Node(newItem)

        newNode.next = self.stackTop
        self.stackTop = newNode
        self.nNodes += 1

    def top(self):
        if (self.stackTop != None):
            return self.stackTop.data
        else:
            return None

    def topNode(self):
        if (self.stackTop != None):
            return self.stackTop
        else:
            return None

    def pop(self):

        if (self.stackTop != None):
            temp = self.stackTop
            self.stackTop = self.stackTop.next
            del temp
            self.nNodes -= 1
        else:
            print("Cannot remove from an empty stack.")

    def size(self):
        return self.nNodes

    def __str__(self):
        retstr = "" + "top |  "
        s = self.stackTop

        while (s != None):
            retstr += str(s.data) + "  "
            s = s.next
        retstr += "| bottom"
        return retstr

        # make a copy of otherStack to this stack.*/

    def copyStack(self, otherStack):

        if (self.stackTop != None):  # if stack is nonempty, make it empty
            self.initializeStack()

        if (otherStack.stackTop == None):
            self.stackTop = None
        else:

            current = otherStack.stackTop
            # self.stackTop = new Node<Type>;  #create the node
            self.stackTop = Node(current.data)
            self.stackTop.next = None  # set the next field of the node to NULL
            last = self.stackTop
            current = current.next
            # copy the remaining stack
            while (current != None):
                newNode = Node(current.data)
                newNode.next = None
                last.next = newNode
                last = newNode
                current = current.next
                self.nNodes += 1
            self.nNodes += 1

    def isEqual(self, other):
        if (not isinstance(other, Stack)):
            return False
        if (not self.isEmpty() and not other.isEmpty() and type(self.stackTop) != type(other.stackTop)):
            return False;
        if (self.isEmpty() and other.isEmpty()):
            return True;
        if (self.size() != other.size()):
            return False;

        lstA = []
        lstB = []
        result = False
        thisSize = self.size()
        otherSize = other.size()

        for i in range(0, thisSize):
            lstA.append(self.top())
            self.pop();

        for i in range(0, otherSize):
            lstB.append(other.top())
            other.pop();

        self.stackTop = None
        self.nNodes = 0
        for j in range(thisSize - 1, -1, -1):
            self.pushNode(Node(lstA[j]))

        for j in range(otherSize - 1, -1, -1):
            other.pushNode(Node(lstB[j]))
        i = 0
        while (not self.isEmpty() and not (other.isEmpty())):

            if (self.top() == other.top()):

                t = self.top()
                self.pop()
                o = other.top()
                other.pop()

                if (self.isEmpty() and other.isEmpty()):
                    result = True
                    break
                i += 1
            else:
                result = False
                break

        while (not other.isEmpty()):
            o = other.top()
            other.pop()

        self.stackTop = None
        self.nNodes = 0

        for j in range(thisSize - 1, -1, -1):
            self.push(Node(lstA[j]))
        for j in range(otherSize - 1, -1, -1):
            other.push(Node(lstB[j]))

        return result

    def reverse(self):

        current = prev = self.stackTop
        current = current.next
        prev.next = None
        while (current != None):
            succ = current.next
            current.next = prev
            prev = current
            current = succ

        self.stackTop = prev

    def print(self):
        s = self.stackTop;
        print("top ", end="")
        while (s != None):
            print(str(s.data) + " ", end="")
            s = s.next;
        print(" bottom")
        print()

    def deleteInnerNode(self, loc):

        s = Stack()
        assert self.stackTop != None, "Stack is Empty"
        current = self.stackTop
        i = 0
        size = self.size()
        assert loc < size and not (
            self.isEmpty()), "Stack is Empty or location of deleted node is outside of stack size"
        while (i < loc and current != None):
            # print("i="+str(i))
            current = current.next
            i += 1

        n = current

        i = 0
        size = self.size()
        while (not self.isEmpty() and i < size):
            if (i != loc):
                s.push(self.stackTop.data)
                self.pop()

            else:
                self.pop()
            i += 1
        s.reverse()
        self.stackTop = s.stackTop
        self.nNodes = s.size()
        return n.data

    def getInnerNode(self, loc):
        s = Stack()
        assert self.stackTop != None, "Stack is Empty"
        current = self.stackTop
        i = 0
        size = self.size()
        assert loc < size, "requested location outside of stack size"
        while (i < loc and current != None):
            current = current.next
            i += 1

        return current.data

    def __eq__(self, other):
        return self.isEqual(other)

    def __ne__(self, other):
        return (not self.isEqual(other))


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def addAtHead(self, newNode):

        self.count += 1

        if (self.head == None):  # empty
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def addAtTail(self, newNode):
        self.count += 1

        if (self.head == None):  # empty
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def insert(self, d):

        if (self.head == None):
            self.addAtHead(d)
        elif (d.data <= self.head.data):
            self.addAtHead(d)
        elif (d.data >= self.tail.data):
            self.addAtTail(d)
        else:
            n = d
            self.count += 1
            t1 = self.head
            t2 = None
            while (d.data > t1.data):
                t2 = t1
                t1 = t1.next

            n.next = t1
            t2.next = n

    def __str__(self):
        current = self.head
        lstr = ""
        while (current != None):
            lstr = lstr + str(current.data).rjust(4) + " --> "
            current = current.next
        lstr = lstr + " None"
        return lstr

    def isEmpty(self):
        return self.head == None

    def contains(self, searchItem):
        current = self.head
        while (current != None):
            if (current.data == searchItem):
                return True;
            current = current.next
        return False

    def deleteItem(self, deleteItem):
        current = Node(None)  # current is a pointer to traverse the list
        trailCurrent = Node(None)  # pointerjust before current bool found
        if (self.head == None):  # Case 1; the list is empty.
            print("Cannot delete from an empty list.")
        else:
            if (self.head.data == deleteItem):  # Case2
                current = self.head
                self.head = self.head.next
                self.count -= 1
                if (self.head == None):  # the list has only one node
                    self.tail = None
                del current
            else:  # search the list for the node with the given info
                found = False
                trailCurrent = self.head  # set trailCurrent to point to the first node
                current = self.head.next  # set current to point to the second node
                while (current != None and not found):
                    if (current.data != deleteItem):
                        trailCurrent = current
                        current = current.next
                    else:
                        found = True
                if (found):  # Case 3; if found, delete the node
                    trailCurrent.next = current.next;
                    self.count -= 1
                    if (self.tail == current):  # node to be deleted was the last node
                        self.tail = trailCurrent;  # update the value of tail
                    del current  # delete the node from the list
                else:
                    print("The item to be deleted is not in the list.")

    def swap(self, p1, p2):
        temp = Node(None)
        temp.data = p1.data;
        p1.data = p2.data;
        p2.data = temp.data;

    def selectionSort(self):
        start = Node(None)
        current = Node(None)
        start = self.head;
        if (self.isEmpty()):
            return
        while (start.next != None):
            min = start
            current = start.next

            while (current != None):
                # Find minimum element in the list
                if (min.data > current.data):
                    min = current
                current = current.next
                # print(current.data)

            # swap minimum element with start location
            self.swap(start, min)
            start = start.next

    def __contains__(self, value):
        current = self.head
        while (current != None):
            if (current.data == value):
                return True
            current = current.next
        return False


class Deck(Stack):

    def __init__(self, sname=None, otherStack=None):
        super(Deck,self).__init__(sname=None, otherStack=None)

    def printDeck(self):

        s = self.stackTop;
        while (s != None):
            print(str(s.data) + " ", end="")
            s = s.next;
        print()

    def printPlayerDeck(self):
            print('Player cards: ', end="")
            s = self.stackTop;
            while (s != None):
                print(str(s.data) + " ", end="")
                s = s.next;
            print('\nPoints: ', self.total())


    def printDealerDeck(self):
        print('Dealer Cards: ', end="")
        s = self.stackTop;
        while (s != None):
            print(str(s.data) + " ", end="")
            s = s.next;
        print('\nPoints: ', self.total())
        print('---------------------------')

    #Calculate Total Points
    def total(self):
        s = self.stackTop;
        totValue = 0

        for i in range(self.size()):
            totValue = totValue + s.data.numberval
            s=s.next
            if s == None:
                continue

        return totValue

    def popToDeck(self,deck2):
        if self.size() != 0:
            deck2.push(self.top())
            self.pop()

    def clearStack(self):
        for i in range(self.size()):
            self.pop()



class Cards(object):

    def __init__(self, card):
        self.card = card
        if len(card) == 2:
            self.value = card[-1]
        if len(card) == 3:
            self.value = card[-2]+card[-1]
        if self.value == 'K':
            self.numberval = 10
        if self.value == 'Q':
            self.numberval = 10
        if self.value == 'J':
            self.numberval = 10
        if self.value == 'A':
            self.numberval = 11
        if self.value == '10':
            self.numberval = 10
        if self.value == '9':
            self.numberval = 9
        if self.value == '6':
            self.numberval = 6
        if self.value == '8':
            self.numberval = 8
        if self.value == '7':
            self.numberval = 7
        if self.value == '5':
            self.numberval = 5
        if self.value == '4':
            self.numberval = 4
        if self.value == '3':
            self.numberval = 3
        if self.value == '2':
            self.numberval = 2

    def __str__(self):
        return self.card


class Game(object):

    def __init__(self,playerDeck,dealerDeck,mainDeck):
        self.playerwins = 0
        self.dealerwins = 0
        self.playerDeck = playerDeck
        self.dealerDeck= dealerDeck
        self.mainDeck = mainDeck

    def playerwon(self):
        print('\033[1m' + 'Player Won!!\n' + '\033[0m')
        self.playerwins += 1

    def dealerwon(self):
        print('\033[1m' + 'Dealer Won!!\n' + '\033[0m')
        self.dealerwins += 1

    def clearPlayerAndDealerDeck(self):
        self.dealerDeck.clearStack()
        self.playerDeck.clearStack()

    def start(self):

        while self.playerDeck.total() < 18 or self.dealerDeck.total()<17:

            #random choice from player to draw card
            if 12 <= self.playerDeck.total() < 18:
                choice = random.randint(0, 1)
                if choice == 0 and self.dealerDeck.total() > 16:
                    break
                elif choice == 1:
                    self.mainDeck.popToDeck(self.playerDeck)

            #draw card to player deck and print deck
            if self.playerDeck.total() < 12:
                self.mainDeck.popToDeck(self.playerDeck)
            self.playerDeck.printPlayerDeck()

            #draw card to dealer deck
            if self.dealerDeck.total() < 17:
                self.mainDeck.popToDeck(self.dealerDeck)

            #break if went over 21
            if self.playerDeck.total() > 21:
                self.dealerDeck.printDealerDeck()
                break
            self.dealerDeck.printDealerDeck()
            if self.dealerDeck.total() > 21:
                break

    def results(self):
    #Decide winner and clear decks
        if self.playerDeck.total() > 21:
            self.dealerwon()
            self.clearPlayerAndDealerDeck()
            return

        if self.dealerDeck.total() > 21 or self.playerDeck.total() > self.dealerDeck.total():
            self.playerwon()
            self.clearPlayerAndDealerDeck()
            return

        else:
            self.dealerwon()
            self.clearPlayerAndDealerDeck()

    def showScore(self):

        PlayerPercentage = self.playerwins / ( self.playerwins + self.dealerwins)
        DealerPercetage = self.dealerwins / ( self.playerwins + self.dealerwins)

        print('_______________SCORE______________')
        print('Player: ', '{:.0%}'.format(PlayerPercentage), 'of games with ', self.playerwins,'Wins')
        print('Dealer: ', '{:.0%}'.format(DealerPercetage), 'of games with ', self.dealerwins, 'Wins')








