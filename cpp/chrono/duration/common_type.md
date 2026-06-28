---
title: std::common_type<std::chrono::duration>
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/duration/common_type
---


# common_typesmall|<std::chrono::duration>

ddcl|header=chrono|since=c++11|
template< class Rep1, class Period1, class Rep2, class Period2 >
struct common_type<std::chrono::duration<Rep1, Period1>,
std::chrono::duration<Rep2, Period2>>;
Exposes the type named `type`, which is the common type of two `std::chrono::duration`s, whose period is the greatest common divisor of `Period1` and `Period2`.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Note

The period of the resulting duration can be computed by forming a ratio of the greatest common divisor of `Period1::num` and `Period2::num` and the least common multiple of `Period1::den` and `Period2::den`.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>
#include <type_traits>

// std::chrono already finds the greatest common divisor,
// likely using std::common_type<>. We make the type
// deduction externally. 

template<typename T,typename S>
constexpr auto durationDiff(const T& t, const S& s)
    -> typename std::common_type<T,S>::type
{
    typedef typename std::common_type<T,S>::type Common;
    return Common(t) - Common(s);
}

int main() 
{
    using namespace std::literals;

    constexpr auto ms = 30ms;
    constexpr auto us = 1100us;
    constexpr auto diff = durationDiff(ms, us);

    std::cout << ms << " - " << us << " = " << diff << '\n';
}
```


**Output:**
```
30ms - 1100us = 28900us
```


## See also


| cpp/chrono/time_point/dsc common_type | (see dedicated page) |
| cpp/types/dsc common_type | (see dedicated page) |

