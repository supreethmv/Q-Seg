# Q-Seg: Quantum Annealing-Based Image Segmentation

## Overview
Q-Seg is an innovative unsupervised image segmentation method leveraging quantum annealing, specifically designed for the D-Wave Advantage quantum hardware. It addresses pixel-wise segmentation by formulating it as a graph-cut optimization task. Q-Seg stands out for its scalability and efficiency, surpassing classical methods in runtime performance and offering competitive segmentation quality, particularly in Earth Observation image analysis.

![Q-Seg Pipeline](figures/pipeline_overview.png)
*Figure: Overview of the Q-Seg segmentation pipeline.*

## Features
- Unsupervised segmentation using quantum annealing.
- Efficient use of D-Wave's qubit topology for scalability.
- Superior runtime performance compared to classical optimizers like Gurobi.
- Effective in scenarios with limited labeled data, such as flood mapping and forest coverage detection.

## Getting Started

### Prerequisites
- Python 3.x
- Jupyter Notebook
- Required Python packages: `numpy`, `networkx`, `qiskit`, `dwave-system`

### Installation
Clone the repository and install the required packages:
```
git clone https://github.com/yourusername/q-seg.git
cd q-seg
pip install -r requirements.txt
```

### Running the Example
Navigate to the `examples` directory and open the Jupyter Notebook:
```
cd examples
jupyter notebook q_seg_toy_example.ipynb
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








