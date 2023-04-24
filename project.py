# %%

# CQC Spring '23 Hackathon

# NOTE: I couldn't access the links in the 
# pdf on the CQC github, so I started from 
# scratch.  As a result, my project is fairly jank

# Part 1
# Run optimization function and minimise cost
# while maximizing energy produced 

# I want to run a Monte Carlo simulation bc IDK what else to do
# PROBLEM: how do I do this?
# ANSWER: Generate random bits, get a random 1 or 0


from qiskit import *
from qiskit.tools.monitor import job_monitor
import numpy as np
import matplotlib.pyplot as plt

#IBMQ.enable_account('ad1d4e7c85af15fe1b1f229e98c688751cfe3d78bb06d9934f8d8b95c539f3f1fc1ea5439abaebd2d08c19fc9a74f78e6446bf49e1e7cbc2ad7b4b6deb717925')
provider = IBMQ.get_provider(hub='ibm-q')


# way to print out from counts objects
def printCounts(countsObj):
  for item in countsObj:
    item = str(item)
    print(item)

# Make a num with x bits (1 or 0)
def makeNum(numCircuits):
  q = QuantumRegister(numCircuits,'q')
  c = ClassicalRegister(numCircuits,'c')
  circuit = QuantumCircuit(q,c)
  circuit.h(q) 
  result = circuit.measure(q,c) 
  backend = provider.get_backend('ibmq_qasm_simulator')
  job = execute(circuit, backend, shots=1)
  counts = job.result().get_counts()
  printCounts(counts)
  return counts

# Should print out a string 1 or 0
makeNum(1)


# Part 2

# Now that we have a way to simulate 
# whether or not a source is making electricty,
# such as simulating weather 
# (i.e. all 1's from 9am-5pm)
# we need a way to simulate how much energy is produced

# I will use weighted Adders here.

# returns a list of qubits
def makeQubits(length):
  # not actually qubits per se, just simulated
  list = []
  for i in range(length):
    number = makeNum(1)
    print(number)
    list.append(number)
  return list

# makeQubits needs to be 1 less than what you want
# additionally, the weights (based off weather)
qubitList = makeQubits(2)
weights = [3.2, 1.7, 5]

for i in range(len(qubitList)):
  print(float(str(qubitList[i])) * weights[i])


# %%
