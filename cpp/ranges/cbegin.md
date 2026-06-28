---
title: std::ranges::cbegin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/cbegin
---


```cpp
**Header:** `<`ranges`>`
**Header:** `<`iterator`>`
|since=c++20|1=
inline namespace /* unspecified */ {
inline constexpr /* unspecified */ cbegin = /* unspecified */;
}
dcl|since=c++20|1=
template< class T >
requires /* see below */
constexpr /* see below */ auto cbegin( T&& t );
```

rrev multi|until1=c++23
|rev1=Returns an iterator to the first element of the const-qualified argument.
|rev2=Returns a constant iterator to the first element of the argument.
rrev multi|until1=c++23|rev1=
Let `CT` be
* `const std::remove_reference_t<T>&` if the argument is an lvalue (i.e. `T` is an lvalue reference type),
* `const T` otherwise.
A call to `ranges::cbegin` is expression-equivalent to `ranges::begin(static_cast<CT&&>(t))`.
|rev2=
If the argument is an lvalue or `ranges::enable_borrowed_range<std::remove_cv_t<T>>` is `true`, then a call to `ranges::cbegin` is expression-equivalent to:
* `std::const_iterator<decltype(U)>(U)` for some expression `U` equivalent to .
In all other cases, a call to `ranges::cbegin` is ill-formed, which can result in substitution failure when the call appears in the immediate context of a template instantiation.
The return type models `std::input_or_output_iterator` <sup>(since C++23)</sup>  and  in all cases.

## Notes

For an lvalue range `e` of type `T`, `ranges::cbegin(e)` is equivalent to
rrev multi|until1=c++23|rev1=
`ranges::begin(std::as_const(e))`.
|rev2=
* `ranges::begin(e)` if `T` models .
* Otherwise, `ranges::begin(std::as_const(e))` if `const T` models .
* Otherwise, `std::basic_const_iterator(ranges::begin(e))`.

## Example


### Example

```cpp
#include <cassert>
#include <ranges>
#include <vector>

int main()
{
    std::vector v{3, 1, 4};
    auto vi = std::ranges::cbegin(v);
    assert(3 == *vi);
    ++vi; // OK, constant-iterator object is mutable
    assert(1 == *vi);
    // *vi = 13; // Error: constant-iterator points to an immutable element

    int a[]{3, 1, 4};
    auto ai = std::ranges::cbegin(a); // cbegin works with C-arrays as well
    assert(3 == *ai and *(ai + 1) == 1);
    // *ai = 13; // Error: read-only variable is not assignable
}
```


## See also


| cpp/ranges/dsc begin | (see dedicated page) |
| cpp/iterator/dsc begin | (see dedicated page) |

