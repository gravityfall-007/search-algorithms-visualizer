# Search Algorithm Visualizer

## Description

The Search Algorithm Visualizer is an interactive Python application that demonstrates various search algorithms through visual representation. It provides a user-friendly interface for learning and comparing different search techniques, including linear search, binary search, and more advanced algorithms like BFS and DFS.

## Features

- Interactive GUI built with Tkinter
- Visualization of multiple search algorithms:
  - Linear Search
  - Binary Search
  - Jump Search
  - Ternary Search
  - Interpolation Search
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Hash Table Search
- Step-by-step visualization of each algorithm's process
- Information display for time complexity and algorithm characteristics
- Options to generate random arrays or use preset examples
- Dynamic resizing of the visualization window

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- Matplotlib
- NumPy

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required libraries:
3. Clone this repository or download the `search_visualizer.py` file.

## Usage

1. Run the script:


2. The application window will open, presenting you with several options:

- Select a search algorithm from the dropdown menu
- Enter an array of numbers (space-separated) or use the "Generate Random Array" button
- Enter a target value to search for
- Click "Visualize Search" to start the visualization

3. The visualization will display in the lower part of the window, showing each step of the selected algorithm.

4. Information about the selected algorithm, including its time complexity, will be displayed in the info box.

## Algorithm Descriptions

1. **Linear Search**: Sequentially checks each element of the list.
2. **Binary Search**: Efficiently searches a sorted list by repeatedly dividing the search interval in half.
3. **Jump Search**: Jumps ahead by fixed steps to skip some elements, then performs a linear search.
4. **Ternary Search**: Divides the array into three parts and determines which part the element is in.
5. **Interpolation Search**: Improves on binary search for uniformly distributed sorted arrays.
6. **Breadth-First Search (BFS)**: Explores neighbor nodes first, before moving to the next level neighbors.
7. **Depth-First Search (DFS)**: Explores as far as possible along each branch before backtracking.
8. **Hash Table Search**: Uses a hash function to map keys to indices for constant-time average case search.

## Customization

- To add new algorithms, extend the `SearchVisualizerApp` class with new methods and update the `search_functions` dictionary in the `visualize_search` method.
- Modify the `update_visualization` method to change how the search process is displayed.
- Adjust the `time.sleep()` duration in `update_visualization` to control the speed of the animation.

## Contributing

Contributions to improve the visualizer or add new algorithms are welcome. Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open-source and available under the MIT License.
