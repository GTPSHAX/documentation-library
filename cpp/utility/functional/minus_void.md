---
title: std::minus<void>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/minus_void
---

ddcl|header=functional|since=c++14|
template<>
class minus<void>;
`std::minus<void>` is a specialization of `std::minus` with parameter and return type deduced.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions

member|operator()|2=
ddcl|1=
template< class T, class U >
constexpr auto operator()( T&& lhs, U&& rhs ) const
-> decltype(std::forward<T>(lhs) - std::forward<U>(rhs));
Returns the difference of `lhs` and `rhs`.

## Parameters


### Parameters

- `lhs, rhs` - values to subtract

## Return value

`std::forward<T>(lhs) - std::forward<U>(rhs)`.

## Example


### Example

```cpp
#include <complex>
#include <functional>
#include <iostream>

int main()
{
    auto complex_minus = std::minus<void>{}; // “void” can be omitted
    constexpr std::complex<int> z(4, 2);
    std::cout << complex_minus(z, 1) << '\n';
    std::cout << (z - 1) << '\n';
}
```


**Output:**
```
(3,2)
(3,2)
```

