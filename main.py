class Vector:
        def __init__(self, x, y, z):
                self.x = x
                self.y = y
                self.z = z
               
        #V podstatě přetížená print metoda 
        def __repr__(self):
                return 'Vector(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')'
            
        #Sčítání vektorů
        def addVector(self, vecTwo):
            return Vector(self.x + vecTwo.x, self.y + vecTwo.y, self.z + vecTwo.z)
        
        #Odčítání vektorů
        def deductVector(self, vecTwo):
            return Vector(self.x - vecTwo.x, self.y - vecTwo.y, self.z - vecTwo.z)
        
        #Skalární součin vektorů
        def scalarVector(self, vecTwo):
            return Vector(self.x * vecTwo.x, self.y * vecTwo.y, self.z * vecTwo.z)

#Fibonacci funkce
def returnFib(num):
    if num in [0, 1]:
        return num
    else:
        return returnFib(num - 1) + returnFib(num - 2)
           
 #Fibonacci into a file
def fibFile(num):
    filename = 'input.txt'
    print('Writing')
    with open(filename, "w") as f:
        f.write(returnFib(num)) 
            
def choices(): 
    #While loop
    while True:
        print("_______________")
        print("1. Vectors")
        print("2. Fibonacci")
        print("3. Fibonacci into a file")
        print("_______________")
        choice = input()
        
        if choice in ['1', '2', '3']:
            return choice
    
choice = int(choices())

match choice:
    case 1:
        print('yes')
        while True:
            print("_______________")
            print("1. Adding Vectors")
            print("2. Deducting Vectors")
            print("3. Skalar multiplication")
            print("_______________")
            choi = input()
            
            if choi in ['1', '2', '3']:
                match choi:
                    case '1':
                        x1 = int(input('Enter first X: '))
                        y1 = int(input('Enter first Y: '))
                        z1 = int(input('Enter first Z: '))
                        x2 = int(input('Enter second X: '))
                        y2 = int(input('Enter second Y: '))
                        z2 = int(input('Enter seconf Z: '))
                        print(Vector(x1, y1, z1).addVector(Vector(x2, y2, z2)))
                        break
                        
                    case '2':
                        x1 = int(input('Enter first X: '))
                        y1 = int(input('Enter first Y: '))
                        z1 = int(input('Enter first Z: '))
                        x2 = int(input('Enter second X: '))
                        y2 = int(input('Enter second Y: '))
                        z2 = int(input('Enter seconf Z: '))
                        print(Vector(x1, y1, z1).deductVector(Vector(x2, y2, z2)))
                        break
                    
                    case '3':
                        x1 = int(input('Enter first X: '))
                        y1 = int(input('Enter first Y: '))
                        z1 = int(input('Enter first Z: '))
                        x2 = int(input('Enter second X: '))
                        y2 = int(input('Enter second Y: '))
                        z2 = int(input('Enter seconf Z: '))
                        print(Vector(x1, y1, z1).scalarVector(Vector(x2, y2, z2)))
                        break
    case 2:
        num = int(input('Enter a number for the Fibonacci: '))
        for i in range(num):
            print(returnFib(i))
    case 3:
        num = int(input('Enter a number for the Fibonacci: '))
        
        with open('input.txt', "w") as f:
            for i in range(num):
                f.write((str(returnFib(i)) + " "))