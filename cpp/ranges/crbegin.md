---
title: std::ranges::crbegin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/crbegin
---


```cpp
**Header:** `<`ranges`>`
**Header:** `<`iterator`>`
|since=c++20|1=
inline namespace /* unspecified */ {
inline constexpr /* unspecified */ crbegin = /* unspecified */;
}
dcl|since=c++20|1=
template< class T >
requires /* see below */
constexpr /* see below */ auto crbegin( T&& t );
```

rrev multi|until1=c++23|rev1=
Returns an iterator to the first element of the const-qualified argument that is treated as a reversed sequence.
|rev2=
Returns a constant iterator to the first element of the argument that is treated as a reversed sequence.
rrev multi|until1=c++23|rev1=
Let `CT` be
* `const std::remove_reference_t<T>&` if the argument is an lvalue (i.e. `T` is an lvalue reference type),
* `const T` otherwise.
A call to `ranges::crbegin` is expression-equivalent to `ranges::rbegin(static_cast<CT&&>(t))`.
|rev2=
If the argument is an lvalue or `ranges::enable_borrowed_range<std::remove_cv_t<T>>` is `true`, then a call to `ranges::crbegin` is expression-equivalent to:
* `std::const_iterator<decltype(U)>(U)` for some expression `U` equivalent to .
In all other cases, a call to `ranges::crbegin` is ill-formed, which can result in substitution failure when the call appears in the immediate context of a template instantiation.
The return type models `std::input_or_output_iterator` <sup>(since C++23)</sup>  and  in all cases.

## Example


### Example

```cpp
#include <cassert>
#include <iterator>
#include <span>
#include <vector>

int main()
{
    std::vector<int> v{3, 1, 4};
    auto vi = std::ranges::crbegin(v);
    assert(*vi == 4);
    ++vi; // OK, iterator object is mutable
    assert(*vi == 1);
    // *vi = 13; // Error: underlying element is read-only

    int a[]{-5, 10, 15};
    auto ai = std::ranges::crbegin(a);
    assert(*ai == 15);

    // auto x_x = std::ranges::crbegin(std::vector<int>{6, 6, 6});
    // ill-formed: the argument is an rvalue (see Notes ↑)

    auto si = std::ranges::crbegin(std::span{a}); // OK
    assert(*si == 15);
    static_assert
    (
        std::ranges::enable_borrowed_range<std::remove_cv_t<decltype(std::span{a})>>
    );
}
```


## See also


| cpp/ranges/dsc rbegin | (see dedicated page) |
| cpp/iterator/dsc rbegin | (see dedicated page) |

