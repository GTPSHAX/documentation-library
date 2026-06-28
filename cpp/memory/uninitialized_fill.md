---
title: std::uninitialized_fill
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/uninitialized_fill
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|constexpr=c++26|
template< class NoThrowForwardIt, class T >
void uninitialized_fill( NoThrowForwardIt first,
NoThrowForwardIt last, const T& value );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class NoThrowForwardIt, class T >
void uninitialized_fill( ExecutionPolicy&& policy,
NoThrowForwardIt first,
NoThrowForwardIt last, const T& value );
```

1. Constructs elements in the destination range [first, last) with the given value `value` as if by
box|
`1=for (; first != last; ++first)`<br />
`::new (``(*first))`<br />
`typename std::iterator_traits<NoThrowForwardIt>::value_type(value);`
@@ If an exception is thrown during the initialization, the objects already constructed are destroyed in an unspecified order.
2. Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `value` - the value to construct the elements with
- `policy` - execution policy

**Type requirements:**

- `NoThrowForwardIt`

## Exceptions

2.

## Notes


## Possible implementation

eq fun|1=
template<class NoThrowForwardIt, class T>
constexpr void uninitialized_fill(NoThrowForwardIt first, NoThrowForwardIt last,
const T& value)
{
using V = typename std::iterator_traits<NoThrowForwardIt>::value_type;
NoThrowForwardIt current = first;
try
{
for (; current != last; ++current)
::new (static_cast<void*>(std::addressof(*current))) V(value);
}
catch (...)
{
for (; first != current; ++first)
first->~V();
throw;
}
}

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <memory>
#include <string>

int main()
{
    const std::size_t sz = 4;
    std::allocator<std::string> alloc;
    std::string* p = alloc.allocate(sz);

    std::uninitialized_fill(p, p + sz, "Example");

    for (std::string* i = p; i != p + sz; ++i)
    {
        std::cout << *i << '\n';
        i->~basic_string<char>();
    }

    alloc.deallocate(p, sz);
}
```


**Output:**
```
Example
Example
Example
Example
```


## Defect reports


## See also


| cpp/memory/dsc uninitialized_fill_n | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_fill | (see dedicated page) |

