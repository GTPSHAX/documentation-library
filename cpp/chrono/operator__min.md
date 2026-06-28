---
title: std::literals::chrono_literals::operator""min
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/operator""min
---


```cpp
**Header:** `<`chrono`>`
dcl|num=1|since=c++14|
constexpr chrono::minutes
operator""min( unsigned long long mins );
dcl|num=2|since=c++14|
constexpr chrono::duration</*unspecified*/, ratio<60,1>>
operator""min( long double mins );
```

Forms a `std::chrono::duration` literal representing minutes.
1. Integer literal, returns exactly `std::chrono::minutes(mins)`.
2. Floating-point literal, returns a floating-point duration equivalent to `std::chrono::minutes`.

## Parameters


### Parameters

- `mins` - the number of minutes

## Return value

The `std::chrono::duration` literal.

## Possible implementation

eq fun
|1=
constexpr std::chrono::minutes operator""min(unsigned long long m)
{
return std::chrono::minutes(m);
}
constexpr std::chrono::duration<long double,
std::ratio<60,1>> operator""min(long double m)
{
return std::chrono::duration<long double, ratio<60,1>> (m);
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
    auto lesson = 45min;
    auto halfmin = 0.5min;
    std::cout << "One lesson is " << lesson.count() << " minutes"
                 " (" << lesson << ")\n"
              << "Half a minute is " << halfmin.count() << " minutes"
                 " (" << halfmin << ")\n";
}
```


**Output:**
```
One lesson is 45 minutes (45min)
Half a minute is 0.5 minutes (0.5min)
```


## See also


| cpp/chrono/duration/dsc constructor | (see dedicated page) |

