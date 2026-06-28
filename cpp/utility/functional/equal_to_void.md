---
title: std::equal_to<void>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/equal_to_void
---

ddcl|header=functional|since=c++14|
template<>
class equal_to<void>;
`std::equal_to<void>` is a specialization of `std::equal_to` with parameter and return type deduced.

## Nested types


| Item | Description |
|------|-------------|
| **Nested type** | Definition |


## Member functions

member|operator()|2=
ddcl|1=
template< class T, class U >
constexpr auto operator()( T&& lhs, U&& rhs ) const
-> decltype(std::forward<T>(lhs) == std::forward<U>(rhs));
Returns the result of equality comparison between `lhs` and `rhs`.

## Parameters


### Parameters

- `lhs, rhs` - values to compare

## Return value

`1=std::forward<T>(lhs) == std::forward<U>(rhs)`.

## Example


### Example

```cpp
#include <functional>

int main()
{
    constexpr int a = 0, b = 8;
    std::equal_to<> equal{};
    static_assert(equal(a, a));
    static_assert(!equal(a, b));
}
```

