sequence_map = {
    "Linear Search": ["Binary Search"],
    "Binary Search": ["BST", "Segment Tree"],
    "Sorting Basics": ["Merge Sort", "Quick Sort"],
    "Merge Sort": ["Quick Sort"],
    "Quick Sort": ["Heap Sort", "DP Basics"],
    "Heap Sort": ["Graphs Basics"],
    "BST": ["Graphs Basics"],
    "Graphs Basics": ["DFS", "BFS"],
    "DFS": ["DP Basics"],
    "BFS": ["Shortest Path"],
    "DP Basics": ["Knapsack", "LIS"]
}


def predict_next(topic):
    if topic in sequence_map:
        return sequence_map[topic][0]
    return None    
