---
title: std::literals::chrono_literals::operator""h
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/operator""h
---


```cpp
**Header:** `<`chrono`>`
dcl|num=1|since=c++14|
constexpr std::chrono::hours
operator""h( unsigned long long hrs );
dcl|num=2|since=c++14|
constexpr std::chrono::duration</*unspecified*/, std::ratio<3600,1>>
operator""h( long double hrs );
```

Forms a `std::chrono::duration` literal representing hours.
1. Integer literal, returns exactly `std::chrono::hours(hrs)`.
2. Floating-point literal, returns a floating-point duration equivalent to `std::chrono::hours`.

## Parameters


### Parameters

- `hrs` - the number of hours

## Return value

The `std::chrono::duration` literal.

## Possible implementation

eq fun
|1=
constexpr std::chrono::hours operator""h(unsigned long long h)
{
return std::chrono::hours(h);
}
constexpr std::chrono::duration<long double, ratio<3600,1>> operator""h(long double h)
{
return std::chrono::duration<long double, std::ratio<3600,1>>(h);
}

## Notes


## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    using namespace std::chrono_literals;
    auto day = 24h;
    auto halfhour = 0.5h;
    std::cout << "one day is " << day.count() << " hours (" << day << ")\n"
              << "half an hour is " << halfhour.count() << " hours ("
              << halfhour << ")\n";
}
```


**Output:**
```
one day is 24 hours (24h)
half an hour is 0.5 hours (0.5h)
```


## See also


| cpp/chrono/duration/dsc constructor | (see dedicated page) |

