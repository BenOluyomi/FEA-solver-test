import numpy as np
import matplotlib.pyplot as plt
n1 = int(input("Please indicate the number of rows of the matrix: "))
n2 = int(input("Please indicate the number of columns of the matrix: "))
mesh = np.zeros((n1,n2))
print(mesh)
# Input the top boundary values
top =float(input("Boundary condition for the top boundary: "))
if top == 0:
    top = 0.001
mesh[0,:] = [top]
print(mesh)
# Input the bottom boundary values
bot =float(input("Boundary condition for the bottom boundary: "))
if bot == 0:
    bot = 0.001
mesh[n1-1,:] = [bot]
print(mesh)
# Input the left boundary values
left =float(input("Boundary condition for the left boundary: "))
if left == 0:
    left = 0.001
mesh[:,0] = [left]
reassigntopleft =float(input("The top left boundary has currently been assigned two values, if the value belongs to the top boundary enter 1 if it belongs to the left, enter 2: "))
reassignbotleft =float(input("The bottom left boundary has currently been assigned two values, if the value belongs to the bottom boundary enter 1 if it belongs to the left, enter 2: "))
if reassigntopleft == 1:
    mesh[0] = [top]
if reassignbotleft == 1:
    mesh[n1-1] = [bot]
print(mesh)
# Input the right boundary values
right =float(input("Boundary condition for the right boundary: "))
if right == 0:
    right = 0.001
mesh[:,n2-1] = [right]
reassigntopright =float(input("The top right boundary has currently been assigned two values, if the value belongs to the top boundary enter 1 if it belongs to the right, enter 2: "))
reassignbotright =float(input("The bottom right boundary has currently been assigned two values, if the value belongs to the bottom boundary enter 1 if it belongs to the right, enter 2: "))
if reassigntopright == 1:
    mesh[0,n2-1] = top
if reassignbotright == 1:
    mesh[n1-1,n2-1] = bot
print(mesh)
# Calculation (Use Navier-Stokes or some other FEM)
for x in range(0,n1):
    for y in range (0,n2):
        if mesh[x,y] == 0:
            mesh[x,y] = (mesh[x-1,y] + mesh[x+1,y] + mesh[x,y+1] + mesh[x,y-1])/4



print(mesh)

fig = plt.figure()
fig.suptitle('Heat Transfer')    
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.imshow(mesh,interpolation='gaussian')
plt.show()

