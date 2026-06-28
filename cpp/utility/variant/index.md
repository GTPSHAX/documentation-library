---
title: std::variant::index
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variant/index
---

ddcl|since=c++17|
constexpr std::size_t index() const noexcept;
Returns the zero-based index of the alternative that is currently held by the variant.
If the variant is `valueless_by_exception`, returns `variant_npos`.

## Example


### Example

```cpp
#include <iostream>
#include <string>
#include <variant>

int main()
{
    std::variant<int, std::string> v = "abc";
    std::cout << "v.index = " << v.index() << '\n';
    v = {};
    std::cout << "v.index = " << v.index() << '\n';
}
```


**Output:**
```
v.index = 1
v.index = 0
```


## See also


| cpp/utility/variant/dsc holds_alternative | (see dedicated page) |
| cpp/utility/variant/dsc get | (see dedicated page) |

