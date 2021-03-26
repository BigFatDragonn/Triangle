#var = int(input())
#x = 1
#var_1 = "#"
#for i in range(0, var):
  #x += 2
  #print((((x - 2) * var_1).center(5," ")).split())
#print(var_2)
side = int(input()) 
c = '#' 
for i in range(side):
    print((c*i).rjust(side-1)+c+(c*i).ljust(side-1))
    
    
    
height = int(input())
base_width = (height * 2) - 1  # formula to obtain the size of the base: y = 2x - 1
for x in range(1, base_width + 1, 2):  # starting with one '#', you need to increase the amount of '#' by 2
    print((x * '#').center(base_width))
