---
title: std::greater<void>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/greater_void
---

ddcl|header=functional|since=c++14|
template<>
class greater<void>;
`std::greater<void>` is a specialization of `std::greater` with parameter and return type deduced.

## Nested types


| Item | Description |
|------|-------------|
| **Nested type** | Definition |


## Member functions

member|operator()|2=
ddcl|1=
template< class T, class U >
constexpr auto operator()( T&& lhs, U&& rhs ) const
-> decltype(std::forward<T>(lhs) > std::forward<U>(rhs));
Returns the result of `std::forward<T>(lhs) > std::forward<U>(rhs)`.

## Parameters


### Parameters

- `lhs, rhs` - values to compare

## Return value

`std::forward<T>(lhs) > std::forward<U>(rhs)`.
If a built-in operator comparing pointers is called, the result is consistent with the implementation-defined strict total order over pointers.

## Example


### Example

```cpp
#include <algorithm>
#include <cstdint>
#include <functional>

constexpr bool strictly_positive(int lhs)
{
    return std::greater<>()(lhs, 0);
}

int main()
{
    constexpr std::int64_t low = 0B11;
    constexpr std::uint16_t high = 0X11;
    std::greater<> greater{};
    static_assert(greater(high, low));

    constexpr static auto arr = {0, 1, 2, 3, 4, 5};
    static_assert(!std::all_of(arr.begin(), arr.end(), strictly_positive));
    static_assert(std::all_of(arr.begin() + 1, arr.end(), strictly_positive));
}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2562 | C++98 | the pointer total order might be inconsistent | guaranteed to be consistent |

