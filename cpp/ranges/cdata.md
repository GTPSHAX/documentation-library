---
title: std::ranges::cdata
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/cdata
---


```cpp
**Header:** `<`ranges`>`
**Header:** `<`iterator`>`
|since=c++20|1=
inline namespace /*unspecified*/ {
inline constexpr /*unspecified*/ cdata = /*unspecified*/;
}
dcl|since=c++20|1=
template< class T >
requires /* see below */
constexpr /* see below */ cdata( T&& t );
```

Returns a pointer to the first element <sup>(since C++23)</sup> of constant type of a contiguous range denoted by a <sup>(until C++23)</sup> const-qualified argument.
rrev|until=c++23|
Let `CT` be
* `const std::remove_reference_t<T>&` if the argument is an lvalue (i.e. `T` is an lvalue reference type),
* `const T` otherwise.
A call to `ranges::cdata` is expression-equivalent to `ranges::data(static_cast<CT&&>(t))`.
The return type is equivalent to `std::remove_reference_t<ranges::range_reference_t<CT>>*`.
rrev|since=c++23|
If the argument is an lvalue or `ranges::enable_borrowed_range<std::remove_cv_t<T>>` is `true`, then a call to `ranges::cdata` is expression-equivalent to:
* .
The return type is equivalent to `std::remove_reference_t<ranges::range_const_reference_t<T>>*`.
In all other cases, a call to `ranges::cdata` is ill-formed, which can result in substitution failure when the call appears in the immediate context of a template instantiation.
If `ranges::cdata(t)` is valid, then it returns a pointer to an object <sup>(since C++23)</sup> of constant type.

## Example


### Example

```cpp
#include <cstring>
#include <iostream>
#include <ranges>
#include <string>

int main()
{
    std::string src {"hello world!\n"};

//  std::ranges::cdata(src)[0] = 'H'; // error, src.data() is treated as read-only
    std::ranges::data(src)[0] = 'H'; // OK, src.data() is a non-const storage

    char dst[20]; // storage for a C-style string
    std::strcpy(dst, std::ranges::cdata(src));
    // [data(src), data(src) + size(src)] is guaranteed to be an NTBS

    std::cout << dst;
}
```


**Output:**
```
Hello world!
```


## See also


| cpp/ranges/dsc data | (see dedicated page) |
| cpp/iterator/dsc data | (see dedicated page) |

