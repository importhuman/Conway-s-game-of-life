import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import numpy as np 
# import sys


#Force printing of entire array in terminal
# np.set_printoptions(threshold=sys.maxsize)

grid = np.zeros((11,11), dtype=np.int16) #Create 100*100 array of zeroes

def neighbors(x,y):
	#cell = grid[x,y]
	n_cells = [grid[x-1, y+1], grid[x, y+1], grid[x+1, y+1], 
				grid[x-1, y], grid[x+1, y], 
				grid[x-1, y-1], grid[x, y-1], grid[x+1, y-1]]
	return sum(n_cells)

grid[3:6,5]=1
print(grid)

newgrid = grid.copy()

#Rules
for x in range(10):
	for y in range(10):
		if grid[x,y]==0:
			if neighbors(x,y)==3:
				newgrid[x,y]=1
		else:
			if neighbors(x,y)<2 or neighbors(x,y)>3:
				newgrid[x,y]=0

print(newgrid)
#To get the current axes
ax = plt.gca()

#To make x and y axis tick labels invisible
ax.set_xticklabels([])  
ax.set_yticklabels([])

#To make x and y axis ticks invisible
ax.set_xticks([])
ax.set_yticks([])

# print(grid)  #prints the array in terminal

plt.imshow(grid, cmap='binary') #create grid, 0=white, 1=black #DO THIS AFTER MODIFYING THE ARRAY TO REFLECT CHANGES
plt.show() #show the plot in a new window
print("done")

# ---------------Old code------------------------

# plt.plot([1,2,3,4],[1,4,2,3])
# plt.grid(True)
# plt.show()


#Make a grid
# plt.grid(b=None, which='both', axis='both', linestyle='-', linewidth=1)


# #Make the tick labels invisible
# ax = plt.gca()
# ax.set_xticklabels([])
# ax.set_yticklabels([])

# plt.show()
