---
title: std::is_convertible
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_convertible
---


```cpp
**Header:** `<`type_traits`>`
dcla|since=c++11|num=1|1=
template< class From, class To >
struct is_convertible;
dcla|since=c++20|num=2|1=
template< class From, class To >
struct is_nothrow_convertible;
```

1. If the imaginary function definition } is well-formed, (that is, either `std::declval<From>()` can be converted to `To` using implicit conversions, or both `From` and `To` are possibly cv-qualified `void`), provides the member constant `value` equal to `true`. Otherwise `value` is `false`. For the purposes of this check, the use of `std::declval` in the return statement is not considered an .
rrev|since=c++26|
If `To` is a reference type and a temporary object would be created when binding `std::declval<From>()` to `To`, the `return` statement in the imaginary function is considered well-formed, even though such binding is ill-formed in an actual function.
@@ Access checks are performed as if from a context unrelated to either type. Only the validity of the immediate context of the expression in the return statement (including conversions to the return type) is considered.
2. Same as , but the conversion is also `noexcept`.

## Helper variable template


```cpp
dcl|since=c++17|1=
template< class From, class To >
constexpr bool is_convertible_v = is_convertible<From, To>::value;
dcl|since=c++20|1=
template< class From, class To >
constexpr bool is_nothrow_convertible_v = is_nothrow_convertible<From, To>::value;
```


## Possible implementation

eq impl
|title1=`is_convertible` (1)|ver1=1|1=
namespace detail
{
template<class T>
auto test_returnable(int) -> decltype(
void(static_cast<T(*)()>(nullptr)), std::true_type{}
);
template<class>
auto test_returnable(...) -> std::false_type;
template<class From, class To>
auto test_implicitly_convertible(int) -> decltype(
void(std::declval<void(&)(To)>()(std::declval<From>())), std::true_type{}
);
template<class, class>
auto test_implicitly_convertible(...) -> std::false_type;
} // namespace detail
template<class From, class To>
struct is_convertible : std::integral_constant<bool,
(decltype(detail::test_returnable<To>(0))::value &&
decltype(detail::test_implicitly_convertible<From, To>(0))::value)
(std::is_void<From>::value && std::is_void<To>::value)
> {};
|title2=`is_nothrow_convertible` (2)|ver2=2|2=
template<class From, class To>
struct is_nothrow_convertible : std::conjunction<std::is_void<From>, std::is_void<To>> {};
template<class From, class To>
requires
requires
{
static_cast<To(*)()>(nullptr);
{ std::declval<void(&)(To) noexcept>()(std::declval<From>()) } noexcept;
}
struct is_nothrow_convertible<From, To> : std::true_type {};

## Notes

Gives well-defined results for reference types, void types, array types, and function types.
Currently the standard has not specified whether the destruction of the object produced by the conversion (either a result object or a temporary bound to a reference) is considered as a part of the conversion. This is .
All known implementations treat the destruction as a part of the conversion, as proposed in .

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <string>
#include <string_view>
#include <type_traits>

class E { public: template<class T> E(T&&) {} };

int main()
{
    class A {};
    class B : public A {};
    class C {};
    class D { public: operator C() { return c; } C c; };

    static_assert(std::is_convertible_v<B*, A*>);
    static_assert(!std::is_convertible_v<A*, B*>);
    static_assert(std::is_convertible_v<D, C>);
    static_assert(!std::is_convertible_v<B*, C*>);
    // Note that the Perfect Forwarding constructor makes the class E be
    // "convertible" from everything. So, A is replaceable by B, C, D..:
    static_assert(std::is_convertible_v<A, E>);

    static_assert(!std::is_convertible_v<std::string_view, std::string>);
    static_assert(std::is_convertible_v<std::string, std::string_view>);

    auto stringify = []<typename T>(T x)
    {
        if constexpr (std::is_convertible_v<T, std::string> or
                      std::is_convertible_v<T, std::string_view>)
            return x;
        else
            return std::to_string(x);
    };

    using std::operator "" s, std::operator "" sv;
    const char* three = "three";

    std::cout << std::quoted(stringify("one"s)) << ' '
              << std::quoted(stringify("two"sv)) << ' '
              << std::quoted(stringify(three)) << ' '
              << std::quoted(stringify(42)) << ' '
              << std::quoted(stringify(42.0)) << '\n';
}
```


**Output:**
```
"one" "two" "three" "42" "42.000000"
```


## See also


| cpp/types/dsc is_base_of | (see dedicated page) |
| cpp/types/dsc is_pointer_interconvertible_base_of | (see dedicated page) |
| cpp/types/dsc is_pointer_interconvertible_with_class | (see dedicated page) |
| cpp/concepts/dsc convertible_to | (see dedicated page) |

