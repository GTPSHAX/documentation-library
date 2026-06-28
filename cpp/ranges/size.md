---
title: std::ranges::size
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/size
---


```cpp
**Header:** `<`ranges`>`
**Header:** `<`iterator`>`
|since=c++20|1=
inline namespace /* unspecified */ {
inline constexpr auto size = /* unspecified */;
}
dcl|since=c++20|1=
template< class T >
requires /* see below */
constexpr auto size( T&& t );
```

Calculates the number of elements in `t` in constant time.
Given the subexpression of which `t` denotes the (possibly materialized) result object as `E`, and the type of `E` as `T`:
* If `T` is an array of unknown bound, `ranges::size(E)` is ill-formed.
* Otherwise, if `T` is an array type, `ranges::size(E)` is expression-equivalent to <sup>(until C++23)</sup> <sup>(since C++23)</sup> `auto(std::extent_v<T>)`.
* Otherwise, if all following conditions are satisfied, `ranges::size(E)` is expression-equivalent to <sup>(until C++23)</sup> <sup>(since C++23)</sup> `auto(t.size())`:
** `ranges::disable_sized_range<std::remove_cv_t<T>>` is `false`.
** <sup>(until C++23)</sup> <sup>(since C++23)</sup> `auto(t.size())` is a valid expression of integer-like type.
* Otherwise, if all following conditions are satisfied, `ranges::size(E)` is expression-equivalent to <sup>(until C++23)</sup> <sup>(since C++23)</sup> `auto(size(t))`:
** `T` is a class or enumeration type.
** `ranges::disable_sized_range<std::remove_cv_t<T>>` is `false`.
** <sup>(until C++23)</sup> <sup>(since C++23)</sup> `auto(size(t))` is a valid expression of integer-like type, where the meaning of `size` is established as if by performing argument-dependent lookup only.
* Otherwise, if all following conditions are satisfied, `ranges::size(E)` is expression-equivalent to :
** `T` models .
** Given the type of `ranges::begin(t)` as `I` and the type of `ranges::end(t)` as `S`, both  and  are modeled.
**  is a valid expression.
* Otherwise, `ranges::size(E)` is ill-formed.
Diagnosable ill-formed cases above result in substitution failure when `ranges::size(E)` appears in the immediate context of a template instantiation.

## Notes

Whenever `ranges::size(e)` is valid for an expression `e`, the return type is integer-like.
The expression `ranges::distance(e)` can also be used to determine the size of a range `e`. Unlike `ranges::size(e)`, `ranges::distance(e)` works even if `e` is an unsized range, at the cost of having linear complexity in that case.

## Example


### Example

```cpp
#include <iostream>
#include <ranges>
#include <type_traits>
#include <vector>

int main()
{
    auto v = std::vector<int>{};
    std::cout << "ranges::size(v) == " << std::ranges::size(v) << '\n';

    auto il = {7};     // std::initializer_list
    std::cout << "ranges::size(il) == " << std::ranges::size(il) << '\n';

    int array[]{4, 5}; // array has a known bound
    std::cout << "ranges::size(array) == " << std::ranges::size(array) << '\n';

    static_assert(std::is_signed_v<decltype(std::ranges::size(v))> == false);
}
```


**Output:**
```
ranges::size(v) == 0
ranges::size(il) == 1
ranges::size(array) == 2
```


## Defect reports


## See also


| cpp/ranges/dsc ssize | (see dedicated page) |
| cpp/ranges/dsc sized_range | (see dedicated page) |
| cpp/iterator/ranges/dsc distance | (see dedicated page) |
| cpp/iterator/dsc size | (see dedicated page) |

