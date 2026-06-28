---
title: std::literals::chrono_literals::operator""y
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/operator""y
---

ddcl|header=chrono|since=c++20|
constexpr std::chrono::year operator""y( unsigned long long y ) noexcept;
Forms a `std::chrono::year` literal representing a year in the [proleptic Gregorian calendar](https://en.wikipedia.org/wiki/proleptic Gregorian calendar).

## Parameters


### Parameters

- `y` - the year value

## Return value

A `std::chrono::year` initialized from `int(y)`. If `y` is not in the range , the stored value is unspecified.

## Possible implementation

eq fun
|1=
constexpr std::chrono::year operator""y(unsigned long long y) noexcept
{
return std::chrono::year(static_cast<int>(y));
}

## Notes


## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    using namespace std::literals;

    std::cout << int(2020y)  << '\t' << 2020y  << '\n'
              << int(-220y)  << '\t' << -220y  << '\n'
              << int(3000y)  << '\t' << 3000y  << '\n'
              << int(32768y) << '\t' << 32768y << '\n'  // unspecified
              << int(65578y) << '\t' << 65578y << '\n'; // unspecified
}
```


**Output:**
```
2020	2020
-220	-0220
3000	3000
-32768	-32768 is not a valid year
42	0042
```


## See also


| cpp/chrono/year/dsc constructor | (see dedicated page) |

