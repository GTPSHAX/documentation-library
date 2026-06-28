---
title: std::chrono::abs(std::chrono::duration)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/duration/abs
---

ddcl|since=c++17|header=chrono|
template< class Rep, class Period >
constexpr std::chrono::duration<Rep, Period> abs( std::chrono::duration<Rep, Period> d );
Returns the absolute value of the duration `d`. Specifically, if `1=d >= d.zero()`, return `d`, otherwise return `-d`.
The function does not participate in the overload resolution unless `std::numeric_limits<Rep>::is_signed` is `true`.

## Parameters


### Parameters

- `d` - duration

## Return value

Absolute value of `d`.

## Possible implementation

eq fun|1=
template<class Rep, class Period,
class = std::enable_if_t<std::numeric_limits<Rep>::is_signed>>
constexpr std::chrono::duration<Rep, Period> abs(std::chrono::duration<Rep, Period> d)
{
return d >= d.zero() ? +d : -d;
}

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    using namespace std::chrono;

    static_assert(abs(-42s) == std::chrono::abs(42s));

    std::cout << "abs(+3min) = " << abs(3min).count() << '\n'
              << "abs(-3min) = " << abs(-3min).count() << '\n';
}
```


**Output:**
```
abs(+3min) = 3
abs(-3min) = 3
```


## See also


| cpp/chrono/duration/dsc operator_arith | (see dedicated page) |
| cpp/numeric/math/dsc abs | (see dedicated page) |

