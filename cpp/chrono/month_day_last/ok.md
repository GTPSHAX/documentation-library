---
title: std::chrono::month_day_last::ok
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month_day_last/ok
---


```cpp
dcl|since=c++20|1=
constexpr bool ok() const noexcept;
```

Checks if the `month` object stored in `*this` is valid.

## Return value

`month().ok()`

## Example


### Example

```cpp
#include <cassert>
#include <chrono>

int main()
{
    auto mdl{std::chrono::February/std::chrono::last};
    assert(mdl.ok());
    mdl = {std::chrono::month(42)/std::chrono::last};
    assert(!mdl.ok());
}
```

