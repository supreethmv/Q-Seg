import time
import dimod
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
from qiskit_optimization.applications import Maxcut
import networkx as nx

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
  w = -1 * nx.adjacency_matrix(G).todense()
  max_cut = Maxcut(w)
  qp = max_cut.to_quadratic_program()
  linear = qp.objective.linear.coefficients.toarray(order=None, out=None)
  quadratic = qp.objective.quadratic.coefficients.toarray(order=None, out=None)
  linear = {int(idx):-round(value,2) for idx,value in enumerate(linear[0])}
  quadratic = {(int(iy),int(ix)):-quadratic[iy, ix] for iy, ix in np.ndindex(quadratic.shape) if iy<ix and abs(quadratic[iy, ix])!=0}
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