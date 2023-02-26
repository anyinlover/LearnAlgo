#ifndef BINARY_SEARCH_TREE_ST_H
#define BINARY_SEARCH_TREE_ST_H

#include "st.h"
#include <stdexcept>

template<typename Key, typename Value>
struct Node {
    Node(Key&& key, Value&& val)
    {
        _key = key;
        _val = val;
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
    size_t _n = 1;
};

template <typename Key, typename Value>
class BST : public ST<Key, Value> {
public:
    BST() = default;
    ~BST()
    {
        delete _root;
    }

    void Put(Key&& key, Value&& val) override
    {
        _root = Put(_root, std::forward<Key>(key), std::forward<Value>(val));
    }

    Value& Get(const Key& key) const override
    {
        Node<Key, Value>* x = Get(_root, key);
        if (x == nullptr)
            throw std::out_of_range("no key");
        return x->_val;
    }

    void Delete(const Key& key) noexcept override
    {
        _root = Delete(_root, key);
    }

    bool Contains(const Key& key) const noexcept override
    {
        Node<Key, Value>* x = Get(_root, key);
        return x == nullptr ? false : true;
    }

    size_t Size() const noexcept override
    {
        return Size(_root);
    }

    const Key& Min() const override
    {
        const Node<Key, Value>* x = Min(_root);
        if (x == nullptr)
            throw std::out_of_range("no node");
        return x->_key;
    }

    const Key& Max() const override
    {
        const Node<Key, Value>* x = Max(_root);
        if (x == nullptr)
            throw std::out_of_range("no node");
        return x->_key;
    }

    const Key& Floor(const Key& key) const override
    {
        const Node<Key, Value>* x = Floor(_root, key);
        if (x == nullptr)
            throw std::out_of_range("no key smaller");
        return x->_key;
    }

    const Key& Ceiling(const Key& key) const override
    {
        const Node<Key, Value>* x = Ceiling(_root, key);
        if (x == nullptr)
            throw std::out_of_range("no key larger");
        return x->_key;
    }

    size_t Rank(const Key& key) const noexcept override
    {
        return Rank(_root, key);
    }

    const Key& Select(size_t k) const override
    {
        const Node<Key, Value>* x = Select(_root, k);
        if (x == nullptr)
            throw std::out_of_range("select size is too large");
        return x->_key;
    }

    void DeleteMin() noexcept override
    {
        _root = DeleteMin(_root);
    }

    void DeleteMax() noexcept override
    {
        _root = DeleteMax(_root);
    }

    size_t Size(const Key& lo, const Key& hi) const noexcept override
    {
        if (hi < lo)
            return 0;
        
        return Contains(hi) ? Rank(hi) - Rank(lo) + 1 : Rank(hi) - Rank(lo);
    }

private:
    size_t Size(Node<Key, Value>* x) const noexcept
    {
        return x ? x->_n : 0;
    }

    Node<Key, Value>* Min(Node<Key, Value>* x) const noexcept
    {
        if (x == nullptr)
            return nullptr;
        
        if (x->_left == nullptr)
            return x;
        
        return Min(x->_left);
    }

    Node<Key, Value>* Max(Node<Key, Value>* x) const noexcept
    {
        if (x == nullptr)
            return nullptr;
        
        if (x->_right == nullptr)
            return x;
        
        return Max(x->_right);
    }

    Node<Key, Value>* Put(Node<Key, Value>* x, Key&& key, Value&& val)
    {
        if (x == nullptr)
            return new Node(std::forward<Key>(key), std::forward<Value>(val));
        if (key == x->_key)
            x->_val = val;
        else if (key < x->_key)
            x->_left = Put(x->_left, std::forward<Key>(key), std::forward<Value>(val));
        else
            x->_right = Put(x->_right, std::forward<Key>(key), std::forward<Value>(val));
        x->_n = Size(x->_left) + Size(x->_right) + 1;
        return x;
    }

    Node<Key, Value>* Get(Node<Key, Value>* x, const Key& key) const noexcept
    {
        if (x == nullptr)
            return nullptr;
        
        if (key == x->_key)
            return x;

        if (key < x->_key)
            return Get(x->_left, key);

        return Get(x->_right, key);
    }

    Node<Key, Value>* DeleteMin(Node<Key, Value>* x) noexcept
    {
        if (x == nullptr)
            return nullptr;

        if (x->_left == nullptr) {
            Node<Key, Value>* t = x->_right;
            delete x;
            return t;
        }
        x->_left = DeleteMin(x->_left);
        x->_n = Size(x->_left) + Size(x->_right) + 1;
        return x;
    }

    Node<Key, Value>* DeleteMax(Node<Key, Value>* x) noexcept
    {
        if (x == nullptr)
            return nullptr;

        if (x->_right == nullptr) {
            Node<Key, Value>* t = x->_left;
            delete x;
            return t;
        }
        x->_right = DeleteMax(x->_right);
        x->_n = Size(x->_left) + Size(x->_right) + 1;
        return x;
    }

    Node<Key, Value>* Delete(Node<Key, Value>* x, const Key& key) noexcept
    {
        if (x == nullptr)
            return nullptr;
        
        Node<Key, Value>* t;
        if (key == x->_key) {
            if (x->_right == nullptr) {
                t = x->_left;
                delete x;
                return t;
            }
            if (x->_left == nullptr) {
                t = x->_right;
                delete x;
                return t;
            }
            t = x;
            x = Min(t->_right);
            x->_right = DeleteMin(t->_right);
            x->_left = t->_left;
        }
        else if (key < x->_key) {
            x->_left = Delete(x->_left, key);
        }
        else {
            x->_right = Delete(x->_right, key);
        }
        x->_n = Size(x->_left) + Size(x->_right) + 1;
        return x;
    }

    const Node<Key, Value>* Floor(const Node<Key, Value>* x, const Key& key) const noexcept
    {
        if (x == nullptr)
            return nullptr;
        
        if (key == x->_key)
            return x;

        if (key < x->_key)
            return Floor(x->_left, key);

        const Node<Key, Value>* t = Floor(x->_right, key);
        return t ? t : x;
    }

    const Node<Key, Value>* Ceiling(const Node<Key, Value>* x, const Key& key) const noexcept
    {
        if (x == nullptr)
            return nullptr;
        
        if (key == x->_key)
            return x;

        if (key < x->_key) {
            const Node<Key, Value>* t = Ceiling(x->_right, key);
            return t ? t : x;
        }
        return Ceiling(x->_left, key);
    }

    const Node<Key, Value>* Select(const Node<Key, Value>* x, size_t k) const noexcept
    {
        if (x == nullptr)
            return nullptr;
        
        auto s = Size(x->_left);
        if (s == k)
            return x;
        if (s < k)
            return Select(x->_right, k-s-1);
        return Select(x->_left, k);
    }

    size_t Rank(const Node<Key, Value>* x, const Key& key) const noexcept
    {
        if (x == nullptr)
            return 0;
        
        if (key == x->_key)
            return Size(x->_left);
        
        if (key < x->_key)
            return Rank(x->_left, key);
        
        return Rank(x->_right, key) + Size(x->_left) + 1;
    }

    Node<Key, Value>* _root = nullptr;
};

#endif // !BINARY_SEARCH_TREE_ST_H