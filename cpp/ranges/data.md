---
title: std::ranges::data
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/data
---


```cpp
**Header:** `<`ranges`>`
**Header:** `<`iterator`>`
|since=c++20|1=
inline namespace /* unspecified */ {
inline constexpr /* unspecified */ data = /* unspecified */;
}
dcl|since=c++20|1=
template< class T >
requires /* see below */
constexpr std::remove_reference_t<
ranges::range_reference_t<T>>* data( T&& t );
```

Returns a pointer to the first element of a contiguous range.
If `T` is an array type and `std::remove_all_extents_t<std::remove_reference_t<T>>` is incomplete, then the call to `ranges::data` is ill-formed, no diagnostic required.
If the argument is an lvalue or `ranges::enable_borrowed_range<std::remove_cv_t<T>>` is `true`, a call to `ranges::data` is expression-equivalent to:
# <sup>(until C++23)</sup> <sup>(since C++23)</sup> `auto(t.data())`, if that expression is valid and its type is a pointer to an object type.
# Otherwise, `std::to_address(ranges::begin(t))`, if the expression `ranges::begin(t)` is valid and its type models `std::contiguous_iterator`.
In all other cases, a call to `ranges::data` is ill-formed, which can result in substitution failure when `ranges::data(e)` appears in the immediate context of a template instantiation.

## Notes

If the argument is an rvalue (i.e. `T` is an object type) and `ranges::enable_borrowed_range<std::remove_cv_t<T>>` is `false`, the call to `ranges::data` is ill-formed, which also results in substitution failure.
If `ranges::data(e)` is valid for an expression `e`, then it returns a pointer to an object.

## Example


### Example

```cpp
#include <cstring>
#include <iostream>
#include <ranges>
#include <string>

int main()
{
    std::string s{"Hello world!\n"};

    char a[20]; // storage for a C-style string
    std::strcpy(a, std::ranges::data(s));
    // [data(s), data(s) + size(s)] is guaranteed to be an NTBS

    std::cout << a;
}
```


**Output:**
```
Hello world!
```


## See also


| cpp/ranges/dsc cdata | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |
| cpp/iterator/dsc data | (see dedicated page) |

