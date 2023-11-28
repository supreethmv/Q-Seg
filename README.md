# Q-Seg: Quantum Annealing-based Unsupervised Image Segmentation

## Overview
Q-Seg is a novel unsupervised image segmentation method leveraging quantum annealing, specifically designed for the existing D-Wave Advantage quantum hardware. It addresses pixel-wise segmentation by formulating it as a graph-cut optimization task. Q-Seg stands out for its scalability and efficiency, surpassing classical methods in runtime performance and offering competitive segmentation quality, particularly in Earth Observation image analysis.

![Q-Seg Overview](figures/overview_pipeline.png)
*Figure: Overview of the Q-Seg algorithm.*

## Features
- Unsupervised segmentation using quantum annealing.
- Efficient use of D-Wave's qubit topology for scalability.
- Superior runtime performance compared to classical optimizers like Gurobi.
- Effective in scenarios with limited labeled data, such as flood mapping and forest coverage detection.

## Operational Pipeline of Q-Seg

The process of Q-Seg utilizing the D-Wave quantum annealer is illustrated in the figure below. The pipeline consists of several key steps:

1. **Converting the Image to Graph**: The image is first translated into an undirected, weighted, connected grid-graph wtih the pixels correspond to vertices and the edge weights are assigned between neighboring pixels using an appropriate similarity metric.
2. **Reformulating the Minimum Cut Problem**: The segmentation task is converted into a Quadratic Unconstrained Binary Optimization (QUBO) problem.
2. **Remote Access Authentication**: A private token is used for secure remote access to the D-Wave quantum annealer.
3. **Qubit Mapping**: The `minorminer` tool maps the logical qubits in the QUBO to the physical qubits in the D-Wave hardware.
4. **Problem Submission and Queuing**: The problem instance is transmitted over the internet and queued on the shared D-Wave device.
5. **Quantum Annealing**: The Quantum Processing Unit (QPU) on the D-Wave device performs the annealing process.
6. **Solution Extraction**: The retrieval of the sample set produced by the QPU and extracting the optimal solution based on the lowest energy state.
7. **Solution Decode**: The final step involves lowest energy binary solution string being decoded into a binary segmentation mask.

![Q-Seg Operational Pipeline](figures/operational_pipeline.png)
*Figure: Operational pipeline of Q-Seg using D-Wave quantum annealer.*

## Getting Started

### Prerequisites
- Python 3.10
- Jupyter Notebook
- Required Python packages: `numpy`, `networkx`, `qiskit`, `dwave-system`

### Installation
Clone the repository and install the required packages:
```
git clone https://github.com/yourusername/Q-seg.git
cd Q-seg
pip install -r requirements.txt
```

### Running the Example
Navigate to the `examples` directory and open the Jupyter Notebook:
```
cd examples
jupyter notebook q_seg_pipeline.ipynb
```

Follow the instructions in the notebook to perform image segmentation on a sample grayscale image.

## Repository Structure

```
Q-Seg/
│
├── qseg/ # Source code for Q-Seg
│ ├── init.py
│ ├── graph_utils.py
│ ├── dwave_utils.py
│ └── utils.py
│
├── examples/ # Jupyter notebook with example usage
│ └── q_seg_pipeline.ipynb
│
├── data/ # Sample data 
│ └── sample_image.jpg
│
├── figures/ # Figures and diagrams
│ └── pipeline_overview.png
│
├── requirements.txt # List of Python package dependencies
└── README.md # Documentation and usage instructions
```

## Project Structure

### Modules in the `qseg` Package
- **graph_utils.py**: Contains `image_to_grid_graph` and `draw` functions for graph-related operations.
- **dwave_utils.py**: Includes `dwave_solver` and `annealer_solver` functions, dedicated to D-Wave specific operations and quantum annealing.
- **utils.py**: Features the `decode_binary_string` function, useful for general utility purposes across the project.

### Notebook
- **q_seg_pipeline.ipynb**: Located in the `examples` directory, this Jupyter notebook demonstrates the usage of Q-Seg functions on a toy example, providing a step-by-step walkthrough of the algorithm.

### Data and Figures Directories
- Store any specific data used in the notebook in the `data` directory.
- Place figures and diagrams for documentation in the `figures` directory.

### Dependencies
- List all required dependencies in the `requirements.txt` file, such as `qiskit_optimization`, `pylatexenc`, `dwave-ocean-sdk`, and `gurobipy`.



## Citation
If you find Q-Seg useful in your research, please consider citing our paper:
```
Citation details here...
```


## License
Describe the license under which your project is released.


## Contact
Your Contact Information


<!--## Contributors-->

<!--[![Author1](path_to_thumbnail1.jpg)](https://author1website.com)-->
<!--[![Author2](path_to_thumbnail2.jpg)](https://author2website.com)-->

<!--*Click on the images to visit the authors' websites.*-->








