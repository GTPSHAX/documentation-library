---
title: std::shared_ptr::operator[]
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/shared_ptr/operator_at
---

ddcla|since=c++17|constexpr=c++26|
element_type& operator[]( std::ptrdiff_t idx ) const;
Returns a reference to the element at specified location `idx` of the array pointed to by the stored pointer.
When `T` is not an array type, it is unspecified whether `operator[]` is declared. If it is declared, it is unspecified what its return type is, except that the declaration is guaranteed to be well-formed.
.

## Parameters


### Parameters

- `idx` - the array index

## Return value

`get()[idx]`

## Exceptions

Throws nothing.

## Example


### Example

```cpp
#include <cstddef>
#include <iostream>
#include <memory>

int main()
{
    const std::size_t arr_size = 10;
    std::shared_ptr<int[]> pis(new int[10]{0, 1, 2, 3, 4, 5, 6, 7, 8, 9});
    for (std::size_t i = 0; i < arr_size; ++i)
        std::cout << pis[i] << ' ';
    std::cout << '\n';
}
```


**Output:**
```
0 1 2 3 4 5 6 7 8 9
```


## See also


| cpp/memory/shared_ptr/dsc get | (see dedicated page) |

