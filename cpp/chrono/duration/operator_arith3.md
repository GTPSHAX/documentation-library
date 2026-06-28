---
title: std::chrono::duration::operators (%=)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/duration/operator_arith3
---


```cpp
dcla|num=1|since=c++11|constexpr=c++17|1=
duration& operator+=( const duration& d );
dcla|num=2|since=c++11|constexpr=c++17|1=
duration& operator-=( const duration& d );
dcla|num=3|since=c++11|constexpr=c++17|1=
duration& operator*=( const rep& rhs );
dcla|num=4|since=c++11|constexpr=c++17|1=
duration& operator/=( const rep& rhs );
dcla|num=5|since=c++11|constexpr=c++17|1=
duration& operator%=( const rep& rhs );
dcla|num=6|since=c++11|constexpr=c++17|1=
duration& operator%=( const duration& rhs );
```

Performs compound assignments between two durations with the same period or between a duration and a tick count value.
If `rep_` is the member variable holding the number of ticks in this duration object,
1. Equivalent to `rep_ +.
2. Equivalent to `rep_ -.
3. Equivalent to `rep_ *.
4. Equivalent to `rep_ /.
5. Equivalent to `rep_ %.
6. Equivalent to `rep_ %.

## Parameters


### Parameters

- `d` - duration on the right-hand side of the operator
- `rhs` - number of ticks on the right-hand side of the operator

## Return value

A reference to this duration after modification.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::chrono::minutes m(11);
    m *= 2;
    m += std::chrono::hours(10); // hours implicitly convert to minutes
    std::cout << m.count() << " minutes equals "
              << std::chrono::duration_cast<std::chrono::hours>(m).count()
              << " hours and ";
    m %= std::chrono::hours(1);
    std::cout << m.count() << " minutes\n";
}
```


**Output:**
```
622 minutes equals 10 hours and 22 minutes
```


## See also


| cpp/chrono/duration/dsc operator_arith2 | (see dedicated page) |
| cpp/chrono/duration/dsc operator_arith4 | (see dedicated page) |

