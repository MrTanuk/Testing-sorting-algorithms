### Inventory Management - CarFix

### Problem 
Mechanical workshops in Venezuela face critical challenges in the management of spare parts:  
- Disorganized inventories with hundreds of parts.  
- Difficulty prioritizing items by price, stock or demand  
- Inefficient search times that affect customer service.  

### Objective  
Develop a system that allows:  
1. Sort spare parts by key criteria (price, stock, name) 2.  
2. Optimize inventory and replenishment management  
3. Compare the performance of algorithms for informed decision making.  

## Installation

1. Clone the repository

```bash
git clone git@github.com:MrTanuk/Testing-sorting-algorithms.git
cd Testing-sorting-algorithms
```

2. Install the dependencies

```bash
pip install numpy rich
```

3. Generate CSV File (if not already present):

```bash
python generate_csv.py
```

4. Run the program

```bash
python main.py
```

### System Description  
**Spare Parts Data:**
- Unique ID  
- Part Name  
- Compatibility (Toyota, Ford, Chevrolet, etc.)  
- Price  
- Stock on hand  
- Days until expiration  


**Sorting Algorithms:**
| Criteria | Algorithm | Use Case |  
|----------------|----------------|---------------------------|  
By Price | QuickSort | Identify Expensive Parts | 
| By Stock | InsertionSort | Manage urgent replenishments |  
| By Name | MergeSort | Quick Alphabet Search |  
By Compatibility | BubbleSort | Group parts by vehicle brand | 


**Performance Comparison:**
- All algorithms are tested on the same extended dataset.
- The run time for each algorithm is displayed.

### Benefits  
**For the Shop Floor:**
- 60% reduction in search times  
- Intelligent inventory organization  
- Proactive detection of critical stock
- Intelligent grouping: Quickly find all spare parts for a specific make


**For the Customers:**
- Increased speed of repair service  
- Transparency in parts availability  
- Competitive pricing through efficient management  

### Tools Used  
- Python 3.10+  
- Rich library for interactive tables (CLI)  
- CSV for data management  
- Custom sorting algorithms  