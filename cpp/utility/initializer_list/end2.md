---
title: std::end(std::initializer_list)
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/initializer_list/end2
---


# endpetty|(std::initializer_list)

ddcla|header=initializer_list|since=c++11|constexpr=c++14|
template< class E >
const E* end( std::initializer_list<E> il ) noexcept;
The overload of `std::end` for `initializer_list` returns a pointer to one past the last element of `il`.

## Parameters


### Parameters

- `il` - an `initializer_list`

## Return value

`il.end()`

## Example


### Example

```cpp
#include <cassert>
#include <initializer_list>
#include <iterator>
#include <numeric>

int main()
{
    std::initializer_list e = {2, 7, 1, 8, 2, 8, 1};
    assert(std::accumulate(std::begin(e), std::end(e), 13) == 42);
}
```


## See also


| cpp/utility/initializer_list/dsc end | (see dedicated page) |

