---
title: std::chrono::year::min
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year/min
---


```cpp
dcl|since=c++20|1=
static constexpr std::chrono::year min() noexcept;
```

Returns the smallest possible `year`, that is, `std::chrono::year(-32767)`.

## Return value

`std::chrono::year(-32767)`

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::cout << "The minimum year is: " << (int)std::chrono::year::min() << '\n';
}
```


**Output:**
```
The minimum year is: -32767
```

