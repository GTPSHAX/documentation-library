---
title: std::less_equal<void>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/less_equal_void
---

ddcl|header=functional|since=c++14|
template<>
class less_equal<void>;
`std::less_equal<void>` is a specialization of `std::less_equal` with parameter and return type deduced.

## Nested types


| Item | Description |
|------|-------------|
| **Nested type** | Definition |


## Member functions

member|operator()|2=
ddcl|1=
template< class T, class U >
constexpr auto operator()( T&& lhs, U&& rhs ) const
-> decltype(std::forward<T>(lhs) <= std::forward<U>(rhs));
Returns the result of `1=std::forward<T>(lhs) <= std::forward<U>(rhs)`.

## Parameters


### Parameters

- `lhs, rhs` - values to compare

## Return value

`1=std::forward<T>(lhs) <= std::forward<U>(rhs)`.
If a built-in operator comparing pointers is called, the result is consistent with the implementation-defined strict total order over pointers.

## Example


### Example

```cpp
#include <algorithm>
#include <functional>
#include <initializer_list>

constexpr bool strictly_not_positive(int lhs)
{
    return std::less_equal<>()(lhs, 0);
}

int main()
{
    constexpr int low = 0, high = 8;
    std::less_equal<> less_equal{};
    static_assert(less_equal(low, high));
    static_assert(less_equal(low, low));

    static constexpr auto arr = {1, 0, -1, -2, -3, -4};
    static_assert(!std::all_of(arr.begin(), arr.end(), strictly_not_positive));
    static_assert(std::all_of(arr.begin() + 1, arr.end(), strictly_not_positive));
}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2562 | C++98 | the pointer total order might be inconsistent | guaranteed to be consistent |

