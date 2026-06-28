---
title: std::plus<void>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/plus_void
---

ddcl|header=functional|since=c++14|
template<>
class plus<void>;
`std::plus<void>` is a specialization of `std::plus` with parameter and return type deduced.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/utility/functional/plus_void/dsc operator() | (see dedicated page) |

member|operator()|2=
ddcl|1=
template< class T, class U >
constexpr auto operator()( T&& lhs, U&& rhs ) const
-> decltype(std::forward<T>(lhs) + std::forward<U>(rhs));
Returns the sum of `lhs` and `rhs`.

## Parameters


### Parameters

- `lhs, rhs` - values to sum

## Return value

`std::forward<T>(lhs) + std::forward<U>(rhs)`.

## Example


### Example

```cpp
#include <functional>
#include <iostream>

int main()
{
    auto string_plus = std::plus<void>{}; // “void” can be omitted
    std::string a = "Hello ";
    const char* b = "world";
    std::cout << string_plus(a, b) << '\n';
}
```


**Output:**
```
Hello world
```

