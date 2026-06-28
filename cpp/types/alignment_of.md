---
title: std::alignment_of
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/alignment_of
---

ddcl|header=type_traits|since=c++11|
template< class T >
struct alignment_of;
Provides the member constant `value` equal to the alignment requirement of the type `T`, as if obtained by an `cpp/language/alignof` expression. If `T` is an array type, returns the alignment requirements of the element type. If `T` is a reference type, returns the alignment requirements of the type referred to.
If `alignof(T)` is not a valid expression, the behavior is undefined.

## Helper variable template

ddcl|since=c++17|1=
template< class T >
constexpr std::size_t alignment_of_v = alignment_of<T>::value;

## Possible implementation

eq fun
|1=
template<class T>
struct alignment_of : std::integral_constant<std::size_t, alignof(T)> {};

## Notes

This type trait predates the `cpp/language/alignof` keyword, which can be used to obtain the same value with less verbosity.

## Example


### Example

```cpp
#include <cstdint>
#include <iostream>
#include <type_traits>

struct A {};
struct B
{
    std::int8_t p;
    std::int16_t q;
};

int main()
{
    std::cout << std::alignment_of<A>::value << ' ';
    std::cout << std::alignment_of<B>::value << ' ';
    std::cout << std::alignment_of<int>() << ' '; // alt syntax
    std::cout << std::alignment_of_v<double> << '\n'; // c++17 alt syntax
}
```


**Output:**
```
1 2 4 8
```


## See also


| cpp/language/dsc alignof | (see dedicated page) |
| cpp/language/dsc alignas | (see dedicated page) |
| cpp/types/dsc aligned_storage | (see dedicated page) |
| cpp/types/dsc aligned_union | (see dedicated page) |
| cpp/types/dsc max_align_t | (see dedicated page) |

