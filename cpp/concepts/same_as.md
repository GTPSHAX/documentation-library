---
title: std::same_as
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/same_as
---

ddcl|header=concepts|since=c++20|1=
template< class T, class U >
concept same_as = /* see below */;
The concept `same_as<T, U>` is satisfied if and only if `T` and `U` denote the same type.
`std::same_as<T, U>` subsumes `std::same_as<U, T>` and vice versa.

## Possible implementation

eq fun|1=
namespace detail
{
template< class T, class U >
concept SameHelper = std::is_same_v<T, U>;
}
template< class T, class U >
concept same_as = detail::SameHelper<T, U> && detail::SameHelper<U, T>;

## Example


### Example

```cpp
#include <concepts>
#include <iostream>

template<typename T, typename ... U>
concept either = (std::same_as<T, U> {{!!
```

template<typename T>
concept is_printable = std::integral<T>  std::floating_point<T>
either<std::remove_cvref_t<std::remove_pointer_t<std::decay_t<T>>>, char, wchar_t>;
void println(is_printable auto const ... arguments)
{
(std::wcout << ... << arguments) << '\n';
}
int main()
{
println("Example: ", 3.14, " : ", 42, " : [", 'a', L'-', L"Z]");
}
|output=
Example: 3.14 : 42 : [a-Z]

## References


## See also


| cpp/types/dsc is_same | (see dedicated page) |

