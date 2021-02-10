#include <list>
#include <iostream>
#include <unordered_map>
#include <utility>
using namespace std;

struct Node {
    int key, val;
    Node* next;
    Node* prev;
    Node(int key, int val): key(key), val(val) {}
};

class LRUCache {
    Node* head;
    Node* end;
    unordered_map<int, Node*> table;
    int capacity;
public:
    LRUCache(int capacity) {
        head = new Node(0, 0);
        end = new Node(0, 0);
        this->capacity = capacity;

    }
    
    int get(int key) {

    }
    
    void put(int key, int value) {

    }
};
