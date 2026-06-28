---
title: std::is_move_assignable
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_move_assignable
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|num=1|
template< class T >
struct is_move_assignable;
dcl|since=c++11|num=2|
template< class T >
struct is_trivially_move_assignable;
dcl|since=c++11|num=3|
template< class T >
struct is_nothrow_move_assignable;
```

1. If `T` is not a referenceable type (i.e., possibly cv-qualified `void` or a function type with a ''cv-qualifier-seq'' or a ''ref-qualifier''), provides a member constant `value` equal to `false`. Otherwise, provides a member constant `value` equal to `std::is_assignable<T&, T&&>::value`.
2. Same as , but uses `std::is_trivially_assignable<T&, T&&>`.
3. Same as , but uses `std::is_nothrow_assignable<T&, T&&>`.

## Helper variable templates


```cpp
dcl|since=c++17|1=
template< class T >
inline constexpr bool is_move_assignable_v =
is_move_assignable<T>::value;
dcl|since=c++17|1=
template< class T >
inline constexpr bool is_trivially_move_assignable_v =
is_trivially_move_assignable<T>::value;
dcl|since=c++17|1=
template< class T >
inline constexpr bool is_nothrow_move_assignable_v =
is_nothrow_move_assignable<T>::value;
```


## Possible implementation

eq fun
|1=
template<class T>
struct is_move_assignable
: std::is_assignable<typename std::add_lvalue_reference<T>::type,
typename std::add_rvalue_reference<T>::type> {};
template<class T>
struct is_trivially_move_assignable
: std::is_trivially_assignable<typename std::add_lvalue_reference<T>::type,
typename std::add_rvalue_reference<T>::type> {};
template<class T>
struct is_nothrow_move_assignable
: std::is_nothrow_assignable<typename std::add_lvalue_reference<T>::type,
typename std::add_rvalue_reference<T>::type> {};

## Notes

The trait `std::is_move_assignable` is less strict than *MoveAssignable* because it does not check the type of the result of the assignment (which, for a *MoveAssignable* type, must be `T&`), nor the semantic requirement that the target's value after the assignment is equivalent to the source's value before the assignment.
The type does not have to implement a move assignment operator in order to satisfy this trait; see *MoveAssignable* for details.

## Example


### Example

```cpp
#include <iostream>
#include <string>
#include <type_traits>

struct Foo { int n; };

struct NoMove
{
    // prevents implicit declaration of default move assignment operator
    // however, the class is still move-assignable because its
    // copy assignment operator can bind to an rvalue argument
    NoMove& operator=(const NoMove&) { return *this; }
};

int main()
{
    std::cout << std::boolalpha
              << "std::string is nothrow move-assignable? "
              << std::is_nothrow_move_assignable<std::string>::value << '\n'
              << "int[2] is move-assignable? "
              << std::is_move_assignable<int[2]>::value << '\n'
              << "Foo is trivially move-assignable? "
              << std::is_trivially_move_assignable<Foo>::value << '\n'
              << "NoMove is move-assignable? "
              << std::is_move_assignable<NoMove>::value << '\n'
              << "NoMove is nothrow move-assignable? "
              << std::is_nothrow_move_assignable<NoMove>::value << '\n';
}
```


**Output:**
```
std::string is nothrow move-assignable? true
int[2] is move-assignable? false
Foo is trivially move-assignable? true
NoMove is move-assignable? true
NoMove is nothrow move-assignable? false
```


## Defect reports


## See also


| cpp/types/dsc is_assignable | (see dedicated page) |
| cpp/types/dsc is_copy_assignable | (see dedicated page) |

