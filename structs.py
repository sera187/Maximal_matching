import random
import math
from math import sqrt
import json
import cProfile
import networkx as nx
from operator import itemgetter
from avltree import *
from heap import *
from colorama import Fore, Back, Style
from termcolor import colored, cprint
import time
import timeit




def graph_add_edge(G, nodes, G_edges, G_nodes):
 
    while True:
        u = random.randint(0, nodes-1)
        v = random.randint(0, nodes-1)

        if v != u and not G.has_edge(u, v):
            G.add_edge(u, v)
            G_edges.append((u, v))
            G_nodes[0] = u
            G_nodes[1] = v
            break


     
def graph_delete_edge (G, G_edges,G_nodes):
    i=random.randint (0,len(G_edges)-1)
   
    G_nodes[0], G_nodes[1] = G_edges[i]
    #print(G_edges[i])
    if G.has_edge(G_nodes[0], G_nodes[1]):
        G.remove_edge(G_nodes[0], G_nodes[1])
    elif G.has_edge(G_nodes[1], G_nodes[0]):
        G.remove_edge(G_nodes[1], G_nodes[0])


    G_edges.remove(G_edges[i])
   
        

def maximal_matching_to_graph(maximalG, set):  
    
    for (z,y) in set:
        maximalG.add_edge(z, y)
    print ("Maximal Matching Graph = (",maximalG.number_of_nodes(), ",",maximalG.number_of_edges(),")")
    print("with edges:",set) 



    
def Degrees(G): 
    Degrees = {}
    for i in G:
        Degrees.update({i:G.degree[i]})
  
    return Degrees

def updateDegrees (u,v,G, a_listDegrees):
    for i in (u,v):
        a_listDegrees.update({i:G.degree[i]})
    
    return a_listDegrees




def avlTreeNeighbors(G, vertex):
   
    neighbors = list(G.adj[vertex])
    avlTree = AVLTree()

    for neighbor in neighbors:
        avlTree.insert(neighbor)

    return avlTree

def dict_avlTreeNeighbors(G):
   
    avlNeighbors = {}

    for vertex in G.nodes:
        avlNeighbors[vertex] = AVLTree()
        for neighbor in G.adj[vertex]:
            avlNeighbors[vertex].insert(neighbor)
    
    return avlNeighbors


def printAvl (avlNeighbors):
    for vertex in avlNeighbors.keys():
        print ("vertex (",vertex,"):")
        avlNeighbors[vertex].printTree()








def add_NodeAvlTreeNeighbors(avlNeighbors, new_vertex):
  
    avlNeighbors[new_vertex]=AVLTree()
    
    return avlNeighbors

def delete_NodeAvlTreeNeighbors(avlNeighbors, deleted_vertex):
 
    if deleted_vertex in avlNeighbors.keys():
        avlNeighbors.pop(deleted_vertex)

    for vertex in avlNeighbors.keys():
        if avlNeighbors[vertex].search(deleted_vertex):
            avlNeighbors[vertex].remove(deleted_vertex)
                    
    return avlNeighbors

def add_EdgeAvlTreeNeighbors(avlNeighbors, u, v):
  
  
    if u in avlNeighbors.keys():
        avlNeighbors[u].insert(v)
        
    else:
        add_NodeAvlTreeNeighbors(avlNeighbors, u)
        avlNeighbors[u].insert(v)
   
    if v in avlNeighbors.keys():
        avlNeighbors[v].insert(u)
    else:
       add_NodeAvlTreeNeighbors(avlNeighbors, v)
       avlNeighbors[v].insert(u)
    
    return avlNeighbors



def delete_EdgeAvlTreeNeighbors(avlNeighbors, u, v):

    avlNeighbors[u].remove(v)
    avlNeighbors[v].remove(u)
    
    return avlNeighbors



def print_dict_of_neighbors(a_dict):
    
    for vertex in a_dict.keys():
        print("------------------------")  
        print("vertex (",vertex,"):")
        a_dict[vertex].printTree()
       

def freeNeighbors(G,maximalG): 
    dict_freeNeighbors={} 
    for i in G:
        subdict_freeNeighbors={} 
        for j in G.adj[i]:
            if  j in maximalG:
                free_neighbors=False
                subdict_freeNeighbors.update({j:free_neighbors})
            else:
                free_neighbors=True
                subdict_freeNeighbors.update({j:free_neighbors})
       
        dict_freeNeighbors.update({i:subdict_freeNeighbors})
    
    return dict_freeNeighbors




def addupdate_DictFNG (u,v, dict_freeNeighbors):
    
    dict_freeNeighbors[u].update({v: False})
   
    dict_freeNeighbors[v].update({u:False})
        
    return dict_freeNeighbors





def hasFree(dict,key): 
    has_free=False
   
    if key in dict.keys():
        for key2 in dict.get(key).keys():
            if dict.get(key).get(key2)==True:                
                has_free=True
               
                break
            if has_free==True:
                break
        
    return has_free


def getFree(dict,key): 
    get_free=0
   
    if key in dict.keys():
        for key2 in dict.get(key).keys():
            if dict.get(key).get(key2)==True:
                get_free=key2
             
                break
            if get_free>0:
                break
      
            
    return get_free














def list_of_free_nodes (maximalG, mmGraph): 
    listfn=[] 
    temp=[]
  
    for i in maximalG:
        if i not in mmGraph:
            a=[maximalG.degree[i],i]            
            temp.append(a)
    listfn=sorted(temp, key=itemgetter(0), reverse=True)
            
   
    return listfn




def match(u, v, G, maximalG, a_list_of_structures):
    if not G.has_node(u) or not G.has_node(v):
        
        return a_list_of_structures
    
    maximalG.add_edge (u,v)                   
    for i in (u,v):
        if not a_list_of_structures[2].search (i):
            a_list_of_structures[2].insert(i)             
    for z in (u,v):  
        if a_list_of_structures[4].search((G.degree[z], z)):
            a_list_of_structures[4].delete((G.degree[z], z))  
    
    for w in (u,v):                                
        for i in a_list_of_structures[3].keys():
            if w in a_list_of_structures[3][i].keys():
                a_list_of_structures[3][i][w]=False
    
    return a_list_of_structures






def handle_addition (u, v, G, maximalG, a_list_of_structures,iteration_counters):
   
    
    a_list_of_structures[1]=add_EdgeAvlTreeNeighbors(a_list_of_structures[1], u, v) 
    a_list_of_structures[0]=updateDegrees(u,v,G, a_list_of_structures[0])  
    
    

    for z in (u,v):
        if a_list_of_structures[4].search((G.degree[z]-1, z)): 
            a_list_of_structures[4].update_key((G.degree[z]-1, z), (G.degree[z], z))
     
    addupdate_DictFNG (u,v, a_list_of_structures[3]) 


    vT=None
    
    
    if a_list_of_structures[4].search((G.degree[u], u)) and a_list_of_structures[4].search((G.degree[v], v)):     
        
            a_list_of_structures=match (u, v, G, maximalG, a_list_of_structures)
            iteration_counters['add_edges_maximal'] += 1
            cprint(f"({u} - {v})", 'green')
       
    
    if a_list_of_structures[4].search((G.degree[u], u)) and not a_list_of_structures[4].search((G.degree[v], v)):
    
    
        for i in maximalG.adj[v]:                      
            vT=i
            
        if vT != None:
            
            if a_list_of_structures[3][vT].keys() and u in a_list_of_structures[3][vT].keys():       
                a_list_of_structures[3][vT][u]=False           
                
            if hasFree(a_list_of_structures[3],vT):
                print("bhka has free moy phre arketo xrono") 
                get_free=getFree(a_list_of_structures[3],vT)            
                a_list_of_structures=match(u, v, G, maximalG, a_list_of_structures)
                iteration_counters['add_edges_maximal'] += 1
                cprint(f"({u} - {v})", 'green')
                a_list_of_structures=match(vT, get_free, G, maximalG, a_list_of_structures)
                iteration_counters['add_edges_maximal'] += 1
                cprint(f"({vT} - {get_free})", 'green')
                maximalG.remove_edge(v, vT)           
                iteration_counters['remove_edges_maximal'] += 1
                cprint(f"({v} - {vT})", 'red')
        
            else:    
                a_list_of_structures[3][u][v]=False
                for w in G.adj[u]:
                    a_list_of_structures[3][w][u]=True


    
    if not a_list_of_structures[4].search((G.degree[u], u)) and a_list_of_structures[4].search((G.degree[v], v)):
        temp=u
        u=v
        v=temp
    
        for i in maximalG.adj[v]:                       
            vT=i
             
        if vT != None:
            
            if a_list_of_structures[3][vT].keys() and u in a_list_of_structures[3][vT].keys():       
                a_list_of_structures[3][vT][u]=False           
                
            
            if hasFree(a_list_of_structures[3],vT):                    
                get_free=getFree(a_list_of_structures[3],vT)
                a_list_of_structures=match(u, v, G, maximalG, a_list_of_structures)
                iteration_counters['add_edges_maximal'] += 1
                cprint(f"({u} - {v})", 'green')
                a_list_of_structures=match(vT, get_free, G, maximalG, a_list_of_structures)
                iteration_counters['add_edges_maximal'] += 1
                cprint(f"({vT} - {get_free})", 'green')
                if maximalG.has_edge(v, vT):
                    maximalG.remove_edge(v, vT) 
                    iteration_counters['remove_edges_maximal'] += 1
                    cprint(f"({v} - {vT})", 'red')
                
            else:                                         
                a_list_of_structures[3][u][v]=False
                for w in G.adj[u]:
                    a_list_of_structures[3][w][u]=True
                    
        temp=u
        u=v
        v=temp
        
    a_list_of_structures=bounding_deg_of_free_vertices (u,v,G,maximalG,a_list_of_structures,iteration_counters)
    
   
    return a_list_of_structures


    
def handle_deletion (u, v, G, maximalG, a_list_of_structures,iteration_counters):
        
   
    
    a_list_of_structures[1]=delete_EdgeAvlTreeNeighbors(a_list_of_structures[1], u, v)   
    
    for z in (u,v):
        if a_list_of_structures[4].search((G.degree[z]+1, z)):
            a_list_of_structures[4].update_key((G.degree[z]+1, z), (G.degree[z], z)) 
        
    
    
   
    if (u,v) not in maximalG.edges() or (v,u) not in maximalG.edges():
        a_list_of_structures[3][v].pop(u, "element not found")
        a_list_of_structures[3][u].pop(v, "element not found")
        
    
    
    else:   
        a_list_of_structures[3][v].pop(u, "element not found")
        a_list_of_structures[3][u].pop(v, "element not found")
        
        
        maximalG.remove_edge(u,v)                 
        iteration_counters['remove_edges_maximal'] += 1
        cprint(f"({u} - {v})", 'red')

        a_list_of_structures[2].remove(u)
        a_list_of_structures[2].remove(v)
       
        for z in (u,v): 
            print("deg z:",G.degree[z])
            print("G.size:",sqrt(2*G.size()))
            if hasFree(a_list_of_structures[3], z):
                get_free=getFree(a_list_of_structures[3],z)
                a_list_of_structures= match(z,get_free, G, maximalG, a_list_of_structures)
                iteration_counters['add_edges_maximal'] += 1
                cprint(f"({z} - {get_free})", 'green')
                         
            else:   
                if G.degree[z] > sqrt(2*G.size()):
                    
                    a_list_of_structures= surrogate (z, G, maximalG, a_list_of_structures,iteration_counters)
                    z=a_list_of_structures[5]
                    
                    get_free=getFree(a_list_of_structures[3],z)
                   
                    a_list_of_structures=match(z, get_free, G, maximalG, a_list_of_structures)
                    iteration_counters['add_edges_maximal'] += 1
                    cprint(f"({u} - {v})", 'green')
                    a_list_of_structures[5]=0 
                    
                else: 
                    a_list_of_structures=aug_path(z, G, maximalG, a_list_of_structures,iteration_counters)
                    
    a_list_of_structures=bounding_deg_of_free_vertices (u,v,G,maximalG, a_list_of_structures,iteration_counters)

  


    return a_list_of_structures

def surrogate (u, G, maximalG, a_list_of_structures,iteration_counters):
    cprint("----------------enter surrogate---------------",'blue')
    counter1=0
    counter2=0
    w1=None
    w2=None
    
    for w in G.adj[u]:          
        while counter1==0:
            if a_list_of_structures[3][u][w]==False:
                for wT in maximalG.adj[w]:
                    while counter2==0:
                        if G.degree[wT] <= sqrt(2*G.size()):
                            w1=wT
                            w2=w             
                            counter1+=1
                            counter2+=1
                        else:
                            counter2=1
            counter1=1

    if w1 is not None and w2 is not None:
        a_list_of_structures[5]=w1
        #print(w1)
        maximalG.remove_edge(w2,w1)
        iteration_counters['remove_edges_maximal'] += 1
        
        cprint(f"({w2} - {w1})", 'red')

        a_list_of_structures = match(u,w2,G, maximalG, a_list_of_structures)
        iteration_counters['add_edges_maximal'] += 1
        cprint(f"({u} - {w2})", 'green')
        
        iteration_counters['surrogate'] += 1
    return a_list_of_structures                


def aug_path(u, G, maximalG, a_list_of_structures,iteration_counters):
    print("----enter aug-----")
    counter1=0
    
    if G.adj[u]=={} and u in maximalG.nodes:
        maximalG.remove_node(u)
        a_list_of_structures[4].insert((G.degree[u],u))
        
    else:
        for w in G.adj[u]:
            
            if a_list_of_structures[3][u][w]==False:
                for w1 in maximalG.adj[w]:
                    
                    if counter1==0:
                        
                        if hasFree(a_list_of_structures[3], w1):
                            x=getFree(a_list_of_structures[3],w1)
                            wT=w
                            wT1=w1
                            counter1=counter1+1
          
        if counter1==1:
            a_list_of_structures = match(u,wT, G, maximalG, a_list_of_structures)
            iteration_counters['add_edges_maximal'] += 1
            cprint(f"({u} - {wT})", 'green')
            a_list_of_structures = match(wT1,x, G, maximalG, a_list_of_structures)
            iteration_counters['add_edges_maximal'] += 1
            cprint(f"({wT1} - {x})", 'green')
            
            maximalG.remove_edge(wT,wT1)
            iteration_counters['remove_edges_maximal'] += 1
            cprint(f"({wT} - {wT1})", 'red')
            iteration_counters['aug_paths'] += 1
        else:
             maximalG.remove_node(u)
             a_list_of_structures[2].remove(u)
             a_list_of_structures[4].insert((G.degree[u],u))
             
             for w in G.adj[u]:
                 a_list_of_structures[3][w][u]=True
   
    return a_list_of_structures

                     
def bounding_deg_of_free_vertices (u,v,G,maximalG,a_list_of_structures,iteration_counters):
    
    a_tuple=[]
    
    if a_list_of_structures[4].find_max():
        #print(a_list_of_structures[4].print_tree())
        #print(a_list_of_structures[4].find_max())
        a_tuple1=[]
        a_tuple1=a_list_of_structures[4].find_max()
        a_tuple.append(a_tuple1[1])
        #print(a_tuple1)
   
   


    for z in a_tuple: 
        if G.degree[z] > sqrt(2*G.size()):
            print("--------exist-----")
            a_list_of_structures= surrogate (z, G, maximalG, a_list_of_structures,iteration_counters)
            z=a_list_of_structures[5]
            
            get_free=getFree(a_list_of_structures[3],z)    
           
            a_list_of_structures = match(z,get_free,G,maximalG, a_list_of_structures)
            iteration_counters['add_edges_maximal'] += 1
           
            a_list_of_structures=aug_path(z, G, maximalG, a_list_of_structures,iteration_counters)
            
            a_list_of_structures[5]=0 
          
    return a_list_of_structures

