#ifndef TREE_NODE_H
#define TREE_NODE_H

template<typename Key, typename Value>
struct Node {
    Node(Key&& key, Value val, size_t n)
    {
        _key = key;
        _val = val;
        _n = n;
    }
    ~Node()
    {
        delete _left;
        delete _right;
    }

    Key _key;
    Value _val;
    Node* _left = nullptr;
    Node* _right = nullptr;
    size_t _n;
};

#endif // !TREE_NODE_H