import pdb
import random
import json
import networkx as nx 
from networkx.algorithms import approximation as apxm  
import matplotlib.pyplot as plt 
import sys
import math
import timeit
import copy
from colorama import Fore, Back, Style
from termcolor import colored, cprint
import numpy as np


from avltree import *
from structs import *
from heap import *
#from plot import plot_addition_deletion_times




nodes=7
max_rounds=27

G=nx.empty_graph(nodes)
print ("Empty Graph has ",G. number_of_nodes(), "nodes")
print(G.nodes)

edges_bunch = []    
nodes_bunch = [-1,-1]  



maximal_matching_set=nx.maximal_matching(G) 
maximalG= nx.Graph()
maximal_matching_to_graph(maximalG, maximal_matching_set)
listDegrees_G=Degrees(G)
dict_neighbors_G= dict_avlTreeNeighbors(G)
max_match_avl = AVLTree()
dict_freeNeighbors_G= freeNeighbors(G,maximalG)



Fmax_heap=MaxHeapPair()  
for i in range(0, nodes):
    
    Fmax_heap.insert((G.degree[i],i))


flag=0

#block_size = int(math.sqrt(len(G)))
#counter_array = [0] * (len(G) // block_size + 1)



list_of_structures=[]
list_of_structures.append(listDegrees_G)
list_of_structures.append(dict_neighbors_G)
list_of_structures.append(max_match_avl)
list_of_structures.append(dict_freeNeighbors_G)
list_of_structures.append(Fmax_heap)
list_of_structures.append(flag)
#list_of_structures.append(counter_array)    
#list_of_structures.append(block_size)


               
              

iteration_counters = {
    'addition_total': 0,
    'add_edges_maximal': 0,
    'deletion_total': 0,
    'remove_edges_maximal': 0,
    'aug_paths':0,
    'surrogate' :0
}



count1=0
count2=0




print("Initial count1:", count1, "Initial count2:", count2)

start_time11=time.time()
addition_times=[]
deletion_times=[]

for times in range (1,max_rounds+1):

        if times <= 4:  
            action = random.randint(1,2) 
        else:
            action = random.randint(0,2)


       
    
        if (action==1 or action==2 )  and (count2<=int(nodes*(nodes-1)/2)):

            start_time=time.time()
            graph_add_edge (G,nodes,edges_bunch, nodes_bunch)
            iteration_counters['addition_total'] += 1
            
            print ("Round ", count1, ": Addition of edge (",nodes_bunch[0],", ",nodes_bunch[1],")")
           
            
            list_of_structures = handle_addition (nodes_bunch[0], nodes_bunch[1], G,maximalG, list_of_structures,iteration_counters)
            
            end_time=time.time()
            elapsedtime=end_time-start_time
            addition_times.append(elapsedtime)
            
           
            count1=count1+1
            count2=count2+1
           
            if count2==int(nodes*(nodes-1)/2):
                cprint ("*******Graph is complete*******",'green')
                print()
                break


        if action==0 and count2>=2 :
            start_time2=time.time()
            graph_delete_edge (G, edges_bunch, nodes_bunch)
            iteration_counters['deletion_total'] += 1
            print ("Round ", count1, ": Deletion of edge (",nodes_bunch[0],", ",nodes_bunch[1],")")
        
            
        
            list_of_structures=handle_deletion (nodes_bunch[0], nodes_bunch[1], G, maximalG, list_of_structures,iteration_counters)
        
            end_time2=time.time()
            elapsedtime2=end_time2-start_time2
            deletion_times.append(elapsedtime2)
        
            count1=count1+1
            count2=count2-1



print("Initial count1:", count1, "Initial count2:", count2)

end_time11=time.time()
elapsed_time11=end_time11-start_time11

additionTotal=sum(addition_times)
deletionTotal=sum(deletion_times)        
average_addition_time = sum(addition_times) / len(addition_times)
average_deletion_time = sum(deletion_times) / len(deletion_times)





#print("Maximal matching set is:", end=' '); cprint(f"({maximalG.edges})", 'red')
#print("Maximal matching nodes are: ", end=''); cprint(f"({sorted(list(maximalG.nodes))})", 'red')
#print("New list of degrees is")
#print(list_of_structures[0])
print()
print()

print("Addition Total:", iteration_counters['addition_total'])
print("Deletion Total:", iteration_counters['deletion_total'])
print("Number of added_edges in maximal:", iteration_counters['add_edges_maximal'])
print("Number of removed_edges in maximal:", iteration_counters['remove_edges_maximal'])
print("Augmenting paths:", iteration_counters['aug_paths'])
print("Surrogate:", iteration_counters['surrogate'])
print()
print()

print("addition time:",additionTotal)
print("deletion time:",deletionTotal)
print("Elapsed time:",elapsed_time11,"seconds")
print("average addition time:",average_addition_time)
print("average deletion time:",average_deletion_time)

pos = nx.spring_layout(G)
plt.figure(figsize=(2, 4))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=300)
nx.draw_networkx_edges(G, pos, edgelist=nx.maximal_matching(maximalG), edge_color='red', width=2)
plt.show()



print()
print("----------END----------")
print()
