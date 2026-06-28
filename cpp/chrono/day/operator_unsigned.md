---
title: std::chrono::day::operator unsigned
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/day/operator_unsigned
---


```cpp
dcl|since=c++20|
constexpr explicit operator unsigned() const noexcept;
```

Returns the day value stored in `*this`.

## Return value

The day value stored in `*this`.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    constexpr std::chrono::day d{15};
    constexpr unsigned day = static_cast<unsigned>(d);
    std::cout << "The day is: " << day << '\n';
}
```


**Output:**
```
The day is: 15
```

