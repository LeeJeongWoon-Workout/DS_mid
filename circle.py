class NodeType:
    """ Node Type """
    def __init__(self, item):
        self.info = item
        self.next = None

class CircularLL:
    def __init__(self):
        self.listData = None
        self.length = 0
        self.currentPos = None

    def is_full(self):
        try:
            location = NodeType("test")
            return False
        except:
            return True

    def length_is(self):
        return self.length

    def make_empty(self):
        while self.listData != None:
            tempPtr = self.listData.next
            del self.listData
            self.listData = tempPtr
        self.length = 0

    def find_item(self, listData, item):

        moreToSearch=True
        location=listData.next
        pred=listData
        found=False

        while (moreToSearch and not found):
            if (item<location.info):
                moreToSearch=False
            elif (item==location.info):
                found=True
            else:
                pred=location
                location=location.next
                moreToSearch=(location!=listData.next)

        return location,pred,found



    
    def insert_item(self, item):

        newNode=None
        pred=None
        location=None
        found=False

        newNode=NodeType(item)
        if (self.listData!=None):
            location,pred,found=self.find_item(self.listData,item)
            newNode.next=pred.next
            pred.next=newNode

            if self.listData.info<item:
                self.listData=newNode
        else:
            self.listData=newNode
            newNode.next=newNode

        self.length+=1




    def delete_item(self, item):

        location=None
        pred=None
        found=False

        location,pred,found=self.find_item(self.listData,item)

        if (pred==location):
            self.listData=None
        else:
            pred.next=location.next
            if location==self.listData:
                self.listData=pred

        self.length-=1



   

    def reset_list(self):
        self.currentPos = None

    def get_next_item(self):
        if self.currentPos == None:
            self.currentPos = self.listData
        else:
            self.currentPos = self.currentPos.next
        return self.currentPos.info

    def __str__(self):
        self.reset_list()
        items = []
        for i in range(0, self.length):
            t = self.get_next_item()
            items.append(str(t))
        return " ".join(items)
