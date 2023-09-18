import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


# define Matplotlib figure and axis
fig, ax = plt.subplots()


def draw_process(proc: list, y: int, color: str):
    for r in proc:
        ax.add_patch(Rectangle((r[0], y), r[1], 1, facecolor=color))
    plt.arrow(0, y=y, dx=10, dy=0, width=0.05,color='black')
    plt.text(0,y+.25,"P"+str(y))
# create simple line plot







draw_process([(0,3),(4,1),(7,2)],0,'red')
draw_process([(0,4),(4,2),(8,1)],1,'blue')
draw_process([(1,5),(7,3)],2,'green')

# display plot
plt.show()
