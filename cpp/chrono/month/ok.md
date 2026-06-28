---
title: std::chrono::month::ok
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month/ok
---

ddcl|since=c++20|
constexpr bool ok() const noexcept;
Checks if the month value stored in `*this` is in the valid range, i.e., .

## Return value

`true` if the month value stored in `*this` is in the range . Otherwise `false`.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    for (const unsigned mm : {6u, 0u, 16U})
    {
        std::cout << mm << ": ";
        const std::chrono::month m{mm};
        m.ok() ? std::cout << "month is valid\n"
               : std::cout << "month is invalid\n";
    }
}
```


**Output:**
```
6: month is valid
0: month is invalid
16: month is invalid
```

