---
title: std::compare_three_way_result
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/compare/compare_three_way_result
---


```cpp
**Header:** `<`compare`>`
dcl|since=c++20|1=
template< class T, class U = T >
struct compare_three_way_result;
```

Let `t` and `u` denote lvalue of `const std::remove_reference_t<T>` and `const std::remove_reference_t<U>` respectively, if the expression `1=t <=> u` is well-formed, provides the member typedef `type` equal to `1=decltype(t <=> u)`, otherwise there is no member `type`.

## Member types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Helper types

ddcl|since=c++20|1=
template< class T, class U = T >
using compare_three_way_result_t = compare_three_way_result<T, U>::type;

## Possible implementation

eq fun
|1=
// recommended by Casey Carter
// see also: https://github.com/microsoft/STL/pull/385#discussion_r357894054
template<class T, class U = T>
using compare_three_way_result_t = decltype(
std::declval<const std::remove_reference_t<T>&>() <=>
std::declval<const std::remove_reference_t<U>&>()
);
template<class T, class U = T>
struct compare_three_way_result {};
template<class T, class U>
requires requires { typename compare_three_way_result_t<T, U>; }
struct compare_three_way_result<T, U>
{
using type = compare_three_way_result_t<T, U>;
};

## Example


### Example

```cpp
#include <compare>
#include <iostream>
#include <type_traits>

template<class Ord>
void print_cmp_type()
{
    if constexpr (std::is_same_v<Ord, std::strong_ordering>)
        std::cout << "strong ordering\n";
    else if constexpr (std::is_same_v<Ord, std::weak_ordering>)
        std::cout << "weak ordering\n";
    else if constexpr (std::is_same_v<Ord, std::partial_ordering>)
        std::cout << "partial ordering\n";
    else
        std::cout << "illegal comparison result type\n";
}

int main()
{
    print_cmp_type<std::compare_three_way_result_t<int>>();
    print_cmp_type<std::compare_three_way_result_t<double>>();
}
```


**Output:**
```
strong ordering
partial ordering
```


## See also


| cpp/utility/compare/dsc partial_ordering | (see dedicated page) |
| cpp/utility/compare/dsc weak_ordering | (see dedicated page) |
| cpp/utility/compare/dsc strong_ordering | (see dedicated page) |

