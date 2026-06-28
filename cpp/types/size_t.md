---
title: std::size_t
type: Utilities
source: https://en.cppreference.com/w/cpp/types/size_t
---


```cpp
**Header:** `<`cstddef`>`
**Header:** `<`cstdio`>`
**Header:** `<`cstdlib`>`
**Header:** `<`cstring`>`
**Header:** `<`ctime`>`
**Header:** `<`cuchar|notes=
**Header:** `<`cwchar`>`
dcl|
typedef /* implementation-defined */ size_t;
```

`std::size_t` is the unsigned integer type of the result of the following operators:
* `cpp/language/sizeof`
rrev|since=c++11|
* `cpp/language/sizeof...`
* `cpp/language/alignof`
If a program attempts to form an oversized type (i.e., the number of bytes in its object representation exceeds the maximum value representable in `std::size_t`), the program is ill-formed.
rrev|since=c++11|
The bit width of `std::size_t` is not less than 16.

## Notes

`std::size_t` can store the maximum size of a theoretically possible object of any type (including array). On many platforms (an exception is systems with segmented addressing) `std::size_t` can safely store the value of any non-member pointer, in which case it is synonymous with `std::uintptr_t`.
`std::size_t` is commonly used for array indexing and loop counting. Programs that use other types, such as `unsigned int`, for array indexing may fail on, e.g. 64-bit systems when the index exceeds `UINT_MAX` or if it relies on 32-bit modular arithmetic.
When indexing C++ containers, such as `std::string`, `std::vector`, etc, the appropriate type is the nested type `size_type` provided by such containers. It is usually defined as a synonym for `std::size_t`.
It is unspecified whether the declaration of `std::size_t` is available in any other standard library header. An implementation may avoid introducing this name even when the standard requires `std::size_t` to be used.
rrev|since=c++23|
The integer literal suffix for `std::size_t` is any combination of `z` or `Z` with `u` or `U` (i.e. `zu`, `zU`, `Zu`, `ZU`, `uz`, `uZ`, `Uz`, or `UZ`).

## Example


### Example

```cpp
#include <array>
#include <cstddef>
#include <iostream>

int main()
{
    std::array<std::size_t, 10> a;

    // Example with C++23 std::size_t literal
    for (auto i = 0uz; i != a.size(); ++i)
        std::cout << (a[i] = i) << ' ';
    std::cout << '\n';

    // Example of decrementing loop
    for (std::size_t i = a.size(); i--;)
        std::cout << a[i] << ' ';
    std::cout << '\n';

    // Note the naive decrementing loop:
    //  for (std::size_t i = a.size() - 1; i >= 0; --i) ...
    // is an infinite loop, because unsigned numbers are always non-negative
}
```


**Output:**
```
0 1 2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2 1 0
```


## Defect reports


## References


## See also


| cpp/types/dsc ptrdiff_t | (see dedicated page) |
| cpp/types/dsc offsetof | (see dedicated page) |
| cpp/language/dsc integer literal | (see dedicated page) |

