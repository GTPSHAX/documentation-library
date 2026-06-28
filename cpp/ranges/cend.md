---
title: std::ranges::cend
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/cend
---


```cpp
**Header:** `<`ranges`>`
**Header:** `<`iterator`>`
|since=c++20|1=
inline namespace /* unspecified */ {
inline constexpr /* unspecified */ cend = /* unspecified */;
}
dcl|since=c++20|1=
template< class T >
requires /* see below */
constexpr /* see below */ auto cend( T&& t );
```

Returns a sentinel<sup>(since C++23)</sup>  for the constant iterator indicating the end of a <sup>(until C++23)</sup> const-qualified range.
rrev multi|until1=c++23
|rev1=
Let `CT` be
* `const std::remove_reference_t<T>&` if the argument is an lvalue (i.e. `T` is an lvalue reference type),
* `const T` otherwise.
A call to `ranges::cend` is expression-equivalent to `ranges::end(static_cast<CT&&>(t))`.
|rev2=
If the argument is an lvalue or `ranges::enable_borrowed_range<std::remove_cv_t<T>>` is `true`, then a call to `ranges::cend` is expression-equivalent to:
* `std::const_sentinel<decltype(U)>(U)` for some expression `U` equivalent to .
In all other cases, a call to `ranges::cend` is ill-formed, which can result in substitution failure when the call appears in the immediate context of a template instantiation.
If `ranges::cend(e)` is valid for an expression `e`, where `decltype((e))` is `T`, then <sup>(until C++23)</sup> `CT` models `std::ranges::range`, and `std::sentinel_for<S, I>` is `true` in all cases, where `S` is `decltype(ranges::cend(e))`, and `I` is `decltype(ranges::cbegin(e))`. <sup>(since C++23)</sup> Additionally, `S` models

## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <ranges>
#include <vector>

int main()
{
    std::vector vec{3, 1, 4};
    int arr[]{5, 10, 15};

    assert(std::ranges::find(vec, 5) == std::ranges::cend(vec));
    assert(std::ranges::find(arr, 5) != std::ranges::cend(arr));
}
```


## See also


| cpp/ranges/dsc end | (see dedicated page) |
| cpp/iterator/dsc end | (see dedicated page) |

