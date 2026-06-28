---
title: std::not_equal_to<void>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/not_equal_to_void
---

ddcl|header=functional|since=c++14|
template<>
class not_equal_to<void>;
`std::not_equal_to<void>` is a specialization of `std::not_equal_to` with parameter and return type deduced.

## Nested types


| Item | Description |
|------|-------------|
| **Nested type** | Definition |


## Member functions

member|operator()|2=
ddcl|1=
template< class T, class U >
constexpr auto operator()( T&& lhs, U&& rhs ) const
-> decltype(std::forward<T>(lhs) != std::forward<U>(rhs));
Returns the result of non-equality comparison between `lhs` and `rhs`.

## Parameters


### Parameters

- `lhs, rhs` - values to compare

## Return value

`1=std::forward<T>(lhs) != std::forward<U>(rhs)`.

## Example


### Example

```cpp
#include <functional>

int main()
{
    constexpr int p = 0, q = 8;
    std::not_equal_to<> not_equal{};
    static_assert(!not_equal(p, p));
    static_assert(not_equal(p, q));
}
```

