---
title: std::is_copy_constructible
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_copy_constructible
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|num=1|
template< class T >
struct is_copy_constructible;
dcl|since=c++11|num=2|
template< class T >
struct is_trivially_copy_constructible;
dcl|since=c++11|num=3|
template< class T >
struct is_nothrow_copy_constructible;
```

1. If `T` is not a referenceable type (i.e., possibly cv-qualified `void` or a function type with a ''cv-qualifier-seq'' or a ''ref-qualifier''), provides a member constant `value` equal to `false`. Otherwise, provides a member constant `value` equal to `std::is_constructible<T, const T&>::value`.
2. Same as , but uses `std::is_trivially_constructible<T, const T&>`.
3. Same as , but uses `std::is_nothrow_constructible<T, const T&>`.

## Helper variable templates


```cpp
dcl|since=c++17|1=
template< class T >
inline constexpr bool is_copy_constructible_v =
is_copy_constructible<T>::value;
dcl|since=c++17|1=
template< class T >
inline constexpr bool is_trivially_copy_constructible_v =
is_trivially_copy_constructible<T>::value;
dcl|since=c++17|1=
template< class T >
inline constexpr bool is_nothrow_copy_constructible_v =
is_nothrow_copy_constructible<T>::value;
```


## Possible implementation

eq fun
|1=
template<class T>
struct is_copy_constructible :
std::is_constructible<T, typename std::add_lvalue_reference<
typename std::add_const<T>::type>::type> {};
template<class T>
struct is_trivially_copy_constructible :
std::is_trivially_constructible<T, typename std::add_lvalue_reference<
typename std::add_const<T>::type>::type> {};
template<class T>
struct is_nothrow_copy_constructible :
std::is_nothrow_constructible<T, typename std::add_lvalue_reference<
typename std::add_const<T>::type>::type> {};

## Notes

In many implementations, `is_nothrow_copy_constructible` also checks if the destructor throws because it is effectively `noexcept(T(arg))`. Same applies to `is_trivially_copy_constructible`, which, in these implementations, also requires that the destructor is trivial: [https://gcc.gnu.org/bugzilla/show_bug.cgi?id=51452 GCC bug 51452], .

## Example


### Example

```cpp
#include <string>
#include <type_traits>

struct S1
{
    std::string str; // member has a non-trivial copy constructor
};
static_assert(std::is_copy_constructible_v<S1>);
static_assert(!std::is_trivially_copy_constructible_v<S1>);

struct S2
{
    int n;
    S2(const S2&) = default; // trivial and non-throwing
};
static_assert(std::is_trivially_copy_constructible_v<S2>);
static_assert(std::is_nothrow_copy_constructible_v<S2>);

struct S3
{
    S3(const S3&) = delete; // explicitly deleted
};
static_assert(!std::is_copy_constructible_v<S3>);

struct S4
{
    S4(S4&) {}; // cannot bind const, hence not a copy-constructible
};
static_assert(!std::is_copy_constructible_v<S4>);

int main() {}
```


## Defect reports


## See also


| cpp/types/dsc is_constructible | (see dedicated page) |
| cpp/types/dsc is_default_constructible | (see dedicated page) |
| cpp/types/dsc is_move_constructible | (see dedicated page) |
| cpp/concepts/dsc copy_constructible | (see dedicated page) |

