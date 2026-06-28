---
title: std::chrono::duration::operators (unary)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/duration/operator_arith
---


```cpp
dcl rev multi|num=1|until1=c++17|dcl1=
constexpr duration operator+() const;
|dcl2=
constexpr std::common_type_t<duration> operator+() const;
dcl rev multi|num=2|until1=c++17|dcl1=
constexpr duration operator-() const;
|dcl2=
constexpr std::common_type_t<duration> operator-() const;
```

Implements unary plus and unary minus for the durations.
If `rep_` is a member variable holding the number of ticks in a duration object, and `D` is the return type,
1. Equivalent to `return D(*this);`.
2. Equivalent to `return D(-rep_);`.

## Parameters

(none)

## Return value

1. A copy of this duration object.
2. A copy of this duration object, with the number of ticks negated.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    constexpr std::chrono::seconds s1(-052);
    constexpr std::chrono::seconds s2 = -s1;

    std::cout << "Negated " << s1 << " are " << s2 << '\n';
}
```


**Output:**
```
Negated -42s are 42s
```


## See also


| cpp/chrono/duration/dsc operator_arith2 | (see dedicated page) |
| cpp/chrono/duration/dsc operator_arith4 | (see dedicated page) |

