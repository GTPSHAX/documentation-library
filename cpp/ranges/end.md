---
title: std::ranges::end
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/end
---


```cpp
**Header:** `<`ranges`>`
**Header:** `<`iterator`>`
|since=c++20|1=
inline namespace /* unspecified */ {
inline constexpr /* unspecified */ end = /* unspecified */;
}
dcl|since=c++20|1=
template< class T >
requires /* see below */
constexpr std::sentinel_for<ranges::iterator_t<T>> auto end( T&& t );
```

Returns a sentinel indicating the end of a range.
If the argument is an lvalue or `ranges::enable_borrowed_range<std::remove_cv_t<T>>` is `true`, then a call to `ranges::end` is expression-equivalent to:
# `t + std::extent_v<T>` if `t` has an array type of known bound.
#* If `std::remove_all_extents_t<std::remove_reference_t<T>>` is incomplete, then the call to `ranges::end` is ill-formed, no diagnostic required.
# Otherwise, <sup>(until C++23)</sup> <sup>(since C++23)</sup> `auto(t.end())`, if that expression is valid, and its type models `std::sentinel_for<ranges::iterator_t<T>>`.
# Otherwise, <sup>(until C++23)</sup> <sup>(since C++23)</sup> `auto(end(t))`, if `T` is a class or enumeration type, that expression is valid and its converted type models `std::sentinel_for<ranges::iterator_t<T>>`, where the meaning of `end` is established as if by performing argument-dependent lookup only.
In all other cases, a call to `ranges::end` is ill-formed, which can result in substitution failure when the call to `ranges::end` appears in the immediate context of a template instantiation.

## Notes

If the argument is an rvalue (i.e. `T` is an object type) and `ranges::enable_borrowed_range<std::remove_cv_t<T>>` is `false`, or if it is of an array type of unknown bound, the call to `ranges::end` is ill-formed, which also results in substitution failure.
If `ranges::end(std::forward<T>(t))` is valid, then `decltype(ranges::end(std::forward<T>(t)))` and `decltype(ranges::begin(std::forward<T>(t)))` model `std::sentinel_for` in all cases, while `T` models `std::ranges::range`.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <ranges>
#include <vector>

int main()
{
    std::vector<int> vec{3, 1, 4};
    if (std::ranges::find(vec, 5) != std::ranges::end(vec))
        std::cout << "found a 5 in vector vec!\n";

    int arr[]{5, 10, 15};
    if (std::ranges::find(arr, 5) != std::ranges::end(arr))
        std::cout << "found a 5 in array arr!\n";
}
```


**Output:**
```
found a 5 in array arr!
```


## Defect reports


## See also


| cpp/ranges/dsc cend | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |
| cpp/iterator/dsc end | (see dedicated page) |

