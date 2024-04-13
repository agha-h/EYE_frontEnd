import matplotlib.pyplot as plt
import numpy as np

# Your data
exec_times = {
    'duckModified2': [89.39, 92.45, 90.90, 95.52, 258.98, 95.35],
    'duckModifies': [103.79, 209.40, 331.25, 171.68, 64.47, 56.57],
    'duckProject': [54.996, 56.943, 215.395, 290.959, 226.015, 72.423]  # Converted to seconds
}
threads = [1, 2, 3, 4, 5, 6]
programs = list(exec_times.keys())

# Setup for bar chart
n = len(threads)  # Number of thread counts
x = np.arange(n)  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots(figsize=(12, 8))
rects1 = ax.bar(x - width, exec_times['duckModified2'], width, label='duckModified2')
rects2 = ax.bar(x, exec_times['duckModifies'], width, label='duckModifies')
rects3 = ax.bar(x + width, exec_times['duckProject'], width, label='duckProject')

# Add some text for labels, title, and custom x-axis tick labels, etc.
ax.set_xlabel('Number of Threads')
ax.set_ylabel('Execution Time (seconds)')
ax.set_title('Execution Time by Program Version and Number of Threads')
ax.set_xticks(x)
ax.set_xticklabels(threads)
ax.legend()

# Function to automatically attach a label above each bar showing its height
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

fig.tight_layout()

plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.savefig('./templates/execution_times_bar_chart.png')
plt.show()
