from functools import total_ordering
import heapq
import math

class MaxHeapPair:
    def __init__(self):
        self.heap = []
        self.mapping = {}
    
    def insert(self, pair):
        if pair in self.mapping:
            raise ValueError("Pair already in heap")
        self.mapping[pair] = len(self.heap)
        heapq.heappush(self.heap, (-pair[0], pair[1]))
    
    
    





    
    
    def delete(self, pair):
        if pair not in self.mapping:
           raise ValueError("Pair not in heap")
        index1=self.heap.index((-pair[0],pair[1]))
                
        del self.mapping[pair]        
        last_pair = self.heap.pop()
        
        if index1 != len(self.heap):
            
            self.heap[index1] = last_pair            
            self.mapping[last_pair[1]] = index1            
            parent_index = (index1 - 1) // 2
            
            if index1 > 0 and self.heap[parent_index][0] < last_pair[0]:
                heapq._siftup(self.heap, index1)
            else:
                heapq._siftup(self.heap, index1)
                heapq._siftdown(self.heap, 0, index1)
        
        return self

    def update_key(self, old_pair, new_pair):
        if old_pair not in self.mapping:
            raise ValueError("Pair not in heap")
        self.delete(old_pair)
        self.insert(new_pair)
        return self

    def find_max(self):
        if not self.heap:
            return None
        return (-self.heap[0][0], self.heap[0][1])
    '''
    def _get_children(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        left_child = self.heap[left_child_index] if left_child_index < len(self.heap) else None
        right_child = self.heap[right_child_index] if right_child_index < len(self.heap) else None
        return left_child, right_child
    '''
    def _get_tree_height(self):
        return math.ceil(math.log2(len(self.heap) + 1))

    def search(self, pair):
        if pair in self.mapping:
            return True
        else:
            return False
    
    def print_tree(self):
        if not self.heap:
            return
        height = self._get_tree_height()
        max_width = 2 ** height - 1
        for i in range(height):
            row_width = 2 ** i
            row_padding = " " * (max_width // row_width - 1)
            row_items = []
            for j in range(row_width):
                index = 2 ** i - 1 + j
                item = self.heap[index] if index < len(self.heap) else None
                item_str = f"({-item[0]}, {item[1]})" if item else ""
                row_items.append(item_str)
            print(row_padding.join(row_items))



 






max_heap=MaxHeapPair()

max_heap.insert((5,0))
max_heap.insert((2,1))
max_heap.insert((7,2))
max_heap.insert((4,4))
max_heap.insert((5,5))
max_heap.insert((29,5))
print("heap structure:")
max_heap.print_tree()
max_heap.delete((29,5))
print("heap structure:")
max_heap.print_tree()
max_heap.insert((8,7))
max_heap.print_tree()

