---
title: std::enable_shared_from_this::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/enable_shared_from_this/operator=
---

ddcla|since=c++11|constexpr=c++26|1=
enable_shared_from_this&
operator=( const enable_shared_from_this &rhs ) noexcept;
Does nothing:  is not affected by the assignment.

## Parameters


### Parameters

- `rhs` - another `enable_shared_from_this` to assign to `*this`

## Return value

`*this`

## Notes

`1=operator=` is defined as `protected` in order to prevent accidental slicing but allow derived classes to have default assignment operators.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

class SharedInt : public std::enable_shared_from_this<SharedInt>
{
public:
    explicit SharedInt(int n) : mNumber(n) {}
    SharedInt(const SharedInt&) = default;
    SharedInt(SharedInt&&) = default;
    ~SharedInt() = default;

    // Both assignment operators use enable_shared_from_this::operator=
    SharedInt& operator=(const SharedInt&) = default;
    SharedInt& operator=(SharedInt&&) = default;

    int number() const { return mNumber; }

private:
    int mNumber;
};

int main()
{
    std::shared_ptr<SharedInt> a = std::make_shared<SharedInt>(2);
    std::shared_ptr<SharedInt> b = std::make_shared<SharedInt>(4);
    *a = *b;

    std::cout << a->number() << '\n';
}
```


**Output:**
```
4
```


## See also


| cpp/memory/dsc shared_ptr | (see dedicated page) |

