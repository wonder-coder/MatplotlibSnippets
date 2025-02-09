# Matplotlib Snippets
A comprehensive collection of **Matplotlib code snippets** designed to streamline your plotting workflow and unlock advanced customization, with little change made to the code. This repository includes ready-to-use snippets to imporve and customize common plot types (**line plots, bar charts, scatter plots, histograms, pie charts**) to make it just the way you need it to be.
Whether you're a **data scientist, researcher, or engineer**, these snippets will help you create high-quality visualizations efficiently—so you can focus on insights instead of repetitive coding. Contributions are always welcome!

# How to use
All the code snippets in this repository are **free to use, modify, and adapt** for any project. There are no restrictions, just explore the collection, find the snippet that fits your needs, and **copy-paste it directly into your script or notebook**. Each snippet is designed to be **plug-and-play**, meaning you can use them as they are or tweak them to match your specific requirements. Whether you're looking for a quick visualization or an advanced customization, you’re free to use anything and everything in this repo however you like!

## Generate Seperate Legend
This snippet can be use to create a seperate plot with only the legend in it. It removes the lengend from the plot you give it.
Here is a general use case outline:
```python
import matplotlib.pyplot as plt

def generate_seperate_legend(ax): # you can copy and paste this function into your code
    handles, labels = ax.get_legend_handles_labels()
    fig_legend = plt.figure(figsize=(3, 3))
    ax_legend = fig_legend.add_subplot(111)

    ax_legend.legend(handles, labels, loc="center")
    ax.get_legend().remove()

    ax_legend.grid(False)
    for spine in ["top", "bottom", "left", "right"]:
        ax_legend.spines[spine].set_visible(False)
    ax_legend.set_xticks([])
    ax_legend.set_yticks([])

    plt.show()


ax = plt.gca()  # Your Plot
# ... (add your plot elements and legend to ax) ...
generate_seperate_legend(ax)  # Call the function to create separate legend
```
