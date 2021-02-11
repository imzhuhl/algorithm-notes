#include <list>
#include <iostream>
#include <unordered_map>
#include <utility>
using namespace std;

struct Node {
    int key, val;
    Node* next = nullptr;
    Node* prev = nullptr;
    Node(int key, int val): key(key), val(val) {}
};

class LRUCache {
    Node* head_ = nullptr;
    Node* end_ = nullptr;
    unordered_map<int, Node*> table_;
    int capacity_;
public:
    LRUCache(int capacity) {
        head_ = new Node(0, 0);
        end_ = new Node(0, 0);
        head_->next = end_;
        end_->prev = head_;
        capacity_ = capacity;
    }
    
    int get(int key) {
        if (table_.find(key) == table_.end()) return -1;
        Node* tg_node = table_[key];
        remove_node_from_linklist(tg_node);
        insert_head(tg_node);
        return tg_node->val;
    }
    
    void put(int key, int value) {
        Node* tg_node = nullptr;
        if (table_.find(key) == table_.end()) {
            if (table_.size() >= capacity_) {
                tg_node = end_->prev;
                remove_node_from_linklist(tg_node);
                table_.erase(tg_node->key);
                delete tg_node;
                tg_node = nullptr;
            }
            tg_node = new Node(key, value);
            insert_head(tg_node);
            table_[key] = tg_node;
        } else {
            tg_node = table_[key];
            tg_node->val = value;
            move_to_head(tg_node);
        }
    }

    void remove_node_from_linklist(Node* node) {
        Node* pre_node = node->prev;
        Node* nxt_node = node->next;
        pre_node->next = nxt_node;
        nxt_node->prev = pre_node;
    }

    void insert_head(Node* node) {
        Node* t = head_->next;
        head_->next = node;
        node->prev = head_;
        node->next = t;
        t->prev = node;
    }

    void move_to_head(Node* node) {
        remove_node_from_linklist(node);
        insert_head(node);
    }

};
