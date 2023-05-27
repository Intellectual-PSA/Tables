import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()

# Drawing the tables (as rectangles)
table1 = patches.Rectangle((0.2, 0.2), 0.2, 0.2, fill=None)
table2 = patches.Rectangle((0.6, 0.2), 0.2, 0.2, fill=None)

# Adding the tables to the plot
ax.add_patch(table1)
ax.add_patch(table2)

# Drawing lines between the tables and from table 2 to a point in the surrounding area
plt.plot([0.3, 0.7], [0.3, 0.3], 'k-') # line between tables
plt.plot([0.7, 0.7], [0.4, 0.8], 'k-') # line from table 2 to surrounding area

# Labeling the tables
plt.text(0.3, 0.15, '1', horizontalalignment='center')
plt.text(0.7, 0.15, '2', horizontalalignment='center')

# Adjusting the limits and aspect ratio of the plot to ensure that everything fits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

# Displaying the plot
plt.show()
