---
title: std::begin(std::initializer_list)
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/initializer_list/begin2
---


# beginpetty|(std::initializer_list)

ddcla|header=initializer_list|since=c++11|constexpr=c++14|
template< class E >
const E* begin( std::initializer_list<E> il ) noexcept;
The overload of `std::begin` for `initializer_list` returns a pointer to the first element of `il`.

## Parameters


### Parameters

- `il` - an `initializer_list`

## Return value

`il.begin()`

## Example


### Example

```cpp
#include <algorithm>
#include <initializer_list>
#include <iostream>
#include <iterator>

int main()
{
    std::initializer_list ϕ = {'1', '.', '6', '1', '8', '0'};

    std::copy(std::begin(ϕ),
              std::end(ϕ),
              std::ostream_iterator<char>(std::cout, ""));

    std::cout << '\n';
}
```


**Output:**
```
1.6180
```


## See also


| cpp/utility/initializer_list/dsc begin | (see dedicated page) |

