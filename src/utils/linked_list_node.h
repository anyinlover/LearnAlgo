#ifndef LINKED_LIST_NODE_H
#define LINKED_LIST_NODE_H

template<typename Key, typename Value>
struct Node {
    Node(Key&& key, Value&& value, Node* next)
    {
        _key = key;
        _value = value;
        _next = next;
    }
    Key _key;
    Value _value;
    Node* _next;
};

#endif // !LINKED_LIST_NODE_H