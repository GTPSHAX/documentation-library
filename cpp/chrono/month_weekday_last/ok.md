---
title: std::chrono::month_weekday_last::ok
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month_weekday_last/ok
---


```cpp
dcl|since=c++20|1=
constexpr bool ok() const noexcept;
```

Checks if the contained `cpp/chrono/month` and `cpp/chrono/weekday_last` objects are valid.

## Return value

`month().ok() && weekday_last().ok()`

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::cout << std::boolalpha;

    auto mwdl{std::chrono::March/std::chrono::Wednesday[std::chrono::last]};
    std::cout << (mwdl.ok()) << ' ';
    mwdl = {std::chrono::month(3)/std::chrono::weekday(42)[std::chrono::last]}; 
    std::cout << (mwdl.ok()) << '\n';
}
```


**Output:**
```
true false
```

