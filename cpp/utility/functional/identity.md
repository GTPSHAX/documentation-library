---
title: std::identity
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/identity
---

ddcl|header=functional|since=c++20|
struct identity;
`std::identity` is a function object type whose `operator()` returns its argument unchanged.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions

member|operator()|2=
ddcl|
template< class T >
constexpr T&& operator()( T&& t ) const noexcept;
Returns `std::forward<T>(t)`.

## Parameters


### Parameters

- `t` - argument to return

## Return value

`std::forward<T>(t)`.

## Notes

`std::identity` serves as the default projection in constrained algorithms. Its direct usage is usually not needed.

## Example


### Example


**Output:**
```
Print using std::identity as a projection: {<!---->{1, one}, {2, two}, {3, three}<!---->}
Project the Pair::n: {1, 2, 3}
Project the Pair::s: {one, two, three}
Print using custom closure as a projection: {1:one, 2:two, 3:three}
```


## See also


| cpp/types/dsc type_identity | (see dedicated page) |

