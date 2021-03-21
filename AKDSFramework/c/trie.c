#include <Python.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ALPHABET_SIZE 26

typedef struct TrieNode{
    struct TrieNode *children[ALPHABET_SIZE];
    char character;
    bool isEnd;
} TrieNode;


/*
Create a Empty node. When Inserting any word it'll be invoked implicitly.
*/
static TrieNode* createNode(){

    TrieNode *node;
    node = malloc(sizeof(TrieNode));
    node->isEnd = false;

    int i = 0;
    while (i < ALPHABET_SIZE){
        node->children[i] = NULL;
        i++;
    }

    return node;
}


/*
Trie inserting a new word. It'll have a python interface binding.
*/
static PyObject* insertWord(PyObject* self, PyObject* args){
    /*----Addition of the word done by recursively----*/
    

}