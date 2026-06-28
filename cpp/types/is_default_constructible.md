---
title: std::is_default_constructible
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_default_constructible
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|num=1|
template< class T >
struct is_default_constructible;
dcl|since=c++11|num=2|
template< class T >
struct is_trivially_default_constructible;
dcl|since=c++11|num=3|
template< class T >
struct is_nothrow_default_constructible;
```

1. Provides the member constant `value` equal to `std::is_constructible<T>::value`.
2. Provides the member constant `value` equal to `std::is_trivially_constructible<T>::value`.
3. Provides the member constant `value` equal to `std::is_nothrow_constructible<T>::value`.

## Helper variable templates


```cpp
dcl|since=c++17|1=
template< class T >
inline constexpr bool is_default_constructible_v =
is_default_constructible<T>::value;
dcl|since=c++17|1=
template< class T >
inline constexpr bool is_trivially_default_constructible_v =
is_trivially_default_constructible<T>::value;
dcl|since=c++17|1=
template< class T >
inline constexpr bool is_nothrow_default_constructible_v =
is_nothrow_default_constructible<T>::value;
```


## Possible implementation

eq fun
|1=
template<class T>
struct is_default_constructible : std::is_constructible<T> {};
template<class T>
struct is_trivially_default_constructible : std::is_trivially_constructible<T> {};
template<class T>
struct is_nothrow_default_constructible : std::is_nothrow_constructible<T> {};

## Notes

In many implementations, `std::is_nothrow_default_constructible` also checks if the destructor throws because it is effectively `noexcept(T())`. Same applies to `std::is_trivially_default_constructible`, which, in these implementations, also requires that the destructor is trivial: [https://gcc.gnu.org/bugzilla/show_bug.cgi?id=51452 GCC bug 51452], .
`std::is_default_constructible<T>` does not test that `T x;` would compile; it attempts direct-initialization with an empty argument list (see `std::is_constructible`). Thus, `std::is_default_constructible_v<const int>` and `std::is_default_constructible_v<const int[10]>` are `true`.

## Example


### Example

```cpp
#include <string>
#include <type_traits>

struct S1
{
    std::string str; // member has a non-trivial default constructor
};
static_assert(std::is_default_constructible_v<S1> == true);
static_assert(std::is_trivially_default_constructible_v<S1> == false);

struct S2
{
    int n;
    S2() = default; // trivial and non-throwing
};
static_assert(std::is_trivially_default_constructible_v<S2> == true);
static_assert(std::is_nothrow_default_constructible_v<S2> == true);

int main() {}
```


## See also


| cpp/types/dsc is_constructible | (see dedicated page) |
| cpp/types/dsc is_copy_constructible | (see dedicated page) |
| cpp/types/dsc is_move_constructible | (see dedicated page) |
| cpp/concepts/dsc default_initializable | (see dedicated page) |

