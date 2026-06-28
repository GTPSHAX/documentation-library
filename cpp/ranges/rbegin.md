---
title: std::ranges::rbegin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/rbegin
---


```cpp
**Header:** `<`ranges`>`
**Header:** `<`iterator`>`
|since=c++20|1=
inline namespace /* unspecified */ {
inline constexpr /* unspecified */ rbegin = /* unspecified */;
}
dcl|since=c++20|1=
template< class T >
requires /* see below */
constexpr std::input_or_output_iterator auto rbegin( T&& t );
```

Returns an iterator to the last element of the argument.
If `T` is an array type and `std::remove_all_extents_t<std::remove_reference_t<T>>` is incomplete, then the call to `ranges::rbegin` is ill-formed, no diagnostic required.
If the argument is an lvalue or `ranges::enable_borrowed_range<std::remove_cv_t<T>>` is `true`, then a call to `ranges::rbegin` is expression-equivalent to:
# <sup>(until C++23)</sup> <sup>(since C++23)</sup> `auto(t.rbegin())`, if that expression is valid and its type models `std::input_or_output_iterator`.
# Otherwise, <sup>(until C++23)</sup> <sup>(since C++23)</sup> `auto(rbegin(t))`, if `T` is a class or enumeration type, that expression is valid and its type models `std::input_or_output_iterator`, where the meaning of `rbegin` is established as if by performing argument-dependent lookup only.
# Otherwise, `std::make_reverse_iterator(ranges::end(t))` if both `ranges::begin(t)` and `ranges::end(t)` are valid expressions, have the same type, and that type models `std::bidirectional_iterator`.
In all other cases, a call to `ranges::rbegin` is ill-formed, which can result in substitution failure when `ranges::rbegin(t)` appears in the immediate context of a template instantiation.

## Notes

If the argument is an rvalue (i.e. `T` is an object type) and `ranges::enable_borrowed_range<std::remove_cv_t<T>>` is `false`, the call to `ranges::rbegin` is ill-formed, which also results in substitution failure.
The return type models `std::input_or_output_iterator` in all cases.

## Example


### Example

```cpp
#include <iostream>
#include <ranges>
#include <span>
#include <vector>

int main()
{
    std::vector<int> v = {3, 1, 4};
    auto vi = std::ranges::rbegin(v);
    std::cout << *vi << '\n';
    *vi = 42; // OK

    int a[] = {-5, 10, 15};
    auto ai = std::ranges::rbegin(a);
    std::cout << *ai << '\n';
    *ai = 42; // OK

    // auto x_x = std::ranges::rbegin(std::vector{6, 6, 6});
    // ill-formed: the argument is an rvalue (see Notes ↑)

    auto si = std::ranges::rbegin(std::span{a}); // OK
    static_assert(std::ranges::enable_borrowed_range<
        std::remove_cv_t<decltype(std::span{a})>>);
    *si = 42; // OK
}
```


**Output:**
```
4
15
```


## Defect reports


## See also


| cpp/ranges/dsc crbegin | (see dedicated page) |
| cpp/iterator/dsc rbegin | (see dedicated page) |

