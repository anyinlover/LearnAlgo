#ifndef SEQUENTIAL_SEARCH_ST_H
#define SEQUENTIAL_SEARCH_ST_H

#include "st.h"
#include "utils/linked_list_node.h"

using std::ref;
template<typename Key, typename Value>
class SequentialSearchST : public ST {
public:
    void Put(Key&& key, Value&& val) override
    {
        for (auto x = _first; x != nullptr; x = x.next)
            if (key == x->key) {
                x->value = val;
                return;
            }
        _first = new Node(key, val, _first);
    }

    optional<reference_wrapper<Value>> Get(const Key& key) const override
    {
        for (auto x = _first; x != nullptr; x = x.next)
            if (key == x->key) {
                return ref(x->value);
            }
        return {};
    }

private:
    Node* _first = nullptr;
};

#endif // !SEQUENTIAL_SEARCH_ST_H