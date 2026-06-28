---
title: std::modulus<void>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/modulus_void
---

ddcl|header=functional|since=c++14|
template<>
class modulus<void>;
`std::modulus<void>` is a specialization of `std::modulus` with parameter and return type deduced.

## Nested types


| Item | Description |
|------|-------------|
| **Nested type** | Definition |


## Member functions

member|operator()|2=
ddcl|1=
template< class T, class U >
constexpr auto operator()( T&& lhs, U&& rhs ) const
-> decltype(std::forward<T>(lhs) % std::forward<U>(rhs));
Returns the remainder of the division of `lhs` by `rhs`.

## Parameters


### Parameters

- `lhs, rhs` - values to divide

## Return value

`std::forward<T>(lhs) % std::forward<U>(rhs)`.

## Example


### Example

```cpp
#include <functional>
#include <iostream>

struct M
{
    M(int x) { std::cout << "M(" << x << ");\n"; }
    M() {}
};

auto operator%(M, M) { std::cout << "operator%(M, M);\n"; return M{}; }
auto operator%(M, int) { std::cout << "operator%(M, int);\n"; return M{}; }
auto operator%(int, M) { std::cout << "operator%(int, M);\n"; return M{}; }

int main()
{
    M m;

    // 42 is converted into a temporary object M{42}
    std::modulus<M>{}(m, 42);    // calls operator%(M, M)

    // no temporary object
    std::modulus<void>{}(m, 42); // calls operator%(M, int)
    std::modulus<void>{}(42, m); // calls operator%(int, M)
}
```


**Output:**
```
M(42);
operator%(M, M);
operator%(M, int);
operator%(int, M);
```

