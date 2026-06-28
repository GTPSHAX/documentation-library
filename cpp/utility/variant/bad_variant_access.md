---
title: std::bad_variant_access
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variant/bad_variant_access
---

ddcl|since=c++17|header=variant|
class bad_variant_access : public std::exception
`std::bad_variant_access` is the type of the exception thrown in the following situations:
* `cpp/utility/variant/get|std::get called with an index or type that does not match the currently active alternative.
* `std::visit` called to visit a variant that is `valueless_by_exception`.
rrev|since=c++26|
* `std::variant::visit` called to visit a variant that is `valueless_by_exception`.

## Member functions


## Example


### Example

```cpp
#include <iostream>
#include <variant>

int main()
{
    std::variant<int, float> v;
    v = 12;
    try
    {
        std::get<float>(v);
    }
    catch (const std::bad_variant_access& e)
    {
        std::cout << e.what() << '\n';
    }
}
```


**Output:**
```
bad_variant_access
```


## See also


| cpp/utility/variant/dsc get | (see dedicated page) |
| cpp/utility/variant/dsc visit2 | (see dedicated page) |
| cpp/utility/variant/dsc visit | (see dedicated page) |

