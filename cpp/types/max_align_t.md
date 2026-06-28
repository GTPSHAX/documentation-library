---
title: std::max_align_t
type: Utilities
source: https://en.cppreference.com/w/cpp/types/max_align_t
---

ddcl|header=cstddef|since=c++11|
typedef /* implementation-defined */ max_align_t;
`std::max_align_t` is a standard-layout <sup>(until C++26)</sup> *TrivialType*<sup>(since C++26)</sup> *TriviallyCopyable type* whose alignment requirement is at least as strict (as large) as that of every scalar type.
`std::is_trivially_default_constructible_v<std::max_align_t>` is `true`.

## Notes

Pointers returned by allocation functions such as `std::malloc` are suitably aligned for any object, which means they are aligned at least as strictly as `std::max_align_t`.

## Example


### Example

```cpp
#include <cstddef>
#include <iostream>

int main()
{
    std::cout << alignof(std::max_align_t) << '\n';
}
```


**Output:**
```
16
```


## References


## See also


| cpp/language/dsc alignof | (see dedicated page) |
| cpp/types/dsc alignment_of | (see dedicated page) |
| cpp/types/dsc is_scalar | (see dedicated page) |

