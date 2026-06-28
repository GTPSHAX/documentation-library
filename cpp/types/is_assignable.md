---
title: std::is_assignable
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_assignable
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|num=1|1=
template< class T, class U >
struct is_assignable;
dcl|since=c++11|num=2|1=
template< class T, class U >
struct is_trivially_assignable;
dcl|since=c++11|num=3|1=
template< class T, class U >
struct is_nothrow_assignable;
```

1. If the expression `1=std::declval<T>() = std::declval<U>()` is well-formed in unevaluated context, provides the member constant `value` equal to `true`. Otherwise, `value` is `false`. Access checks are performed as if from a context unrelated to either type.
2. Same as , but the evaluation of the assignment expression will not call any operation that is not trivial. For the purposes of this check, a call to `std::declval` is considered trivial and not considered an odr-use of `std::declval`.
3. Same as , but the evaluation of the assignment expression will not call any operation that is not noexcept.

## Helper variable templates


```cpp
dcl|since=c++17|1=
template< class T, class U >
constexpr bool is_assignable_v = is_assignable<T, U>::value;
dcl|since=c++17|1=
template< class T, class U >
constexpr bool is_trivially_assignable_v = is_trivially_assignable<T, U>::value;
dcl|since=c++17|1=
template< class T, class U >
constexpr bool is_nothrow_assignable_v = is_nothrow_assignable<T, U>::value;
```


## Notes

This trait does not check anything outside the immediate context of the assignment expression: if the use of `T` or `U` would trigger template specializations, generation of implicitly-defined special member functions etc, and those have errors, the actual assignment may not compile even if `std::is_assignable<T,U>::value` compiles and evaluates to `true`.

## Example


### Example

```cpp
#include <iostream>
#include <string>
#include <type_traits>

struct Ex1 { int n; };

int main()
{
    std::cout << std::boolalpha
              << "int is assignable from int? "
              << std::is_assignable<int, int>::value << '\n' // 1 = 1; wouldn't compile
              << "int& is assignable from int? "
              << std::is_assignable<int&, int>::value << '\n' // int a; a = 1; works
              << "int is assignable from double? "
              << std::is_assignable<int, double>::value << '\n'
              << "int& is nothrow assignable from double? "
              << std::is_nothrow_assignable<int&, double>::value << '\n'
              << "string is assignable from double? "
              << std::is_assignable<std::string, double>::value << '\n'
              << "Ex1& is trivially assignable from const Ex1&? "
              << std::is_trivially_assignable<Ex1&, const Ex1&>::value << '\n';
}
```


**Output:**
```
int is assignable from int? false
int& is assignable from int? true
int is assignable from double? false
int& is nothrow assignable from double? true
string is assignable from double? true
Ex1& is trivially assignable from const Ex1&? true
```


## See also


| cpp/types/dsc is_copy_assignable | (see dedicated page) |
| cpp/types/dsc is_move_assignable | (see dedicated page) |
| cpp/concepts/dsc assignable_from | (see dedicated page) |

