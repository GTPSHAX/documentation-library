---
title: std::variant_npos
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variant/variant_npos
---

ddcl|since=c++17|header=variant|1=
inline constexpr std::size_t variant_npos = -1;
This is a special value equal to the largest value representable by the type `std::size_t`, used as the return value of  when  is `true`.

### Example

```cpp
#include <iostream>
#include <stdexcept>
#include <string>
#include <variant>

struct Demon
{
    Demon(int) {}
    Demon(const Demon&) { throw std::domain_error("copy ctor"); }
    Demon& operator= (const Demon&) = default;
};

int main()
{
    std::variant<int, Demon> var{42};
    std::cout
        << std::boolalpha
        << "index == npos: " << (var.index() == std::variant_npos) << '\n';

    try { var = Demon{666}; } catch (const std::domain_error& ex)
    {
        std::cout
            << "Exception: " << ex.what() << '\n'
            << "index == npos: " << (var.index() == std::variant_npos) << '\n'
            << "valueless: " << var.valueless_by_exception() << '\n';
    }
}
```


**Output:**
```
index == npos: false
Exception: copy ctor
index == npos: true
valueless: true
```


## See also


| cpp/utility/variant/dsc index | (see dedicated page) |
| cpp/utility/variant/dsc valueless_by_exception | (see dedicated page) |

