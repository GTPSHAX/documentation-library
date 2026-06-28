---
title: std::is_reference
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_reference
---

cpp/types/traits/is|1=is_reference
|description=
If `T` is a reference type (lvalue reference or rvalue reference), provides the member constant `value` equal `true`. For any other type, `value` is `false`.
|inherit_desc=`T` is a reference type

## Possible implementation

eq fun
|1=
template<class T> struct is_reference : std::false_type {};
template<class T> struct is_reference<T&> : std::true_type {};
template<class T> struct is_reference<T&&> : std::true_type {};

## Example


### Example

```cpp
#include <iostream>
#include <type_traits>

class A {};

int main()
{
#   define REF(x) << #x " ?: " << x << '\n'
    std::cout << std::boolalpha
    REF(std::is_reference_v<A>)
    REF(std::is_reference_v<A&>)
    REF(std::is_reference_v<A&&>)
    REF(std::is_reference_v<long>)
    REF(std::is_reference_v<long&>)
    REF(std::is_reference_v<long&&>)
    REF(std::is_reference_v<double*>)
    REF(std::is_reference_v<double*&>)
    REF(std::is_reference_v<double*&&>);
#   undef REF
}
```


**Output:**
```
std::is_reference_v<A> ?: false
std::is_reference_v<A&> ?: true
std::is_reference_v<A&&> ?: true
std::is_reference_v<long> ?: false
std::is_reference_v<long&> ?: true
std::is_reference_v<long&&> ?: true
std::is_reference_v<double*> ?: false
std::is_reference_v<double*&> ?: true
std::is_reference_v<double*&&> ?: true
```


## See also


| cpp/types/dsc is_lvalue_reference | (see dedicated page) |
| cpp/types/dsc is_rvalue_reference | (see dedicated page) |

