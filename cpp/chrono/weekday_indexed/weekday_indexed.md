---
title: std::chrono::weekday_indexed::weekday_indexed
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/weekday_indexed/weekday_indexed
---


```cpp
dcl|num=1|since=c++20|1=
weekday_indexed() = default;
dcl|num=2|since=c++20|
constexpr weekday_indexed( const std::chrono::weekday& wd, unsigned index ) noexcept;
```

Constructs a `weekday_indexed`.
1. Default constructor leaves both the `std::chrono::weekday` and the index value uninitialized.
2. Constructs a `std::chrono::weekday_indexed|weekday_indexed` storing the weekday `wd` and the index `index`. The values held are unspecified if `1=!wd.ok() .

## Notes

A more convenient way to construct a `std::chrono::weekday_indexed|weekday_indexed` is with `std::chrono::weekday|weekday`'s `operator[]`, i.e., `wd[index]`.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>
using namespace std::chrono;

int main()
{
    constexpr auto third_friday = weekday_indexed(Friday, 3); // uses constructor (2)
    static_assert(third_friday == Friday[3]);

    weekday_indexed wdi = Tuesday[2]; // represents the 2nd Tuesday
    std::cout << year_month_day{ wdi / October / 2019y } << '\n';
}
```


**Output:**
```
2019-10-08
```


## See also


| cpp/chrono/weekday/dsc operator at | (see dedicated page) |

