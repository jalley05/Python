import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np
import random

NUM_VALUES = 10

# Figure
#fig, axs = plt.subplots( 1, 2, figsize=(10,5), sharey=False, sharex=False, tight_layout=True)
fig = plt.figure(figsize=(15,5))
gs = plt.GridSpec(1, 2, width_ratios=[1, 10])
ax0 = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1])

# Queue to hold values
x = []

def quitCallback():
    print("Quit")

#for i in range(0, NUM_VALUES):
while True:
    new = random.randint(0, NUM_VALUES)
    x.append(new)

    count, bins, bars = ax0.hist(x, len(x), color="blue",\
        alpha=0.9, density=1, align="left", orientation="horizontal")

    ax1.clear()
    ax1.plot(x)

    # Draw histo
    plt.pause(0.01)

    if len(x) > NUM_VALUES:
        x.pop(0)

    # Clear the histo
    t = [b.remove() for b in bars]


quitBtn = Button(quitCallback())

plt.show()
