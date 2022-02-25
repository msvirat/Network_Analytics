# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 16:01:02 2021

@author: Sathiya vigraman M
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

network_df = pd.read_csv('network_anal/routes.csv', nrows=50)

#network_test = network_df.iloc[:50, :]
network_df.columns = ['airline', 'ID', 'source_airport', 'source_id', 'destination', 'destination_id', 'code_share', 'stops', 'equipment']

import networkx as nx 


G = nx.Graph()

#edge list--start and end

FG = nx.from_pandas_edgelist(network_df, source = 'source_airport', target = 'destination', edge_attr=True)

FG.nodes #city names
FG.edges # each line

nx.draw_networkx(FG, with_labels=True)











