---
title: std::uninitialized_copy
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/uninitialized_copy
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|constexpr=c++26|
template< class InputIt, class NoThrowForwardIt >
NoThrowForwardIt uninitialized_copy( InputIt first, InputIt last,
NoThrowForwardIt d_first );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class ForwardIt,
class NoThrowForwardIt >
NoThrowForwardIt uninitialized_copy( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last,
NoThrowForwardIt d_first );
```

1. Constructs elements in the destination range beginning at `d_first` from elements in the source range [first, last) as if by
box|
`1=for (; first != last; ++d_first, (void) ++first)`<br />
`::new (``(*d_first))`<br />
`typename std::iterator_traits<NoThrowForwardIt>::value_type(*first);`<br />
`return d_first;`
@@ If an exception is thrown during the initialization, the objects already constructed are destroyed in an unspecified order.
2. Same as , but executed according to `policy`.
@@
rrev|since=c++20|
If  overlaps with [first, last), the behavior is undefined.

## Parameters


### Parameters

- `d_first` - the beginning of the destination range
- `policy` - execution policy

**Type requirements:**

- `InputIt`
- `ForwardIt`
- `NoThrowForwardIt`

## Return value

As described above.

## Exceptions

2.

## Notes


## Possible implementation

eq fun|1=
template<class InputIt, class NoThrowForwardIt>
constexpr NoThrowForwardIt uninitialized_copy(InputIt first, InputIt last,
NoThrowForwardIt d_first)
{
using T = typename std::iterator_traits<NoThrowForwardIt>::value_type;
NoThrowForwardIt current = d_first;
try
{
for (; first != last; ++first, (void) ++current)
::new (static_cast<void*>(std::addressof(*current))) T(*first);
return current;
}
catch (...)
{
for (; d_first != current; ++d_first)
d_first->~T();
throw;
}
}

## Example


### Example

```cpp
#include <cstdlib>
#include <iostream>
#include <memory>
#include <string>

int main()
{
    const char* v[] = {"This", "is", "an", "example"};

    auto sz = std::size(v);

    if (void* pbuf = std::aligned_alloc(alignof(std::string), sizeof(std::string) * sz))
    {
        try
        {
            auto first = static_cast<std::string*>(pbuf);
            auto last = std::uninitialized_copy(std::begin(v), std::end(v), first);

            for (auto it = first; it != last; ++it)
                std::cout << *it << '_';
            std::cout << '\n';

            std::destroy(first, last);
        }
        catch (...) {}
        std::free(pbuf);
    }
}
```


**Output:**
```
This_is_an_example_
```


## Defect reports


## See also


| cpp/memory/dsc uninitialized_copy_n | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_copy | (see dedicated page) |

