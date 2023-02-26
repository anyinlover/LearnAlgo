#ifndef ST_H
#define ST_H

#include <cstddef>
//class Iterator;
template<typename Key, typename Value>
class ST {
public:
    ST() = default;
    virtual ~ST() = default;
    virtual void Put(Key&& key, Value&& val) = 0;
    virtual Value& Get(const Key& key) const = 0;
    virtual void Delete(const Key& key) noexcept = 0;
    virtual bool Contains(const Key& key) const noexcept = 0;
    inline bool IsEmpty() const noexcept {return Size() == 0;}
    virtual size_t Size() const noexcept = 0;
    virtual const Key& Min() const = 0;
    virtual const Key& Max() const = 0;
    virtual const Key& Floor(const Key& key) const = 0;
    virtual const Key& Ceiling(const Key& key) const = 0;
    virtual size_t Rank(const Key& key) const noexcept = 0;
    virtual const Key& Select(size_t k) const = 0;
    virtual void DeleteMin() noexcept = 0;
    virtual void DeleteMax() noexcept = 0;
    virtual size_t Size(const Key& lo, const Key& hi) const noexcept = 0;
    // Iterable<Key> is not done
    // virtual Iterator Begin();
    // virtual Iterator End();
    // virtual Iterator KeyIter(const Key&);
};

#endif // !ST_H