#Matplot lib 
import numpy as np
import matplotlib.pyplot as plt

import matplotlib as mplt
print(mplt.__version__)

x_point = np.array([1,2])
y_point = np.array([1,2])
plt.plot(x_point,y_point)
#plt.show()

#For no line
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
#plt.show()


#Multiple points
xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])

plt.plot(xpoints, ypoints, color="red")
plt.show()

#if x not given default is 0,1,2,3,4......
y_point = np.array([1,2,3,4,5,6,7,8,9])
plt.plot(y_point)
plt.show()

#matplotlib markers
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = '+')
plt.show()

# Marker	Description
# 'o'	Circle	
# '*'	Star	
# '.'	Point	
# ','	Pixel	
# 'x'	X	
# 'X'	X (filled)	
# '+'	Plus	
# 'P'	Plus (filled)	
# 's'	Square	
# 'D'	Diamond	
# 'd'	Diamond (thin)	
# 'p'	Pentagon	
# 'H'	Hexagon	
# 'h'	Hexagon	
# 'v'	Triangle Down	
# '^'	Triangle Up	
# '<'	Triangle Left	
# '>'	Triangle Right	
# '1'	Tri Down	
# '2'	Tri Up	
# '3'	Tri Left	
# '4'	Tri Right	
# '|'	Vline	
# '_'	Hline





########
#Order ---> marker, linestyle, color
########



# the linestyle of plot
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linestyle=':')
plt.show()

# '-'	Solid line	
# ':'	Dotted line	
# '--'	Dashed line	
# '-.'	Dashed/dotted line


ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, '^--b') #-----> marker^, linestyle-- , color->b
plt.show()

# Color Syntax	Description
# 'r'	Red	
# 'g'	Green	
# 'b'	Blue	
# 'c'	Cyan	
# 'm'	Magenta	
# 'y'	Yellow	
# 'k'	Black	
# 'w'	White




#markersize/ms-->size, markeredgecolor/mec-->edge color
#markerfacecolor/mfc = color inside edge
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
plt.show()




###########################################################################
                                 #Matplotlib Line
###########################################################################
#Line plots
#marker, Linestyle/ls, color, 

#Style	   Or
# 'solid' (default)	'-'	
# 'dotted'	':'	
# 'dashed'	'--'	
# 'dashdot'	'-.'	
# 'None'	'' or ' '
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker='o', linestyle=':',color = 'red')#ls = 'dotted') #or linestyle=':'
plt.show()




#Line width
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linewidth = '5',ls=':')
plt.show()


#Plotting many liness
#x default , x = 0,1,2,3,4,5
y1 = np.array([1,3,5,7,9])
y2 = np.array([0,2,4,6,8])
plt.plot(y1,'o:r',linewidth = 3)
plt.plot(y2, '^:b',linewidth = 2)
plt.show()


#Draw two lines by specifiyng the x- and y-point values for both lines:
x1 = np.array([1, 2, 3, 4])
y1 = np.array([4, 3, 2, 1])
x2 = np.array([5, 6, 7, 8])
y2 = np.array([8, 7, 6, 5])

plt.plot(x1, y1, x2, y2) #x1--->y1 and x2-->y2
plt.show()



# adding label font(fontdict) , aligning the labels (loc)
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# Key	Meaning	Example
# 'family'	font type	'serif', 'sans-serif','monospace'
# 'color'	font color	'blue', 'darkred', 'green', '#FF00FF', etc.
# 'size'	font size (points)	15, 20, etc.

font_title = {'family':'monospace', 'color':'blue', 'size':10}
fontx = {'family':'serif', 'color':'blue', 'size':12}
fonty = {'family':'serif', 'color':'darkred', 'size':12}

#Title ---> 'left', 'right', and 'center'
plt.title("Car (mileage vs petrol) price comparison",fontdict=font_title, loc = 'left')
#xlabel -----> right , left, 'center'
plt.xlabel("mileage",fontdict=fontx,loc='right')
#ylabel ------> top, bottom, center
plt.ylabel("petrol price",fontdict=fonty,loc='top')

plt.plot(x, y)
plt.show()



#Using grids
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.grid(axis ="y",color="green",linestyle='--',linewidth=0.5) #lines on y displayed
plt.show()

################################################################################
#  Matplotlib Subplot
################################################################################
#plot 1:
x = np.array([2001,2011,2022,2025])
y = np.array([700,2000,5000,6000])

font_title = {'family':'serif', 'color':'black', 'fontsize':14}
fontx = {'family':'serif', 'color':'black', 'size':12}
fonty = {'family':'serif', 'color':'black', 'size':12}

# row, col, index
plt.subplot(1, 2, 1)
plt.plot(x,y,'o:',color='hotpink',ms= 3, mec='black',mfc="hotpink", linewidth = 3)
plt.title("Apple sales",fontdict=font_title, loc='center')
plt.xlabel("year",fontdict=fontx, loc= 'center')
plt.ylabel("pieces (thousands)",fontdict=fonty, loc='center')
plt.grid(axis="x",color='green',linestyle=":",linewidth=0.5)

#plot 2:
x = np.array([2001,2011,2022,2025])
y = np.array([1000,2000,2500,7000])
# row, col, index
plt.subplot(1, 2, 2)
plt.plot(x,y,'^:r',ms= 2, mec='black',mfc="red",linewidth = 2)
plt.title("samsung sales",fontdict=font_title, loc='center')
plt.xlabel("year",fontdict=fontx, loc='center' )
plt.ylabel("pieces (thousands)",fontdict=fonty, loc='center')
plt.grid(color='green',linestyle=":",linewidth=0.5)


plt.subplots_adjust(left=0.15, right=0.9, bottom=0.15, top=0.85, 
                    wspace=0.9, hspace=0.9)
font_title = {'family':'serif', 'color':'Black', 'fontsize':34}
plt.suptitle("Global Phone Sales", fontdict=font_title)
plt.show()
