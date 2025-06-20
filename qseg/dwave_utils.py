import time
import dimod
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import networkx as nx
import numpy as np

def dwave_solver(linear, quadratic, private_token, runs=10000, **kwargs):
  """
  Solve a binary quadratic model using D-Wave sampler.

  Parameters:
  linear (dict): Linear coefficients of the model.
  quadratic (dict): Quadratic coefficients of the model.
  private_token (str): API token for D-Wave.
  runs (int): Number of reads for the sampler.

  Returns:
  dimod.SampleSet: Sample set returned by D-Wave sampler.
  float: Connection time.
  float: Embedding time.
  float: Response time.
  """
  vartype = dimod.BINARY
  bqm = dimod.BinaryQuadraticModel(linear, quadratic, 0.0, vartype)
  start_time = time.time()
  dwave_sampler = DWaveSampler(token = private_token, solver={'topology__type': 'pegasus'})
  connection_time = time.time() - start_time

  start_time = time.time()
  sampler = EmbeddingComposite(dwave_sampler)
  embedding_time = time.time() - start_time
  start_time = time.time()
  sample_set = sampler.sample(bqm, num_reads=runs)
  response_time = time.time() - start_time
  return sample_set, connection_time, embedding_time, response_time

def get_linear_quadratic_dict(W):
    """Computes the QUBO matrix for the Minimum Cut problem given a weight matrix W."""
    n = W.shape[0]  # Number of nodes
    linear = {}
    quadratic = {}
    
    for i in range(n):
        linear[i] = np.sum(W[i])  # Diagonal terms (degree of node)
        for j in range(n):
            if i < j and W[i, j]!=0:
                quadratic[(i, j)] = -W[i, j]  # Off-diagonal terms (negative adjacency)
    return linear,quadratic

def annealer_solver(G, private_token, n_samples=2000, **kwargs):
  """
  Solve the Maxcut problem on graph G using a D-Wave annealer.

  Parameters:
  G (networkx.Graph): Graph for which Maxcut is to be solved.
  private_token (str): API token for D-Wave.
  n_samples (int): Number of samples to collect.

  Returns:
  pandas.DataFrame: Dataframe containing samples.
  dict: Dictionary containing information about execution times.
  """
  start_time = time.time()
  w = nx.adjacency_matrix(G).todense()
  linear,quadratic = get_linear_quadratic_dict(w)
  problem_formulation_time = time.time() - start_time
  sample_set, connection_time, embedding_time, response_time = dwave_solver(linear, quadratic, private_token, runs=n_samples)
  info_dict = sample_set.info['timing'].copy()

  start_time = time.time()
  samples_df = sample_set.to_pandas_dataframe()
  sample_fetch_time = time.time() - start_time

  info_dict['problem_formulation_time'] = problem_formulation_time
  info_dict['connection_time'] = connection_time
  info_dict['embedding_time'] = embedding_time
  info_dict['response_time'] = response_time
  info_dict['sample_fetch_time'] = sample_fetch_time
  return samples_df, info_dict