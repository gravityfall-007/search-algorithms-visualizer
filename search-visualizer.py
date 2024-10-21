import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import random
from collections import deque

class SearchVisualizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Search Algorithm Visualizer")

        self.algorithm_var = tk.StringVar(value="Linear Search")
        self.array_var = tk.StringVar(value="1 3 5 7 9 11 13 15")
        self.target_var = tk.StringVar()

        self.create_widgets()
        self.fig, self.ax = plt.subplots(figsize=(12, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=6, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        self.master.grid_rowconfigure(6, weight=1)
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)

        self.master.bind("<Configure>", self.on_resize)

        # Initialize graph for BFS and DFS
        self.graph = {}

        # Initialize hash table
        self.hash_table = {}

    def create_widgets(self):
        algorithms = ["Linear Search", "Binary Search", "Jump Search", "Ternary Search", "Interpolation Search", 
                      "BFS", "DFS", "Hash Table Search"]
        ttk.Label(self.master, text="Select a search algorithm:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        algorithm_combo = ttk.Combobox(self.master, textvariable=self.algorithm_var, values=algorithms)
        algorithm_combo.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        algorithm_combo.bind("<<ComboboxSelected>>", self.on_algorithm_change)

        ttk.Label(self.master, text="Enter space-separated numbers for the array:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(self.master, textvariable=self.array_var, width=30).grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.master, text="Enter the target value to search for:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(self.master, textvariable=self.target_var, width=10).grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        ttk.Button(self.master, text="Visualize Search", command=self.visualize_search).grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")
        ttk.Button(self.master, text="Generate Random Array", command=self.generate_random_array).grid(row=3, column=2, pady=10, sticky="ew")
        ttk.Button(self.master, text="Use Preset Example", command=self.use_preset_example).grid(row=3, column=3, pady=10, sticky="ew")

        self.info_text = tk.Text(self.master, height=4, width=50)
        self.info_text.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

        self.step_label = ttk.Label(self.master, text="")
        self.step_label.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

    def on_resize(self, event):
        self.canvas.draw()

    def on_algorithm_change(self, event):
        self.clear_visualization()
        self.update_info()

    def clear_visualization(self):
        self.ax.clear()
        self.canvas.draw()
        self.step_label.config(text="")

    def update_info(self):
        algorithm = self.algorithm_var.get()
        info = {
            "Linear Search": "Time Complexity: O(n)\nSimple but inefficient for large arrays.",
            "Binary Search": "Time Complexity: O(log n)\nEfficient for sorted arrays.",
            "Jump Search": "Time Complexity: O(√n)\nBalanced between Linear and Binary Search.",
            "Ternary Search": "Time Complexity: O(log3 n)\nDivides array into three parts.",
            "Interpolation Search": "Time Complexity: O(log log n) average, O(n) worst\nEfficient for uniformly distributed sorted arrays.",
            "BFS": "Time Complexity: O(V + E)\nExplores all neighbor nodes at the present depth before moving to the next level.",
            "DFS": "Time Complexity: O(V + E)\nExplores as far as possible along each branch before backtracking.",
            "Hash Table Search": "Time Complexity: O(1) average, O(n) worst\nUses a hash function to map keys to indices."
        }
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(tk.END, info.get(algorithm, ""))

    def generate_random_array(self):
        arr = sorted([random.randint(1, 100) for _ in range(20)])
        self.array_var.set(" ".join(map(str, arr)))

    def use_preset_example(self):
        preset = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
        self.array_var.set(" ".join(map(str, preset)))

    def visualize_search(self):
        self.clear_visualization()
        algorithm = self.algorithm_var.get()
        arr = list(map(int, self.array_var.get().split()))
        target = int(self.target_var.get())

        search_functions = {
            "Linear Search": self.linear_search,
            "Binary Search": self.binary_search,
            "Jump Search": self.jump_search,
            "Ternary Search": self.ternary_search,
            "Interpolation Search": self.interpolation_search,
            "BFS": self.bfs,
            "DFS": self.dfs,
            "Hash Table Search": self.hash_table_search
        }

        search_function = search_functions.get(algorithm)
        if search_function:
            if algorithm in ["Binary Search", "Jump Search", "Interpolation Search"]:
                arr.sort()
            if algorithm in ["BFS", "DFS"]:
                self.create_graph(arr)
            if algorithm == "Hash Table Search":
                self.create_hash_table(arr)
            search_function(arr, target)

    def update_visualization(self, arr, current_indices, found=False, step_text=""):
        self.ax.clear()
        self.ax.set_xlim(0, len(arr))
        self.ax.set_ylim(0, max(arr) + 1)
        self.ax.set_yticks([])
        self.ax.set_xticks(range(len(arr)))
        self.ax.set_xticklabels(arr)

        for i, num in enumerate(arr):
            color = 'green' if i in current_indices and found else 'red' if i in current_indices else 'blue'
            self.ax.bar(i, num, color=color, alpha=0.7)
            self.ax.text(i, num, str(num), ha='center', va='bottom')

        self.step_label.config(text=step_text)
        self.canvas.draw()
        self.master.update()
        time.sleep(0.5)

    def linear_search(self, arr, target):
        for i, num in enumerate(arr):
            self.update_visualization(arr, [i], num == target, f"Checking index {i}")
            if num == target:
                return
        self.update_visualization(arr, [], False, "Target not found")

    def binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            self.update_visualization(arr, [left, mid, right], arr[mid] == target, f"Checking index {mid}")
            if arr[mid] == target:
                return
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        self.update_visualization(arr, [], False, "Target not found")

    def jump_search(self, arr, target):
        n = len(arr)
        step = int(n ** 0.5)
        prev = 0
        while arr[min(step, n) - 1] < target:
            self.update_visualization(arr, [prev, min(step, n) - 1], False, f"Jumping to index {min(step, n) - 1}")
            prev = step
            step += int(n ** 0.5)
            if prev >= n:
                self.update_visualization(arr, [], False, "Target not found")
                return
        for i in range(prev, min(step, n)):
            self.update_visualization(arr, [i], arr[i] == target, f"Checking index {i}")
            if arr[i] == target:
                return
        self.update_visualization(arr, [], False, "Target not found")

    def ternary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3
            self.update_visualization(arr, [left, mid1, mid2, right], arr[mid1] == target or arr[mid2] == target, 
                                      f"Checking indices {mid1} and {mid2}")
            if arr[mid1] == target:
                return
            if arr[mid2] == target:
                return
            if target < arr[mid1]:
                right = mid1 - 1
            elif target > arr[mid2]:
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1
        self.update_visualization(arr, [], False, "Target not found")

    def interpolation_search(self, arr, target):
        low, high = 0, len(arr) - 1
        while low <= high and arr[low] <= target <= arr[high]:
            if low == high:
                if arr[low] == target:
                    self.update_visualization(arr, [low], True, f"Found at index {low}")
                    return
                self.update_visualization(arr, [], False, "Target not found")
                return
            pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (target - arr[low])))
            self.update_visualization(arr, [low, pos, high], arr[pos] == target, f"Checking index {pos}")
            if arr[pos] == target:
                return
            if arr[pos] < target:
                low = pos + 1
            else:
                high = pos - 1
        self.update_visualization(arr, [], False, "Target not found")

    def create_graph(self, arr):
        self.graph = {i: [] for i in range(len(arr))}
        for i in range(len(arr)):
            if i > 0:
                self.graph[i].append(i-1)
            if i < len(arr) - 1:
                self.graph[i].append(i+1)

    def bfs(self, arr, target):
        visited = set()
        queue = deque([0])
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                self.update_visualization(arr, [node], arr[node] == target, f"Visiting node {node}")
                if arr[node] == target:
                    return
                queue.extend(n for n in self.graph[node] if n not in visited)
        
        self.update_visualization(arr, [], False, "Target not found")

    def dfs(self, arr, target):
        visited = set()
        
        def dfs_recursive(node):
            if node not in visited:
                visited.add(node)
                self.update_visualization(arr, [node], arr[node] == target, f"Visiting node {node}")
                if arr[node] == target:
                    return True
                for neighbor in self.graph[node]:
                    if dfs_recursive(neighbor):
                        return True
            return False
        
        if not dfs_recursive(0):
            self.update_visualization(arr, [], False, "Target not found")

    def create_hash_table(self, arr):
        self.hash_table = {num: i for i, num in enumerate(arr)}

    def hash_table_search(self, arr, target):
        if target in self.hash_table:
            index = self.hash_table[target]
            self.update_visualization(arr, [index], True, f"Found at index {index}")
        else:
            self.update_visualization(arr, [], False, "Target not found")

root = tk.Tk()
app = SearchVisualizerApp(root)
root.mainloop()