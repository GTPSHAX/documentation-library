---
title: std::chrono::duration_cast
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/duration/duration_cast
---

ddcl|since=c++11|header=chrono|
template< class ToDuration, class Rep, class Period >
constexpr ToDuration duration_cast( const std::chrono::duration<Rep, Period>& d );
Converts a `std::chrono::duration` to a duration of different type `ToDuration`.
The function only participate in overload resolution if `ToDuration` is a specialization of `std::chrono::duration`.
Let
* `ToRep` be `typename ToDuration::rep`,
* `ToPeriod` be `typename ToDuration::period`,
* `CF` be `std::ratio_divide<Period, ToPeriod>`,
* `CR` be `std::common_type<Rep, ToRep, std::intmax_t>::type`,
* `cr_count` be `static_cast<CR>(d.count())`,
* `cr_num` be `static_cast<CR>(CF::num)`, and
* `cr_den` be `static_cast<CR>(CF::den)`,
the result is:


| rowspan=2 colspan=2 |  |
| colspan=2 | c | CF::num |
| - |
| c | 1 |
| not c | 1 |
| - |
| rowspan=2 | c | CF::den |
| c | 1 |
| c multi | ToDuration(static_cast<ToRep> | (d.count())) |
| c multi | ToDuration(static_cast<ToRep> | (cr_count * cr_num)) |
| - |
| not c | 1 |
| c multi | ToDuration(static_cast<ToRep> | (cr_count / cr_den)) |
| c multi | ToDuration(static_cast<ToRep> | (cr_count * cr_num / cr_den)) |


## Parameters


### Parameters

- `d` - duration to convert

## Return value

`d` converted to a duration of type `ToDuration`.

## Notes

No implicit conversions are used. Multiplications and divisions are avoided where possible, if it is known at compile time that one or more parameters are `1`. Computations are done in the widest type available and converted, as if by `cpp/language/static_cast`, to the result type only when finished.
Casting between integer durations where the source period is exactly divisible by the target period (e.g. hours to minutes) or between floating-point durations can be performed with ordinary casts or implicitly via ``std::chrono::duration` constructors`, no `duration_cast` is needed.
Casting from a floating-point duration to an integer duration is subject to undefined behavior when the floating-point value is NaN, infinity, or too large to be representable by the target's integer type. Otherwise, casting to an integer duration is subject to truncation as with any `static_cast` to an integer type.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>
#include <ratio>
#include <thread>

void f()
{
    std::this_thread::sleep_for(std::chrono::seconds(1));
}

int main()
{
    const auto t1 = std::chrono::high_resolution_clock::now();
    f();
    const auto t2 = std::chrono::high_resolution_clock::now();

    // floating-point duration: no duration_cast needed
    const std::chrono::duration<double, std::milli> fp_ms = t2 - t1;

    // integral duration: requires duration_cast
    const auto int_ms = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1);

    // converting integral duration to integral duration of
    // shorter divisible time unit: no duration_cast needed
    const std::chrono::duration<long, std::micro> int_usec = int_ms;

    std::cout << "f() took " << fp_ms << ", or "
              << int_ms << " (whole milliseconds), or "
              << int_usec << " (whole microseconds)\n";
}
```


**Output:**
```
f() took 1000.14ms, or 1000ms (whole milliseconds), or 1000000us (whole microseconds)
```


## See also


| cpp/chrono/dsc duration | (see dedicated page) |
| cpp/chrono/time_point/dsc time_point_cast | (see dedicated page) |
| cpp/chrono/duration/dsc floor | (see dedicated page) |
| cpp/chrono/duration/dsc ceil | (see dedicated page) |
| cpp/chrono/duration/dsc round | (see dedicated page) |

