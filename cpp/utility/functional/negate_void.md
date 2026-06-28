---
title: std::negate<void>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/negate_void
---

ddcl|header=functional|since=c++14|
template<>
class negate<void>;
`std::negate<>` is a specialization of `std::negate` with parameter and return type deduced.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions

member|operator()|2=
ddcl|1=
template< class T >
constexpr auto operator()( T&& arg ) const
-> decltype(-std::forward<T>(arg));
Returns the result of negating `arg`.

## Parameters


### Parameters

- `arg` - value to negate

## Return value

`-std::forward<T>(arg)`.

## Example


### Example

```cpp
#include <complex>
#include <functional>
#include <iostream>

int main()
{
    auto complex_negate = std::negate<void>{}; // “void” can be omitted
    constexpr std::complex z(4, 2);
    std::cout << z << '\n';
    std::cout << -z << '\n';
    std::cout << complex_negate(z) << '\n';
}
```


**Output:**
```
(4,2)
(-4,-2)
(-4,-2)
```

