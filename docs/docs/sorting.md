# Sorting

AKDSFramework supports multiple sorting techniques. Among them bubble sort, insertion sort and heapsort is available currently.

For bubble sort and insertion sort we maintain a dictionary of internal array positions for future use, If you don't want to store each internal state of array simply mention `maintain_iter_dict` = `False`

You can also visualize without maintaining a dictionary by using flag `vizualize` = `True`. Both are set `False` by default.

Below is an example of using the internal state dictionary animating each step of bubble sort.
```python
from AKDSFramework.applications.sorting import bubblesort, insertionsort, heapsort

# For visualization and sorting
from matplotlib import pyplot as plt
import matplotlib.animation as animation

a = [x + 1 for x in range(50)]
random.seed(time.time())
random.shuffle(a)

a, iter_dict = bubblesort(a, False, True)

def get_array_generator(iter_dict):
    for key in iter_dict:
        yield iter_dict[key]

generator = get_array_generator(iter_dict)

fig, ax = plt.subplots()
ax.set_title("Bubble Sort animation")
bar_rects = ax.bar(range(len(a)), a, align="edge")

# Set axis limits. Set y axis upper limit high enough that the tops of the bars won't overlap with the text label.
N = len(a)
ax.set_xlim(0, N)
ax.set_ylim(0, int(1.5 * max(a)))

text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

iteration = [0]

def update_fig(A, rects, iteration):
    for rect, val in zip(rects, A):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text("# of operations: {}".format(iteration[0]))

anim = animation.FuncAnimation(fig, func=update_fig,
    fargs=(bar_rects, iteration), frames=generator, interval=1,
    repeat=False)
plt.show()
```
