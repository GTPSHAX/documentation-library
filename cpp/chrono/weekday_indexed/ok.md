---
title: std::chrono::weekday_indexed::ok
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/weekday_indexed/ok
---

ddcl|since=c++20|
constexpr bool ok() const noexcept;
Checks if the weekday object and the index stored in `*this` are both valid.

## Return value

`true` if `weekday().ok()  and `index()` is in the range . Otherwise `false`.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::cout << std::boolalpha;

    std::chrono::weekday_indexed wdi{std::chrono::Tuesday[2]};
    std::cout << (wdi.ok()) << ' ';
    wdi = {std::chrono::weekday(42)[2]}; 
    std::cout << (wdi.ok()) << ' ';
    wdi = {std::chrono::Tuesday[-4]}; 
    std::cout << (wdi.ok()) << '\n';
}
```


**Output:**
```
true false false
```

