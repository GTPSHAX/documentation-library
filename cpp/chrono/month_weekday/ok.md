---
title: std::chrono::month_weekday::ok
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month_weekday/ok
---


```cpp
dcl|since=c++20|1=
constexpr bool ok() const noexcept;
```

Checks if the contained `cpp/chrono/month` and `cpp/chrono/weekday_indexed` objects are valid.

## Return value

`month().ok() && weekday_indexed().ok()`

## Example


### Example

```cpp
#include <cassert>
#include <chrono>

int main()
{
    auto mwdi{std::chrono::March/std::chrono::Friday[1]};
    assert(mwdi.ok());

    mwdi = {std::chrono::month(17)/std::chrono::Friday[1]}; 
    assert(not mwdi.ok());

    mwdi = {std::chrono::March/std::chrono::Friday[-4]}; 
    assert(not mwdi.ok());
}
```

