---
title: std::literals::chrono_literals::operator""us
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/operator""us
---


```cpp
**Header:** `<`chrono`>`
dcl|num=1|since=c++14|1=
constexpr std::chrono::microseconds
operator""us( unsigned long long us );
dcl|num=2|since=c++14|1=
constexpr std::chrono::duration</*unspecified*/, std::micro>
operator""us( long double us );
```

Forms a `std::chrono::duration` literal representing microseconds.
1. Integer literal, returns exactly `std::chrono::microseconds(us)`.
2. Floating-point literal, returns a floating-point duration equivalent to `std::chrono::microseconds`.

## Parameters


### Parameters

- `us` - the number of microseconds

## Return value

The `std::chrono::duration` literal.

## Possible implementation

eq fun
|1=
constexpr std::chrono::microseconds operator""us(unsigned long long us)
{
return std::chrono::microseconds(us);
}
constexpr std::chrono::duration<long double, std::micro> operator""us(long double us)
{
return std::chrono::duration<long double, std::micro>(us);
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
    auto d1 = 250us;
    std::chrono::microseconds d2 = 1ms;
    std::cout << d1 << " = " << d1.count() << " microseconds\n"
              << 1ms << " = " << d2.count() << " microseconds\n";
}
```


**Output:**
```
250us = 250 microseconds
1ms = 1000 microseconds
```


## See also


| cpp/chrono/duration/dsc constructor | (see dedicated page) |

