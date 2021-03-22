# Trie data structure is an efficient information retrieval data structure can be used for
# providing auto-complete suggestions. http://en.wikipedia.org/wiki/Trie

# -*- coding: utf-8 -*-
# Author: theroyakash <hey@iamroyakash.com>
# Copyright 2021 theroyakash

class TrieNode(object):
    """
    A Trie Node object (basic building blocks for trie data structure).
    See this video for better understanding https://www.youtube.com/watch?v=AXjmTQ8LEoI
    """

    def __init__(self, character: str, endOfWord: bool):
        self.children = [0] * 26    # to establish the parent child relationship
        self.character = None
        self.endOfWord = False


class Trie():
    """
    Trie data structure implementation.
    """

    def __init__(self):
        self.root = TrieNode(character=None, endOfWord=False)

    def add(self, word):
        """
        Inserts a new word into the trie data structure. Setting up the trie and
        adding values are done automatically, users no need to worry.
        Args:
            - word: String word you want to add in to the trie
        """

        current_node = self.root
        for character in word:
            found_in_child = False
            # Search for the character in the children
            for child in current_node.children:
                if child.character == character:
                    # We found the character
                    pass

        current_node.endOfWord = True
