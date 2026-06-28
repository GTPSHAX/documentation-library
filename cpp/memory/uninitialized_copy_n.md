---
title: std::uninitialized_copy_n
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/uninitialized_copy_n
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|since=c++11|constexpr=c++26|
template< class InputIt, class Size, class NoThrowForwardIt >
NoThrowForwardIt uninitialized_copy_n( InputIt first, Size count,
NoThrowForwardIt d_first );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class ForwardIt,
class Size, class NoThrowForwardIt >
NoThrowForwardIt uninitialized_copy_n( ExecutionPolicy&& policy,
ForwardIt first, Size count,
NoThrowForwardIt d_first );
```

1. Constructs elements in the destination range beginning at `d_first` from the first `count` elements in the source range beginning at `first` as if by
box|
`for (; count > 0; ++d_first, (void) ++first, --count)`<br />
`::new (``(*d_first))`<br />
`typename std::iterator_traits<NoThrowForwardIt>::value_type(*first);`<br />
`return d_first;`
@@ If an exception is thrown during the initialization, the objects already constructed are destroyed in an unspecified order.
2. Same as , but executed according to `policy`.
@@
rrev|since=c++20|
.

## Parameters


### Parameters

- `first` - the beginning of the range of the elements to copy
- `count` - the number of elements to copy
- `d_first` - the beginning of the target range
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
template<class InputIt, class Size, class NoThrowForwardIt>
constexpr NoThrowForwardIt uninitialized_copy_n(InputIt first, Size count,
NoThrowForwardIt d_first)
{
using T = typename std::iterator_traits<NoThrowForwardIt>::value_type;
NoThrowForwardIt current = d_first;
try
{
for (; count > 0; ++first, (void) ++current, --count)
::new (static_cast<void*>(std::addressof(*current))) T(*first);
}
catch (...)
{
for (; d_first != current; ++d_first)
d_first->~T();
throw;
}
return current;
}

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <memory>
#include <string>
#include <tuple>
#include <vector>

int main()
{
    std::vector<std::string> v = {"This", "is", "an", "example"};

    std::string* p;
    std::size_t sz;
    std::tie(p, sz) = std::get_temporary_buffer<std::string>(v.size());
    sz = std::min(sz, v.size());

    std::uninitialized_copy_n(v.begin(), sz, p);

    for (std::string* i = p; i != p + sz; ++i)
    {
        std::cout << *i << ' ';
        i->~basic_string<char>();
    }
    std::cout << '\n';

    std::return_temporary_buffer(p);
}
```


**Output:**
```
This is an example
```


## Defect reports


## See also


| cpp/memory/dsc uninitialized_copy | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_copy_n | (see dedicated page) |

