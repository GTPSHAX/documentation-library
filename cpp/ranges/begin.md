---
title: std::ranges::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/begin
---


```cpp
**Header:** `<`ranges`>`
**Header:** `<`iterator`>`
|since=c++20|1=
inline namespace /* unspecified */ {
inline constexpr /* unspecified */ begin = /* unspecified */;
}
dcl|since=c++20|1=
template< class T >
requires /* see below */
constexpr std::input_or_output_iterator auto begin( T&& t );
```

Returns an iterator to the first element of the argument.
If the argument is an lvalue or `ranges::enable_borrowed_range<std::remove_cv_t<T>>` is `true`, then a call to `ranges::begin` is expression-equivalent to:
# `t + 0` if `t` has an array type.
#* If `std::remove_all_extents_t<std::remove_reference_t<T>>` is incomplete, then the call to `ranges::begin` is ill-formed, no diagnostic required.
# Otherwise, <sup>(until C++23)</sup> <sup>(since C++23)</sup> `auto(t.begin())`, if that expression is valid and its type models `std::input_or_output_iterator`.
# Otherwise, <sup>(until C++23)</sup> <sup>(since C++23)</sup> `auto(begin(t))`, if `T` is a class or enumeration type, that expression is valid and its type models `std::input_or_output_iterator`, where the meaning of `begin` is established as if by performing argument-dependent lookup only.
In all other cases, a call to `ranges::begin` is ill-formed, which can result in substitution failure when the call appears in the immediate context of a template instantiation.

## Notes

If the argument is an rvalue (i.e. `T` is an object type) and `ranges::enable_borrowed_range<std::remove_cv_t<T>>` is `false`, the call to `ranges::begin` is ill-formed, which also results in substitution failure.
The return type models `std::input_or_output_iterator` in all cases.

## Example


### Example

```cpp
#include <cassert>
#include <ranges>
#include <vector>

int main() 
{
    std::vector v{3, 1, 4};
    auto vi = std::ranges::begin(v);
    auto vci = std::ranges::cbegin(v);
    assert(*vi == 3 and *vi == *vci);
    ++vi;
    ++vci; // OK: vci is modifiable object
    *vi = 42; // OK: vi points to mutable element
    // *vci = 13; // Error: vci points to immutable element

    int a[]{-5, 10, 15};
    auto ai = std::ranges::begin(a); // works with C-arrays as well
    assert(*ai == -5);
    *ai = 42; // OK
}
```


## Defect reports


## See also


| cpp/ranges/dsc cbegin | (see dedicated page) |
| cpp/iterator/dsc begin | (see dedicated page) |

