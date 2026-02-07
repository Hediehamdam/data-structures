class Tree_Node :
    def __init__(self , x):
        self.Data = x
        self.Lchild = None
        self.Rchild = None
#تابع بازگشتی بنویسید که تعداد برگ های درخت باینری روت را محاسبه کند
def Count_leaves(root):
    if root is None:
        return 0
    if 2 :
#       if root.Lchild is None :
#           and root.Rchild is not None:
#       if root.Rchild is None:
#           and root.Lchild is not None:                
        return 1
    return Count_leaves(root.Lchild) + Count_leaves(root.Rchild)

#تابع بازگشتی بنویسید که گره های درجه یک ، درخت باینری را محاسبه کند
def Count_1Deg(root):
    if root is None:
        return 0
    if root.Lchild:
        return 1
    if root.Rchild:
        return 1
    return Count_1Deg(root.Lchild) + Count_1Deg(root.Rchild)   

def Count_2Deg (root):
    if root is None:
        return 0
    if root.Lchild:
        return Count_2Deg(root.Lchild)
    if root.Rchild:
        return Count_2Deg(root.Rchild)
    return Count_2Deg(root.Lchild) + Count_2Deg(root.Rchild)

#تابعی بازگشتی بنویسید که حاصل جمع تمامی داده های یک درخت دودویی را بازگرداند
def sum_Tree(root):
    if root is None:
        return 0
    if root.Lchild:
        return sum_Tree(root.Lchild) + root.Data
    if root.Rchild:
        return sum_Tree(root.Rchild) + root.Data
    return sum_Tree(root.Lchild) + sum_Tree(root.Rchild) + root.Data

#تابعی بازگشتی بنوبسید که تعداد نود های یک درخت باینری را بازگرداند
def Count(root):
    if root is None:
        return 0
    return 1+ Count(root.Lchild) + Count(root.Rchild)



def pre(root):
    if root is None:
        return
    print(root.Data)
    print(root.Lchild)
    print(root.Rchild)       

#تابعی بازگشتی بنویسید که مقدار تارگت را در یک درخت جستجو کند
def search(root , t):
    if root is None:
        return False
    if root.Data == t:
        return True
    return search(root.Lchild) or search(root.Rchild)      

#تابعی بازگشتی بنویسید که مقدار حداکثر یک درخت را بازگرداند
def max_t(root):
    if root is None:
        return float("inf")
    return max(max_t(root.Lchild) , max_t(root.Rchild) , root.Data)
    


def count(root):
    if root is None:
        return 0
    return 1+ count(root.left) + count(root.right)
 

class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.Lchild = None
        self.Rchild = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_left(self, data):
        a = BinaryNode(data)
        
        if self.root is None:
            self.root = a
        else:
            temp = self.root
            while temp.Lchild != None:
                temp = temp.Lchild
            temp.Lchild = a
    
    def insert_right(self, data):
        a = BinaryNode(data)
        
        if self.root is None:
            self.root = a
        else:
            temp = self.root
            while temp.Rchild != None:
                temp = temp.Rchild
            temp.Rchild = a

    def preorder(self):
        self.ppreorder(self.root)  
    def ppreorder(self, node):
        if node:
            print(node.data, end=" ")
            self.ppreorder(node.Lchild)
            self.ppreorder(node.Rchild)
    
    def inorder(self):
        self.pinorder(self.root)
    def pinorder(self, node):
        if node:
            self.pinorder(node.Lchild)
            print(node.data, end=" ")
            self.pinorder(node.Rchild)
    
    def postorder(self):
        self.ppostorder(self.root)
    def ppostorder(self, node):
        if node:
            self.ppostorder(node.Lchild)
            self.ppostorder(node.Rchild)
            print(node.data, end=" ")
    
    def level_order(self):
        if self.root is None:
            return
        l = list()
        l.append(self.root)
        while l:
            t = l.pop(0)
            print(t.data, end=" ")
            if t.Lchild:
                l.append(t.Lchild)
            if t.Rchild:
                l.append(t.Rchild)
    
    def insert_after_l(self, x, data):
        self.pinsert_after_l(self.root, x, data)
    def pinsert_after_l(self, node, x, data):
        if node:
            if node.data == x:
                temp = node.Lchild
                node.Lchild = BinaryNode(data)
                node.Lchild.Lchild = temp
            self.pinsert_after_l(node.Lchild, x, data)
            self.pinsert_after_l(node.Rchild, x, data)

    def insert_after_r(self, x, data):
        self.pinsert_after_r(self.root, x, data)

    def pinsert_after_r(self, node, x, data):
        if node:
            if node.data == x:
                temp = node.Rchild
                node.Rchild = BinaryNode(data)
                node.Rchild.Rchild = temp
            self.pinsert_after_r(node.Lchild, x, data)    
            self.pinsert_after_r(node.Rchild, x, data)
        
    def delete_left(self):
        if self.root is None:
            print('empty')
            return None
        else:
            temp = self.root
            while temp.Lchild.Lchild != None:
                temp = temp.Lchild
            del(temp.Lchild)
            temp.Lchild = None


    def delete_right(self):
        if self.root is None:
            print("empty")
            return None
        else:
            temp = self.root
            while temp.Rchild.Rchild != None:
                temp = temp.Rchild
            del(temp.Rchild)
            temp.Rchild = None
            
    def delete_x(self, x):
        if self.root is None:
            print('empty')
            return None
        else:
            self.pdelete(self.root, x)    
    def pdelete(self, node, x):
        if node != None:
            if node.Lchild:
                if node.Lchild.data == x:
                    del(node.Lchild)
                    node.Lchild = None
                    return None
                self.pdelete(node.Lchild, x)
                self.pdelete(node.Rchild, x)
            
            if node.Rchild:
                if node.Rchild.data == x:
                    del(node.Rchild)
                    node.Rchild = None
                    return None
                self.pdelete(node.Lchild, x)
                self.pdelete(node.Rchild, x)
            
            if node.data == x:
                node = None
                return
        
    def delete_left_x(self, x):
        if self.root is None:
            print('empty')
            return
        else:
            self.pdelete_left_x(self.root, x)
    def pdelete_left_x(self, node, x):
        if node != None:
            if node.Lchild:
                if node.Lchild.data == x:
                    if node.Lchild.Lchild != None:
                        del(node.Lchild.Lchild)
                        node.Lchild.Lchild = None
                        return
                self.pdelete_left_x(node.Lchild, x)
                self.pdelete_left_x(node.Rchild, x)
            
            if node.Rchild:
                if node.Rchild.data == x:
                    if node.Rchild.Lchild != None:
                        del(node.Rchild.Lchild)
                        node.Rchild.Lchild = None
                        return
                self.pdelete_left_x(node.Lchild, x)
                self.pdelete_left_x(node.Rchild, x)
            
            if node.data == x:
                if node.Lchild != None:
                    node.Lchild = None
                    return 
    def delete_right_x(self, x):
        if self.root is None:
            print("empty")
        else:
            return self.pdelete_right_x(self.root, x)
    def pdelete_right_x(self, node, x):
        if node != None:
            if node.Lchild:
                if node.Lchild.data == x:
                    if node.Lchild.Rchild != None:
                        del(node.Lchild.Rchild)
                        node.Lchild.Rchild = None
                        return
                self.pdelete_right_x(node.Lchild, x)
                self.pdelete_right_x(node.Rchild, x)
            if node.Rchild:
                if node.Rchild.data == x:
                    if node.Rchild.Rchild != None:
                        del(node.Rchild.Rchild)
                        node.Rchild.Rchild = None
                        return
                self.pdelete_right_x(node.Lchild, x)
                self.pdelete_right_x(node.Rchild, x)
            if node.data == x:
                if node.Rchild != None:
                    node.Rchild = None
                    return
            

