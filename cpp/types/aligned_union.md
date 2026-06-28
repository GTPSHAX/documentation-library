---
title: std::aligned_union
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/aligned_union
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|deprecated=c++23|1=
template< std::size_t Len, class... Types >
struct aligned_union;
```

Provides the nested type `type`, which is a trivial standard-layout type of a size and alignment suitable for use as uninitialized storage for an object of any of the types listed in `Types`. The size of the storage is at least `Len`. `std::aligned_union` also determines the strictest (largest) alignment requirement among all `Types` and makes it available as the constant `alignment_value`.
If `1=sizeof...(Types) == 0` or if any of the types in `Types` is not a complete object type, the behavior is undefined.
It is implementation-defined whether any extended alignment is supported.

## Member types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Helper types


```cpp
dcl|since=c++14|deprecated=c++23|1=
template< std::size_t Len, class... Types >
using aligned_union_t = typename aligned_union<Len,Types...>::type;
```


## Member constants


## Possible implementation

eq fun|1=
#include <algorithm>
template<std::size_t Len, class... Types>
struct aligned_union
{
static constexpr std::size_t alignment_value = std::max({alignof(Types)...});
struct type
{
alignas(alignment_value) char _s[std::max({Len, sizeof(Types)...})];
};
};

## Example


### Example

```cpp
#include <iostream>
#include <string>
#include <type_traits>

int main()
{
    std::cout << sizeof(std::aligned_union_t<0, char>) << ' ' // 1
              << sizeof(std::aligned_union_t<2, char>) << ' ' // 2
              << sizeof(std::aligned_union_t<2, char[3]>) << ' ' // 3 (!)
              << sizeof(std::aligned_union_t<3, char[4]>) << ' ' // 4
              << sizeof(std::aligned_union_t<1, char, int, double>) << ' '    // 8
              << sizeof(std::aligned_union_t<12, char, int, double>) << '\n'; // 16 (!)

    using var_t = std::aligned_union<16, int, std::string>;

    std::cout << "var_t::alignment_value = " << var_t::alignment_value << '\n'
              << "sizeof(var_t::type) = " << sizeof(var_t::type) << '\n';

    var_t::type aligned_storage;
    int* int_ptr = new(&aligned_storage) int(42); // placement new
    std::cout << "*int_ptr = " << *int_ptr << '\n';

    std::string* string_ptr = new(&aligned_storage) std::string("bar");
    std::cout << "*string_ptr = " << *string_ptr << '\n';
    *string_ptr = "baz";
    std::cout << "*string_ptr = " << *string_ptr << '\n';
    string_ptr->~basic_string();
}
```


**Output:**
```
1 2 3 4 8 16
var_t::alignment_value = 8
sizeof(var_t::type) = 32
*int_ptr = 42
*string_ptr = bar
*string_ptr = baz
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2979 | C++11 | complete type was not required | requires complete types |


## See also


| cpp/types/dsc alignment_of | (see dedicated page) |
| cpp/types/dsc aligned_storage | (see dedicated page) |

