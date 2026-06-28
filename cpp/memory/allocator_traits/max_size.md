---
title: std::allocator_traits::max_size
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/allocator_traits/max_size
---

ddcla|header=memory|since=c++11|constexpr=c++20|
static size_type max_size( const Alloc& a ) noexcept;
If possible, obtains the maximum theoretically possible allocation size from the allocator `a`, by calling `a.max_size()`.
If the above is not possible (e.g., `Alloc` does not have the member function `max_size()`), then returns `std::numeric_limits<size_type>::max() / sizeof(value_type)`.

## Parameters


### Parameters

- `a` - allocator to detect

## Return value

Theoretical maximum allocation size.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2466 | C++11 | theoretical maximum allocation size in bytes was returned as fallback | size in elements is returned |


## Example


### Example

```cpp
#include <iostream>
#include <memory>
#include <locale>

int main()
{
    std::allocator<short> b;
    std::allocator<int> d;

    const auto p = std::allocator_traits<decltype(b)>::max_size(b);
    const auto q = std::allocator_traits<decltype(d)>::max_size(d);

    std::cout.imbue(std::locale("en_US.UTF-8"));
    std::cout << std::uppercase
              << "p = " << std::dec << p << " = 0x" << std::hex << p << '\n'
              << "q = " << std::dec << q << " = 0x" << std::hex << q << '\n';
}
```


**Output:**
```
p = 9,223,372,036,854,775,807 = 0x7,FFF,FFF,FFF,FFF,FFF
q = 4,611,686,018,427,387,903 = 0x3,FFF,FFF,FFF,FFF,FFF
```


## See also


| cpp/memory/allocator/dsc max_size | (see dedicated page) |

