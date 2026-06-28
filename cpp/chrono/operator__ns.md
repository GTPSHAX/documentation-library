---
title: std::literals::chrono_literals::operator""ns
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/operator""ns
---


```cpp
**Header:** `<`chrono`>`
dcl|num=1|since=c++14|
constexpr std::chrono::nanoseconds
operator""ns( unsigned long long nsec );
dcl|num=2|since=c++14|
constexpr std::chrono::duration</*unspecified*/, std::nano>
operator""ns( long double nsec );
```

Forms a `std::chrono::duration` literal representing nanoseconds.
1. Integer literal, returns exactly `std::chrono::nanoseconds(nsec)`.
2. Floating-point literal, returns a floating-point duration equivalent to `std::chrono::nanoseconds`.

## Parameters


### Parameters

- `nsec` - the number of nanoseconds

## Return value

The `std::chrono::duration` literal.

## Possible implementation

eq fun
|1=
constexpr std::chrono::nanoseconds operator""ns(unsigned long long ns)
{
return std::chrono::nanoseconds(ns);
}
constexpr std::chrono::duration<long double, std::nano> operator""ns(long double ns)
{
return std::chrono::duration<long double, std::nano>(ns);
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
    auto d1{250ns};
    std::chrono::nanoseconds d2{1us};
    std::cout << d1 << " = " << d1.count() << " nanoseconds\n"
              << d2 << " = " << d2.count() << " nanoseconds\n";
}
```


**Output:**
```
250ns = 250 nanoseconds
1000ns = 1000 nanoseconds
```


## See also


| cpp/chrono/duration/dsc constructor | (see dedicated page) |

