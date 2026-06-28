---
title: std::is_constructible
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_constructible
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|num=1|1=
template< class T, class... Args >
struct is_constructible;
dcl|since=c++11|num=2|1=
template< class T, class... Args >
struct is_trivially_constructible;
dcl|since=c++11|num=3|1=
template< class T, class... Args >
struct is_nothrow_constructible;
```

1. If `T` is an object or reference type and the variable definition `T obj(std::declval<Args>()...);` is well-formed, provides the member constant `value` equal to `true`. In all other cases, `value` is `false`.<br />
For the purposes of this check, the variable definition is never interpreted as a function declaration, and the use of `std::declval` is not considered an odr-use. Access checks are performed as if from a context unrelated to `T` and any of the types in `Args`. Only the validity of the immediate context of the variable definition is considered.
2. Same as , but the variable definition does not call any operation that is not trivial. For the purposes of this check, the call to `std::declval` is considered trivial.
3. Same as , but the variable definition is `noexcept`.

## Helper variable templates


```cpp
dcl|since=c++17|1=
template< class T, class... Args >
inline constexpr bool is_constructible_v =
is_constructible<T, Args...>::value;
dcl|since=c++17|1=
template< class T, class... Args >
inline constexpr bool is_trivially_constructible_v =
is_trivially_constructible<T, Args...>::value;
dcl|since=c++17|1=
template< class T, class... Args >
inline constexpr bool is_nothrow_constructible_v =
is_nothrow_constructible<T, Args...>::value;
```


## Notes

In many implementations, `is_nothrow_constructible` also checks if the destructor throws because it is effectively `noexcept(T(arg))`. Same applies to `is_trivially_constructible`, which, in these implementations, also requires that the destructor is trivial: [https://gcc.gnu.org/bugzilla/show_bug.cgi?id=51452 GCC bug 51452] .

## Example


### Example

```cpp
#include <iostream>
#include <type_traits>

class Foo
{
    int v1;
    double v2;
public:
    Foo(int n) : v1(n), v2() {}
    Foo(int n, double f) noexcept : v1(n), v2(f) {}
};

int main()
{
    auto is = [](bool o) { return (o ? "\t" "is " : "\t" "isn't "); };
    std::cout << "Foo ...\n"
              << is(std::is_trivially_constructible_v<Foo, const Foo&>)
              << "Trivially-constructible from const Foo&\n"
              << is(std::is_trivially_constructible_v<Foo, int>)
              << "Trivially-constructible from int\n"
              << is(std::is_constructible_v<Foo, int>)
              << "Constructible from int\n"
              << is(std::is_nothrow_constructible_v<Foo, int>)
              << "Nothrow-constructible from int\n"
              << is(std::is_nothrow_constructible_v<Foo, int, double>)
              << "Nothrow-constructible from int and double\n";
}
```


**Output:**
```
Foo ...
        is Trivially-constructible from const Foo&
        isn't Trivially-constructible from int
        is Constructible from int
        isn't Nothrow-constructible from int
        is Nothrow-constructible from int and double
```


## See also


| cpp/types/dsc is_default_constructible | (see dedicated page) |
| cpp/types/dsc is_copy_constructible | (see dedicated page) |
| cpp/types/dsc is_move_constructible | (see dedicated page) |
| cpp/concepts/dsc constructible_from | (see dedicated page) |

