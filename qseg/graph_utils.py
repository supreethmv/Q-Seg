import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def gaussian_similarity(a, b, sigma = 0.5):
  """
  Calculate the Gaussian similarity score between two values.

  The Gaussian similarity function is often used in image processing and graph-based algorithms
  to measure how close or similar two values (like pixel intensities) are to each other.

  Parameters:
  a (float): The first value.
  b (float): The second value.
  sigma (float): The standard deviation used in the Gaussian function. This parameter controls
                 how quickly the similarity score decreases with the difference between a and b.

  Returns:
  float: The Gaussian similarity score between a and b.
  """
  gaussian_similairity_score = np.exp(-((a - b)**2) / (2 * sigma**2))
  return gaussian_similairity_score


def image_to_grid_graph(gray_img, sigma=0.5):
  """
  Convert a grayscale image to a grid graph with Gaussian similarity as edge weights.

  Parameters:
  gray_img (numpy.ndarray): Grayscale image.
  sigma (float): Parameter for Gaussian similarity.

  Returns:
  list: List of edges with weights for the graph.
  """
  h, w = gray_img.shape
  nodes = np.zeros((h*w, 1))
  edges = []
  nx_elist = []
  min_weight = 1
  max_weight = 0
  for i in range(h*w):
    x, y = i//w, i%w
    nodes[i] = gray_img[x,y]
    if x > 0:
      j = (x-1)*w + y
      weight = 1-gaussian_similarity(gray_img[x,y], gray_img[x-1,y])
      edges.append((i, j, weight))
      nx_elist.append(((x,y),(x-1,y),np.round(weight,2)))
      if min_weight>weight:min_weight=weight
      if max_weight<weight:max_weight=weight
    if y > 0:
      j = x*w + y-1
      weight = 1-gaussian_similarity(gray_img[x,y], gray_img[x,y-1])
      edges.append((i, j, weight))
      nx_elist.append(((x,y),(x,y-1),weight))
      if min_weight>weight:min_weight=weight
      if max_weight<weight:max_weight=weight
  a=-1
  b=1
  if max_weight-min_weight:
    normalized_nx_elist = [(node1,node2,-1*np.round(((b-a)*((edge_weight-min_weight)/(max_weight-min_weight)))+a,4)) for node1,node2,edge_weight in nx_elist]
  elif max_weight==0 and min_weight==0:
    normalized_nx_elist = [(node1,node2,1) for node1,node2,edge_weight in nx_elist]
  else:
    normalized_nx_elist = [(node1,node2,-1*np.round(edge_weight,4)) for node1,node2,edge_weight in nx_elist]
  return normalized_nx_elist


def draw(G, image):
  """
  Draw the graph G with the given image as node colors.

  Parameters:
  G (networkx.Graph): Graph to be drawn.
  image (numpy.ndarray): Grayscale image for node colors.
  """
  pixel_values = image
  plt.figure(figsize=(min(12,2*image.shape[0]),min(12,2*image.shape[0])))
  default_axes = plt.axes(frameon=True)
  pos = {(x,y):(y,-x) for x,y in G.nodes()}
  nx.draw_networkx(G,
                  pos=pos,
                  node_color=1-pixel_values,
                  with_labels=True,
                  node_size=1200,
                  cmap=plt.cm.Greys,
                  alpha=0.5,
                  ax=default_axes)
  nodes = nx.draw_networkx_nodes(G, pos, node_color=1-pixel_values,
                  node_size=1200,
                  cmap=plt.cm.Greys)
  nodes.set_edgecolor('k')
  edge_labels = nx.get_edge_attributes(G, "weight")
  nx.draw_networkx_edge_labels(G,
                              pos=pos,
                             edge_labels=edge_labels)


def draw_graph_cut_edges(G, image, cut_edges):
  """
  Draw the graph G with the given image as node colors, with the cut edges depicted as red dashed lines.

  Parameters:
  G (networkx.Graph): Graph to be drawn.
  image (numpy.ndarray): Grayscale image for node colors.
  cut_edges (list): Each tuple in the list contains two nodes corresponds to an edge that is cut.
  """
  pixel_values = image
  plt.figure(figsize=(min(12,2*image.shape[0]),min(12,2*image.shape[0])))
  default_axes = plt.axes(frameon=True)
  pos = {(x,y):(y,-x) for x,y in G.nodes()}
  nx.draw_networkx(G,
                  pos=pos,
                  node_color=1-pixel_values,
                  with_labels=True,
                  node_size=1200,
                  cmap=plt.cm.Greys,
                  alpha=0.8,
                  ax=default_axes)
  nodes = nx.draw_networkx_nodes(G, pos, node_color=1-pixel_values,
                  node_size=1200,
                  cmap=plt.cm.Greys)
  nodes.set_edgecolor('k')
  nx.draw_networkx_edges(G,
                         pos=pos,
                         edgelist=cut_edges,
                         width=6,
                         alpha=0.5,
                         edge_color="r",
                         style="dashed")
  edge_labels = nx.get_edge_attributes(G, "weight")
  nx.draw_networkx_edge_labels(G,
                               pos=pos,
                               edge_labels=edge_labels)