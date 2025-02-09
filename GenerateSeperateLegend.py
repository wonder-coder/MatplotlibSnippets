import matplotlib.pyplot as plt

def generate_seperate_legend(ax):
    """
    Creates a separate figure for the legend of a plot.

    Args:
        ax: The matplotlib Axes object containing the plot.
    
    Returns:
        None
    """
    
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
