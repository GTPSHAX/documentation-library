---
title: std::any::reset
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/any/reset
---

ddcl|since=c++17|
void reset() noexcept;
If `*this` contains a value, destroys the contained value.
`*this` does not contain a value after this call.

## Parameters

(none)

## Return value

(none)

## Example


### Example

```cpp
#include <any>
#include <cassert>

int main()
{
    std::any a{42};
    assert(a.has_value());
    a.reset();
    assert(not a.has_value());
}
```


## See also


| cpp/utility/any/dsc has_value | (see dedicated page) |

