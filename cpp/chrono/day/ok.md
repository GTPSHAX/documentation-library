---
title: std::chrono::day::ok
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/day/ok
---


```cpp
dcl|since=c++20|
constexpr bool ok() const noexcept;
```

Checks if the day value stored in `*this` is in the valid range, i.e., .

## Return value

`true` if the day value stored in `*this` is in the range . Otherwise `false`.

## Example


### Example

```cpp
#include <chrono>
using namespace std::chrono_literals;

constexpr std::chrono::day d0{00};
constexpr std::chrono::day d1{13};
constexpr std::chrono::day d2{42};

static_assert
(
    d0 == 0d && !d0.ok() &&
    d1 == 13d && d1.ok() &&
    d2 == 42d && !d2.ok()
);

int main() {}
```


## See also


| cpp/chrono/day/dsc operator_unsigned | (see dedicated page) |

