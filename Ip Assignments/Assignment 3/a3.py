import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed

class Shape:
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None
    
    
    def translate(self, dx, dy):
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
 

    def scale(self, sx, sy):
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
        
    def rotate(self, deg):
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

        
    def plot(self, x_dim, y_dim):
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()



class Polygon(Shape):

    def __init__(self, A):
        Shape.__init__(self)
        self.A = A

    def translate(self, dx, dy):
        new_mat = self.A + [dx,dy,0]
        return new_mat

    def scale(self,sx,sy=0):
        if sy ==0:
            sy = sx
        x_mean = self.A[:0].mean()
        y_mean = self.A[:1].mean()
        self.A = (self.A * [sx, sy, 1]) - [x_mean, y_mean, 0]
        return self.A

 

    def rotate(self, deg, rx = 0, ry = 0):
        Shape.rotate(self,deg)
        self.A = np.cross(self.A,self.T_r)
        return self.A


    

    def plot(self):
        pass


class Circle(Shape):
    def __init__(self, x=0, y=0, radius=5):
        self.x = x
        self.y = y
        self.radius = radius



    
    def translate(self, dx, dy):
        self.x = dx
        self.y = dy
        return self.x,self.y

        
    def scale(self, sx):
        pass
 
    
    def rotate(self, deg, rx = 0, ry = 0):

        pass
 
    
    def plot(self):
        pass
        

if __name__ == "__main__":
    n = int(input("verbose? 1 for plot, 0 otherwise "))
    for i in range(int(input("Enter the number of test cases"))):
        if n ==1:
            pass
        else:
            typ = int(input("Enter the shape 0: for polygon and 1 for circle"))
            if typ ==0:
                poly = []
                num_side = int(input("Enter the Number of Sides"))
                for i in range(num_side):
                    l = list(map(float, input("Enter x and y: ").split()))
                    poly.append(l)
                poly = np.array(poly)
                poly = np.append(poly, np.ones((num_side, 1)), axis=1)
                p = Polygon(poly)
                for j in range(int(input("Enter the no of queries"))):
                    if j ==0:
                        print("Enter Query:")
                        print("1) R deg (rx) (ry)")
                        print("2) T dx (dy)")
                        print("3) S sx (sy)")
                        print("4) P")
                    li = list(map(str,input().split()))
                    if li[0] == "T":
                        new_poly = p.translate(float(li[1]),float(li[2]))
                        p = Polygon(new_poly)
                        for a in new_poly[:0]:
                            print(a,end=" ")
                        for b in new_poly[:1]:
                            print(b,end=" ")
                    elif li[0] =="R":
                        pass
                    elif li[0] =="S":
                        if len(li) ==3:
                            new_poly = p.scale(int(li[1]),int(li[2]))
                            p = Polygon(new_poly)
                        else:
                            new_poly = p.scale(int(li[1]))
                            p = Polygon(new_poly)
                        for a in new_poly[:, 0]:
                            print(a, end=" ")
                        for b in new_poly[:, 1]:
                            print(b, end=" ")

                    elif li[0] =="P":
                        pass



