---
title: std::ranges::rend
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/rend
---


```cpp
**Header:** `<`ranges`>`
**Header:** `<`iterator`>`
|since=c++20|1=
inline namespace /* unspecified */ {
inline constexpr /* unspecified */ rend = /* unspecified */;
}
dcl|since=c++20|1=
template< class T >
requires /* see below */
constexpr std::sentinel_for<
decltype(ranges::rbegin(std::declval<T>()))> auto rend( T&& t );
```

Returns a sentinel indicating the end of a reversed range.
If `T` is an array type and `std::remove_all_extents_t<std::remove_reference_t<T>>` is incomplete, then the call to `ranges::rend` is ill-formed, no diagnostic required.
If the argument is an lvalue or `ranges::enable_borrowed_range<std::remove_cv_t<T>>` is `true`, then a call to `ranges::rend` is expression-equivalent to:
# <sup>(until C++23)</sup> <sup>(since C++23)</sup> `auto(t.rend())`, if that expression is valid and its type models `std::sentinel_for<decltype(ranges::rbegin(std::declval<T>()))>`.
# Otherwise, <sup>(until C++23)</sup> <sup>(since C++23)</sup> `auto(rend(t))`, if `T` is a class or enumeration type, that expression is valid and its type models `std::sentinel_for<decltype(ranges::rbegin(std::declval<T>()))>`, where the meaning of `rend` is established as if by performing argument-dependent lookup only.
# Otherwise, `std::make_reverse_iterator(ranges::begin(t))` if both `ranges::begin(t)` and `ranges::end(t)` are valid expressions, have the same type, and that type models `std::bidirectional_iterator`.
In all other cases, a call to `ranges::rend` is ill-formed, which can result in substitution failure when `ranges::rend(t)` appears in the immediate context of a template instantiation.

## Notes

If the argument is an rvalue (i.e. `T` is an object type) and `ranges::enable_borrowed_range<std::remove_cv_t<T>>` is `false`, or if it is of an array type of unknown bound, the call to `ranges::rend` is ill-formed, which also results in substitution failure.
If `ranges::rend(std::forward<T>(t))` is valid, then `decltype(ranges::rend(std::forward<T>(t)))` and `decltype(ranges::begin(std::forward<T>(t)))` model `std::sentinel_for` in all cases, while `T` models `std::ranges::range`.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <ranges>
#include <vector>

int main()
{
    std::vector<int> v = {3, 1, 4};
    namespace ranges = std::ranges;
    if (ranges::find(ranges::rbegin(v), ranges::rend(v), 5) != ranges::rend(v))
        std::cout << "found a 5 in vector v!\n";

    int a[] = {5, 10, 15};
    if (ranges::find(ranges::rbegin(a), ranges::rend(a), 5) != ranges::rend(a))
        std::cout << "found a 5 in array a!\n";
}
```


**Output:**
```
found a 5 in array a!
```


## Defect reports


## See also


| cpp/ranges/dsc crend | (see dedicated page) |
| cpp/ranges/dsc rbegin | (see dedicated page) |
| cpp/iterator/dsc rend | (see dedicated page) |

