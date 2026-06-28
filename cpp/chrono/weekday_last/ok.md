---
title: std::chrono::weekday_last::ok
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/weekday_last/ok
---


```cpp
dcl|since=c++20|1=
constexpr bool ok() const noexcept;
```

Checks if the weekday object stored in `*this` is valid.

## Return value

`weekday().ok()`

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::cout << std::boolalpha;

    auto wdl{std::chrono::Tuesday[std::chrono::last]};
    std::cout << (wdl.ok()) << ' ';

    wdl = {std::chrono::weekday(42)[std::chrono::last]};
    std::cout << (wdl.ok()) << '\n';
}
```


**Output:**
```
true false
```

