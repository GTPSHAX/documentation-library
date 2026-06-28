---
title: std::literals::chrono_literals::operator""ms
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/operator""ms
---


```cpp
**Header:** `<`chrono`>`
dcl|num=1|since=c++14|
constexpr std::chrono::milliseconds
operator""ms( unsigned long long ms );
dcl|num=2|since=c++14|
constexpr std::chrono::duration</*unspecified*/, std::milli>
operator""ms( long double ms );
```

Forms a `std::chrono::duration` literal representing milliseconds.
1. Integer literal, returns exactly `std::chrono::milliseconds(ms)`.
2. Floating-point literal, returns a floating-point duration equivalent to `std::chrono::milliseconds`.

## Parameters


### Parameters

- `ms` - the number of milliseconds

## Return value

The `std::chrono::duration` literal.

## Possible implementation

eq fun
|1=
constexpr std::chrono::milliseconds operator""ms(unsigned long long ms)
{
return std::chrono::milliseconds(ms);
}
constexpr std::chrono::duration<long double, std::milli> operator""ms(long double ms)
{
return std::chrono::duration<long double, std::milli>(ms);
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
    constexpr auto d1{250ms};
    constexpr std::chrono::milliseconds d2{1s};
    std::cout << d1 << " = " << d1.count() << " milliseconds\n"
              << d2 << " = " << d2.count() << " milliseconds\n";
}
```


**Output:**
```
250ms = 250 milliseconds
1000ms = 1000 milliseconds
```


## See also


| cpp/chrono/duration/dsc constructor | (see dedicated page) |

