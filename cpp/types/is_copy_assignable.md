---
title: std::is_copy_assignable
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_copy_assignable
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|num=1|1=
template< class T >
struct is_copy_assignable;
dcl|since=c++11|num=2|1=
template< class T >
struct is_trivially_copy_assignable;
dcl|since=c++11|num=3|1=
template< class T >
struct is_nothrow_copy_assignable;
```

1. If `T` is not a referenceable type (i.e., possibly cv-qualified `void` or a function type with a ''cv-qualifier-seq'' or a ''ref-qualifier''), provides a member constant `value` equal to `false`. Otherwise, provides a member constant `value` equal to `std::is_assignable<T&, const T&>::value`.
2. Same as , but uses `std::is_trivially_assignable<T&, const T&>`.
3. Same as , but uses `std::is_nothrow_assignable<T&, const T&>`.

## Helper variable templates


```cpp
dcl|since=c++17|1=
template< class T >
inline constexpr bool is_copy_assignable_v = is_copy_assignable<T>::value;
dcl|since=c++17|1=
template< class T >
inline constexpr bool is_trivially_copy_assignable_v = is_trivially_copy_assignable<T>::value;
dcl|since=c++17|1=
template< class T >
inline constexpr bool is_nothrow_copy_assignable_v = is_nothrow_copy_assignable<T>::value;
```


## Possible implementation

eq fun
|1=
template<class T>
struct is_copy_assignable
: std::is_assignable<typename std::add_lvalue_reference<T>::type,
typename std::add_lvalue_reference<const T>::type> {};
template<class T>
struct is_trivially_copy_assignable
: std::is_trivially_assignable<typename std::add_lvalue_reference<T>::type,
typename std::add_lvalue_reference<const T>::type> {};
template<class T>
struct is_nothrow_copy_assignable
: std::is_nothrow_assignable<typename std::add_lvalue_reference<T>::type,
typename std::add_lvalue_reference<const T>::type> {};

## Notes

The trait `std::is_copy_assignable` is less strict than *CopyAssignable* because it does not check the type of the result of the assignment (which, for a *CopyAssignable* type, must be an lvalue of type `T`) and does not check the semantic requirement that the argument expression remains unchanged. It also does not check that `T` satisfies *MoveAssignable*, which is required of all *CopyAssignable* types.

## Example


### Example

```cpp
#include <iostream>
#include <type_traits>
#include <utility>

struct Foo { int n; };

int main()
{
    std::cout << std::boolalpha
              << "Foo is trivially copy-assignable? "
              << std::is_trivially_copy_assignable<Foo>::value << '\n'
              << "int[2] is copy-assignable? "
              << std::is_copy_assignable<int[2]>::value << '\n'
              << "int is nothrow copy-assignable? "
              << std::is_nothrow_copy_assignable<int>::value << '\n';
}
```


**Output:**
```
Foo is trivially copy-assignable? true
int[2] is copy-assignable? false
int is nothrow copy-assignable? true
```


## Defect reports


## See also


| cpp/types/dsc is_assignable | (see dedicated page) |
| cpp/types/dsc is_move_assignable | (see dedicated page) |

