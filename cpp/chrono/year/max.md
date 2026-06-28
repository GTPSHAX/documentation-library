---
title: std::chrono::year::max
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year/max
---


```cpp
dcl|since=c++20|1=
static constexpr year max() noexcept;
```

Returns the largest possible `year`, that is, `std::chrono::year(32767)`.

## Return value

`std::chrono::year(32767)`

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::cout << "The maximum year is: " << (int)std::chrono::year::max() << '\n';
}
```


**Output:**
```
The maximum year is: 32767
```

