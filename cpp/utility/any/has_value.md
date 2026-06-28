---
title: std::any::has_value
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/any/has_value
---


```cpp
dcl|since=c++17|
bool has_value() const noexcept;
```

Checks whether the object contains a value.

## Parameters

(none)

## Return value

`true` if and only if the instance contains a value.

## Example


### Example

```cpp
#include <any>
#include <cassert>
#include <string>

int main()
{
    std::any a0;
    assert(a0.has_value() == false);

    std::any a1 = 42;
    assert(a1.has_value() == true);
    assert(std::any_cast<int>(a1) == 42);
    a1.reset();
    assert(a1.has_value() == false);

    auto a2 = std::make_any<std::string>("Andromeda");
    assert(a2.has_value() == true);
    assert(std::any_cast<std::string&>(a2) == "Andromeda");
    a2.reset();
    assert(a2.has_value() == false);
}
```


## See also


| cpp/utility/any/dsc reset | (see dedicated page) |

