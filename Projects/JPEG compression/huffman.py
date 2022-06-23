import pickle
from collections import Counter


class Node(object):
    """
        Module for createing Trees
    """

    def __init__(self, left = None, right = None):
        """
            Constuctor
            
            params:
                left: Left node
                right: Right node
        """

        self.left = left
        self.right = right


    def children(self):
        return (self.left, self.right)


    def nodes(self):
        return (self.left, self.right)


    def __str__(self):
        return '%s - %s' % (self.left, self.right)


class HuffmanEncoder():

    def __init__(self, values: list) -> None:
        """
            Constructor
            
            params:
                values (list): list of values to be encoded
        """
        
        # Calculate frequencies
        self.frequencies = dict(Counter(values)).items()

        # Sort frequencies
        self.frequencies = sorted(self.frequencies, key = lambda x: x[1], reverse = True)

        # Convert dictionary as list of tuples
        frequencies = [(char, freq) for char, freq in self.frequencies]

        # Create nodes and then the Huffman Tree
        self.create_nodes()
        self.tree = self.construct_huffman_tree(self.nodes[0][0])
    

    def create_nodes(self):
        """ Creates and initializes nodes to be later used in the huffman tree """

        # Create nodes
        self.nodes = self.frequencies
        while len(self.nodes) > 1:

            # Extract two last nodes
            (key1, freq1) = self.nodes[-1]
            (key2, freq2) = self.nodes[-2]

            # Remove extracted nodes from the list
            self.nodes = self.nodes[:-2]

            # Create a tree with the two extracted nodes and the sum of their frequencies
            node = Node(key1, key2)
            self.nodes.append((node, freq1 + freq2))

            # Sort the nodes based on their frequencies DESC
            self.nodes = sorted(self.nodes, key = lambda x: x[1], reverse = True)
    

    # Main function implementing huffman coding
    def construct_huffman_tree(self, node: Node, left = True, binString = ''):
        """
            Main implementation of the Huffman Coding algorithm which recursively constructs the tree

            params:
                node (Node): Node to be used in the tree
                left (Bool): Boolean indicating if the node is the left or right child of its parent
                binString (String): String containing the binary representation of the node
        """

        if type(node) is int:
            return {node: binString}

        (l, r) = node.children()    # Get left and right children
        d = dict()

        # Add left and right leafs to the dictionary (recursively)
        d.update(self.construct_huffman_tree(l, True, binString + '0'))
        d.update(self.construct_huffman_tree(r, False, binString + '1'))

        return d


    def print(self):
        """
            Pretty print of the codings and their corresponding values
        """

        print(' Char | Huffman code ')
        print('---------------------')
        for (char, frequency) in self.frequencies:
            print(' %-4r |%12s' % (char, self.tree[char]))
    

    def save_tree(self, filename = 'tree'):
        """ Save Tree as pickel """

        with open(f'{filename}.pkl', 'wb') as file:
            pickle.dump(self.tree, file)
    

    def save_self(self, filename = 'self'):
        """ Save Tree as pickel """

        with open(f'{filename}.pkl', 'wb') as file:
            pickle.dump(self.tree, file)







if __name__ == '__main__':

    values = [8, 8, 34, 5, 10, 34, 6, 43, 127, 10, 10, 8, 10, 34, 10]
    HuffmanEncoder(values).print()