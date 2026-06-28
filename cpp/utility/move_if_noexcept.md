---
title: std::move_if_noexcept
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/move_if_noexcept
---


```cpp
**Header:** `<`utility`>`
dcla|since=c++11|constexpr=c++14|
template< class T >
/* see below */ move_if_noexcept( T& x ) noexcept;
```

`std::move_if_noexcept` obtains an rvalue reference to its argument if its move constructor does not throw exceptions or if there is no copy constructor (move-only type), otherwise obtains an lvalue reference to its argument. It is typically used to combine move semantics with strong exception guarantee.
The return type of `std::move_if_noexcept` is:
* `T&&` if `std::is_nothrow_move_constructible<T>::value  is `true`.
* Otherwise, `const T&`.

## Parameters


### Parameters

- `x` - the object to be moved or copied

## Return value

`std::move(x)` or `x`, depending on exception guarantees.

## Complexity

Constant.

## Notes

This is used, for example, by `std::vector::resize`, which may have to allocate new storage and then move or copy elements from old storage to new storage. If an exception occurs during this operation, `std::vector::resize` undoes everything it did to this point, which is only possible if `std::move_if_noexcept` was used to decide whether to use move construction or copy construction (unless copy constructor is not available, in which case move constructor is used either way and the strong exception guarantee may be waived).

## Example


### Example

```cpp
#include <iostream>
#include <utility>

struct Bad
{
    Bad() {}
    Bad(Bad&&) // may throw
    {
        std::cout << "Throwing move constructor called\n";
    }
    Bad(const Bad&) // may throw as well
    {
        std::cout << "Throwing copy constructor called\n";
    }
};

struct Good
{
    Good() {}
    Good(Good&&) noexcept // will NOT throw
    {
        std::cout << "Non-throwing move constructor called\n";
    }
    Good(const Good&) noexcept // will NOT throw
    {
        std::cout << "Non-throwing copy constructor called\n";
    }
};

int main()
{
    Good g;
    Bad b;
    [[maybe_unused]] Good g2 = std::move_if_noexcept(g);
    [[maybe_unused]] Bad b2 = std::move_if_noexcept(b);
}
```


**Output:**
```
Non-throwing move constructor called
Throwing copy constructor called
```


## See also


| cpp/utility/dsc forward | (see dedicated page) |
| cpp/utility/dsc move | (see dedicated page) |

