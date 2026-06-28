---
title: std::enable_shared_from_this
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/enable_shared_from_this
---

ddcl|header=memory|since=c++11|
template< class T >
class enable_shared_from_this;
`std::enable_shared_from_this` allows an object `t` that is currently managed by a `std::shared_ptr` named `pt` to safely generate additional `std::shared_ptr` instances `pt1`, `pt2` etc. that all share ownership of `t` with `pt`.
Publicly inheriting from `std::enable_shared_from_this<T>` provides the type `T` with a member function `shared_from_this`.  If an object `t` of type `T` is managed by a `std::shared_ptr<T>` named `pt`, then calling `T::shared_from_this` will return a new `std::shared_ptr<T>` that shares ownership of `t` with `pt`.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


## Notes

The constructors of `std::shared_ptr` detect the presence of an unambiguous and accessible (i.e. public) `enable_shared_from_this` base and assign the newly created `std::shared_ptr` to  if not already owned by a live `std::shared_ptr`. Constructing a `std::shared_ptr` for an object that is already managed by another `std::shared_ptr` will not update or share ownership with  and so will lead to undefined behavior.
Calling `shared_from_this` on an object that is not managed by a `std::shared_ptr<T>` will throw `std::bad_weak_ptr` (because the  member is in the "expired" state, and constructing a `std::shared_ptr` from an expired `std::weak_ptr` throws).
`enable_shared_from_this` provides the safe alternative to an expression like `std::shared_ptr<T>(this)`, which is likely to result in `this` being destroyed more than once by multiple owners that are unaware of each other (see example below).

## Example


### Example

```cpp
#include <iostream>
#include <memory>

class Good : public std::enable_shared_from_this<Good>
{
public:
    std::shared_ptr<Good> getptr()
    {
        return shared_from_this();
    }
};

class Best : public std::enable_shared_from_this<Best>
{
    struct Private{ explicit Private() = default; };

public:
    // Constructor is only usable by this class
    Best(Private) {}

    // Everyone else has to use this factory function
    // Hence all Best objects will be contained in shared_ptr
    static std::shared_ptr<Best> create()
    {
        return std::make_shared<Best>(Private());
    }

    std::shared_ptr<Best> getptr()
    {
        return shared_from_this();
    }
};

struct Bad
{
    std::shared_ptr<Bad> getptr()
    {
        return std::shared_ptr<Bad>(this);
    }
    ~Bad() { std::cout << "Bad::~Bad() called\n"; }
};

void testGood()
{
    // Good: the two shared_ptr's share the same object
    std::shared_ptr<Good> good0 = std::make_shared<Good>();
    std::shared_ptr<Good> good1 = good0->getptr();
    std::cout << "good1.use_count() = " << good1.use_count() << '\n';
}

void misuseGood()
{
    // Bad: shared_from_this is called without having std::shared_ptr owning the caller
    try
    {
        Good not_so_good;
        std::shared_ptr<Good> gp1 = not_so_good.getptr();
    }
    catch (std::bad_weak_ptr& e)
    {
        // undefined behavior (until C++17) and std::bad_weak_ptr thrown (since C++17)
        std::cout << e.what() << '\n';
    }
}

void testBest()
{
    // Best: Same but cannot stack-allocate it:
    std::shared_ptr<Best> best0 = Best::create();
    std::shared_ptr<Best> best1 = best0->getptr();
    std::cout << "best1.use_count() = " << best1.use_count() << '\n';

    // Best stackBest; // <- Will not compile: Best::Best() is missing.
    // Best stackBest(Best::Private{}); // <- Will not compile: Best::Private is private
}

void testBad()
{
    // Bad, each shared_ptr thinks it is the only owner of the object
    std::shared_ptr<Bad> bad0 = std::make_shared<Bad>();
    std::shared_ptr<Bad> bad1 = bad0->getptr();
    std::cout << "bad1.use_count() = " << bad1.use_count() << '\n';
} // UB: double-delete of Bad

int main()
{
    testGood();
    misuseGood();

    testBest();

    testBad();
}
```


**Output:**
```
good1.use_count() = 2
bad_weak_ptr
best1.use_count() = 2
bad1.use_count() = 1
Bad::~Bad() called
Bad::~Bad() called
*** glibc detected *** ./test: double free or corruption
```


## Defect reports


## See also


| cpp/memory/dsc shared_ptr | (see dedicated page) |
| cpp/memory/shared_ptr/dsc make_shared | (see dedicated page) |

