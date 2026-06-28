---
title: std::chrono::duration::duration
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/duration/duration
---


```cpp
dcl|num=1|since=c++11|1=
constexpr duration() = default;
dcl|num=2|since=c++11|1=
duration( const duration& ) = default;
dcl|num=3|since=c++11|
template< class Rep2 >
constexpr explicit duration( const Rep2& r );
dcl|num=4|since=c++11|
template< class Rep2, class Period2 >
constexpr duration( const duration<Rep2, Period2>& d );
```

Constructs a new `duration` from one of several optional data sources.
1. The default constructor.
2. The copy constructor.
3. Constructs a duration with `r` ticks.
@@ :
* `is_convertible<const Rep2&, Rep>::value` is `true`.
* Any of the following conditions is satisfied:
:* `std::chrono::treat_as_floating_point<Rep>::value` is `true`.
:* `std::chrono::treat_as_floating_point<Rep2>::value` is `false`.
4. Constructs a duration by converting `d` to an appropriate period and tick count, as if by `std::chrono::duration_cast<duration>(d).count()`.
@@ :
* `std::chrono::treat_as_floating_point<Rep>::value` is `true`.
* All following conditions are satisfied:
:* `std::ratio_divide<Period2, Period>::den` is `1`.
:* `std::chrono::treat_as_floating_point<Rep2>::value` is `false`.

## Parameters


### Parameters

- `r` - a tick count
- `d` - a duration to copy from

## Example


### Example

```cpp
#include <chrono>

int main()
{
    std::chrono::hours h(1); // one hour
    std::chrono::milliseconds ms{3}; // 3 milliseconds
    std::chrono::duration<int, std::kilo> ks(3); // 3000 seconds

    // error: treat_as_floating_point<int>::value == false,
    // This duration allows whole tick counts only
//  std::chrono::duration<int, std::kilo> d3(3.5);

    // 30Hz clock using fractional ticks
    std::chrono::duration<double, std::ratio<1, 30>> hz30(3.5);

    // 3000 microseconds constructed from 3 milliseconds
    std::chrono::microseconds us = ms;
    // error: 1/1000000 is not divisible by 1/1000
//  std::chrono::milliseconds ms2 = us
    std::chrono::duration<double, std::milli> ms2 = us; // 3.0 milliseconds
}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3050 | C++11 | convertibility constraint used non-const xvalue | use const lvalues instead |


## See also


| cpp/chrono/duration/dsc operator{{= | (see dedicated page) |

