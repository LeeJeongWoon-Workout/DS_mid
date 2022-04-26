class NodeType:
    """ Node Type """
    def __init__(self, item):
        self.info = item
        self.next = None
        self.back = None

class DoublyLL:
    def __init__(self):
        self.head = NodeType('head')
    
    def find_item(self, item):

        moreToSearch=True
        location=self.head
        found=False

        while (location!=None):
            if (location.info!=item):
                location=location.next
            else:
                break

        return location

    def insert_item(self, item, new):

        newNode=None
        location=None
        found=False

        newNode=NodeType(new)

        location=self.find_item(item)

        if (location.next==None):
            location.next=newNode
            newNode.back=location

        else:
            next=location.next

            location.next=newNode
            newNode.back=location

            newNode.next=next
            next.back=newNode


    def delete_item(self, item):

        location=self.find_item(item)

        pred=location.back
        next=location.next

        pred.next=next
        next.back=pred
            
    def __str__(self):
        cur_node = self.head
        items = []
        while cur_node is not None:
            items.append("(" + str(cur_node.info) + ")\n")
            cur_node = cur_node.next
        return "".join(items)

