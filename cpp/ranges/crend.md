---
title: std::ranges::crend
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/crend
---


```cpp
**Header:** `<`ranges`>`
**Header:** `<`iterator`>`
|since=c++20|1=
inline namespace /* unspecified */ {
inline constexpr /* unspecified */ crend = /* unspecified */;
}
dcl|since=c++20|1=
template< class T >
requires /* see below */
constexpr /* see below */ auto crend( T&& t );
```

Returns a sentinel<sup>(since C++23)</sup>  for the constant iterator indicating the end of a <sup>(until C++23)</sup> const-qualified range that is treated as a reversed sequence.
rrev multi|until1=c++23|rev1=
Let `CT` be
* `const std::remove_reference_t<T>&` if the argument is an lvalue (i.e. `T` is an lvalue reference type),
* `const T` otherwise.
A call to `ranges::crend` is expression-equivalent to `ranges::rend(static_cast<CT&&>(t))`.
|rev2=
If the argument is an lvalue or `ranges::enable_borrowed_range<std::remove_cv_t<T>>` is `true`, then a call to `ranges::crend` is expression-equivalent to:
* `std::const_sentinel<decltype(U)>(U)` for some expression `U` equivalent to .
In all other cases, a call to `ranges::crend` is ill-formed, which can result in substitution failure when the call appears in the immediate context of a template instantiation.
If `ranges::crend(e)` is valid for an expression `e`, where `decltype((e))` is `T`, then <sup>(until C++23)</sup> `CT` models `std::ranges::range`, and `std::sentinel_for<S, I>` is `true` in all cases, where `S` is `decltype(ranges::crend(e))`, and `I` is `decltype(ranges::crbegin(e))`. <sup>(since C++23)</sup> Additionally, `S` models

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

int main()
{
    int a[]{4, 6, -3, 9, 10};
    std::cout << "Array backwards: ";
    namespace ranges = std::ranges;
    ranges::copy(ranges::rbegin(a), ranges::rend(a),
                 std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';

    std::cout << "Vector backwards: ";
    std::vector v{4, 6, -3, 9, 10};
    ranges::copy(ranges::rbegin(v), ranges::rend(v),
                 std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';
}
```


**Output:**
```
Array backwards: 10 9 -3 6 4
Vector backwards: 10 9 -3 6 4
```


## See also


| cpp/ranges/dsc rend | (see dedicated page) |
| cpp/iterator/dsc rend | (see dedicated page) |

