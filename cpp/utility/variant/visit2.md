---
title: std::variant::visit
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variant/visit2
---


```cpp
**Header:** `<`variant`>`
dcl|since=c++17|num=1|
template< class Visitor, class... Variants >
constexpr /* see below */ visit( Visitor&& v, Variants&&... values );
dcl|since=c++20|num=2|
template< class R, class Visitor, class... Variants >
constexpr R visit( Visitor&& v, Variants&&... values );
|num=3|
template< class... Ts >
auto&& as-variant( std::variant<Ts...>& value );
|num=4|
template< class... Ts >
auto&& as-variant( const std::variant<Ts...>& value );
|num=5|
template< class... Ts >
auto&& as-variant( std::variant<Ts...>&& value );
|num=6|
template< class... Ts >
auto&& as-variant( const std::variant<Ts...>&& value );
```

Applies the visitor `v` (a *Callable* that can be called with any combination of types from Variants) to the Variants `values`.
Given `VariantBases` as `decltype(``(std::forward<Variants>(values))...` (a pack of `sizeof...(Variants)` types):
1. Invokes `v` as if by
,
where `indices` is .
2. Invokes `v` as if by
,
where `indices` is .
If the expression denoted by <sup>(since C++20)</sup>  or  is invalid, or the results of <sup>(since C++20)</sup>  or  have different types or value categories for different `indices`, the program is ill-formed.
@3-6@ The exposition-only  function templates accept a value whose type can be deduced for `std::variant<Ts...>` (i.e., either `std::variant<Ts...>` or a type derived from `std::variant<Ts...>`), and return the `std::variant` value with the same const-qualification and value category.
:@3,4@ Returns `value`.
:@5,6@ Returns `std::move(value)`.

## Parameters


### Parameters

- `v` - a *Callable* that accepts every possible alternative from every variant in `Variants`
- `values` - list of variants to pass to the visitor

## Return value

1. The result of the  operation. The return type is the type obtained from applying `cpp/language/decltype` to the result.
2. Nothing if `R` is (possibly cv-qualified) `void`; otherwise the result of the  operation.
@3-6@ A `std::variant` value converted from `value`.

## Exceptions

Throws `std::bad_variant_access` if  is `true` for any variant `value_i` in `values`.

## Complexity

When the number of variants is zero or one, the invocation of the callable object is implemented in constant time; i.e., it does not depend on the number of types can be stored in the variant.
If the number of variants is larger than one, the invocation of the callable object has no complexity requirements.

## Notes

Let `n` be `(1 * ... * std::variant_size_v<std::remove_reference_t<VariantBases>>)`, implementations usually generate a table equivalent to an (possibly multidimensional) array of `n` function pointers for every specialization of `std::visit`, which is similar to the implementation of virtual functions.
Implementations may also generate a switch statement with `n` branches for `std::visit` (e.g., the MSVC STL implementation uses a switch statement when `n` is not greater than 256).
On typical implementations, the time complexity of the invocation of `v` can be considered equal to that of access to an element in an (possibly multidimensional) array or execution of a switch statement.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <string>
#include <type_traits>
#include <variant>
#include <vector>

// the variant to visit
using value_t = std::variant<int, long, double, std::string>;

// helper type for the visitor #4
template<class... Ts>
struct overloaded : Ts... { using Ts::operator()...; };
// explicit deduction guide (not needed as of C++20)
template<class... Ts>
overloaded(Ts...) -> overloaded<Ts...>;

int main()
{
    std::vector<value_t> vec = {10, 15l, 1.5, "hello"};

    for (auto& v: vec)
    {
        // 1. void visitor, only called for side-effects (here, for I/O)
        std::visit([](auto&& arg){ std::cout << arg; }, v);

        // 2. value-returning visitor, demonstrates the idiom of returning another variant
        value_t w = std::visit([](auto&& arg) -> value_t { return arg + arg; }, v);

        // 3. type-matching visitor: a lambda that handles each type differently
        std::cout << ". After doubling, variant holds ";
        std::visit([](auto&& arg)
        {
            using T = std::decay_t<decltype(arg)>;
            if constexpr (std::is_same_v<T, int>)
                std::cout << "int with value " << arg << '\n';
            else if constexpr (std::is_same_v<T, long>)
                std::cout << "long with value " << arg << '\n';
            else if constexpr (std::is_same_v<T, double>)
                std::cout << "double with value " << arg << '\n';
            else if constexpr (std::is_same_v<T, std::string>)
                std::cout << "std::string with value " << std::quoted(arg) << '\n';
            else
                static_assert(false, "non-exhaustive visitor!");
        }, w);
    }

    for (auto& v: vec)
    {
        // 4. another type-matching visitor: a class with 3 overloaded operator()'s
        // Note: The `(auto arg)` template operator() will bind to `int` and `long`
        //       in this case, but in its absence the `(double arg)` operator()
        //       *will also* bind to `int` and `long` because both are implicitly
        //       convertible to double. When using this form, care has to be taken
        //       that implicit conversions are handled correctly.
        std::visit(overloaded{
            [](auto arg) { std::cout << arg << ' '; },
            [](double arg) { std::cout << std::fixed << arg << ' '; },
            [](const std::string& arg) { std::cout << std::quoted(arg) << ' '; }
        }, v);
    }
}
```


**Output:**
```
10. After doubling, variant holds int with value 20
15. After doubling, variant holds long with value 30
1.5. After doubling, variant holds double with value 3
hello. After doubling, variant holds std::string with value "hellohello"
10 15 1.500000 "hello"
```


## Defect reports


## See also


| cpp/utility/variant/dsc visit | (see dedicated page) |
| cpp/utility/variant/dsc swap | (see dedicated page) |

