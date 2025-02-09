# Matplotlib Snippets
A comprehensive collection of **Matplotlib code snippets** designed to streamline your plotting workflow and unlock advanced customization, with little change made to the code. This repository includes ready-to-use snippets to imporve and customize common plot types (**line plots, bar charts, scatter plots, histograms, pie charts**) to make it just the way you need it to be.
Whether you're a **data scientist, researcher, or engineer**, these snippets will help you create high-quality visualizations efficiently—so you can focus on insights instead of repetitive coding. Contributions are always welcome!

# How to use
All the code snippets in this repository are **free to use, modify, and adapt** for any project. There are no restrictions—just explore the collection, find the snippet that fits your needs, and **copy-paste it directly into your script or notebook**. Each snippet is designed to be **plug-and-play**, meaning you can use them as they are or tweak them to match your specific requirements. Whether you're looking for a quick visualization or an advanced customization, you’re free to use anything and everything in this repo however you like!

# Generate Seperate Legend
This snippet can be use to create a seperate plot with only the legend in it. It removes the lengend from the plot you give in
Here is a general use case outline:
```python


ax = plt.gca()  # Your Plot
# ... (add your plot elements and legend to ax) ...
generate_seperate_legend(ax)  # Call the function to create separate legend
```
