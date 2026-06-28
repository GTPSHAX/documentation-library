---
title: std::is_move_constructible
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_move_constructible
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|num=1|
template< class T >
struct is_move_constructible;
dcl|since=c++11|num=2|
template< class T >
struct is_trivially_move_constructible;
dcl|since=c++11|num=3|
template< class T >
struct is_nothrow_move_constructible;
```

1. If `T` is not a referenceable type (i.e., possibly cv-qualified `void` or a function type with a ''cv-qualifier-seq'' or a ''ref-qualifier''), provides a member constant `value` equal to `false`. Otherwise, provides a member constant `value` equal to `std::is_constructible<T, T&&>::value`.
2. Same as , but uses `std::is_trivially_constructible<T, T&&>`.
3. Same as , but uses `std::is_nothrow_constructible<T, T&&>`.

## Helper variable templates


```cpp
dcl|since=c++17|1=
template< class T >
inline constexpr bool is_move_constructible_v =
is_move_constructible<T>::value;
dcl|since=c++17|1=
template< class T >
inline constexpr bool is_trivially_move_constructible_v =
is_trivially_move_constructible<T>::value;
dcl|since=c++17|1=
template< class T >
inline constexpr bool is_nothrow_move_constructible_v =
is_nothrow_move_constructible<T>::value;
```


## Possible implementation

eq fun
|1=
template<class T>
struct is_move_constructible :
std::is_constructible<T, typename std::add_rvalue_reference<T>::type> {};
template<class T>
struct is_trivially_move_constructible :
std::is_trivially_constructible<T, typename std::add_rvalue_reference<T>::type> {};
template<class T>
struct is_nothrow_move_constructible :
std::is_nothrow_constructible<T, typename std::add_rvalue_reference<T>::type> {};

## Notes

Types without a move constructor, but with a copy constructor that accepts `const T&` arguments, satisfy `std::is_move_constructible`.
Move constructors are usually noexcept, since otherwise they are unusable in any code that provides strong exception guarantee.
In many implementations, `std::is_nothrow_move_constructible` also checks if the destructor throws because it is effectively `noexcept(T(arg))`. Same applies to `std::is_trivially_move_constructible`, which, in these implementations, also requires that the destructor is trivial: [https://gcc.gnu.org/bugzilla/show_bug.cgi?id=51452 GCC bug 51452], .

## Example


### Example

```cpp
#include <string>
#include <type_traits>

struct Ex1
{
    std::string str; // member has a non-trivial but non-throwing move constructor
};
static_assert(std::is_move_constructible_v<Ex1>);
static_assert(!std::is_trivially_move_constructible_v<Ex1>);
static_assert(std::is_nothrow_move_constructible_v<Ex1>);

struct Ex2
{
    int n;
    Ex2(Ex2&&) = default; // trivial and non-throwing
};
static_assert(std::is_move_constructible_v<Ex2>);
static_assert(std::is_trivially_move_constructible_v<Ex2>);
static_assert(std::is_nothrow_move_constructible_v<Ex2>);

struct NoMove1
{
    // prevents implicit declaration of default move constructor;
    // however, the class is still move-constructible because its
    // copy constructor can bind to an rvalue argument
    NoMove1(const NoMove1&) {}
};
static_assert(std::is_move_constructible_v<NoMove1>);
static_assert(!std::is_trivially_move_constructible_v<NoMove1>);
static_assert(!std::is_nothrow_move_constructible_v<NoMove1>);

struct NoMove2
{
    // Not move-constructible since the lvalue reference
    // can't bind to the rvalue argument
    NoMove2(NoMove2&) {}
};
static_assert(!std::is_move_constructible_v<NoMove2>);
static_assert(!std::is_trivially_move_constructible_v<NoMove2>);
static_assert(!std::is_nothrow_move_constructible_v<NoMove2>);

int main() {}
```


## Defect reports


## See also


| cpp/types/dsc is_constructible | (see dedicated page) |
| cpp/types/dsc is_default_constructible | (see dedicated page) |
| cpp/types/dsc is_copy_constructible | (see dedicated page) |
| cpp/concepts/dsc move_constructible | (see dedicated page) |
| cpp/utility/dsc move | (see dedicated page) |
| cpp/utility/dsc move_if_noexcept | (see dedicated page) |

