---
title: operators (std::basic_string_view)
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/operator_cmp
---


# 1=operator==,!=,<,<=,>,>=,<=>small|(std::basic_string_view)


```cpp
**Header:** `<`string_view`>`
dcl rev multi|num=1
|since1=c++17|dcl1=
template< class CharT, class Traits >
constexpr bool operator==( std::basic_string_view<CharT,Traits> lhs,
std::basic_string_view<CharT,Traits> rhs ) noexcept;
|since2=c++20|dcl2=
template< class CharT, class Traits >
constexpr bool operator==(
std::basic_string_view<CharT,Traits> lhs,
std::type_identity_t<std::basic_string_view<CharT,Traits>> rhs ) noexcept;
dcl|num=2|since=c++17|until=c++20|1=
template< class CharT, class Traits >
constexpr bool operator!=( std::basic_string_view<CharT,Traits> lhs,
std::basic_string_view<CharT,Traits> rhs ) noexcept;
dcl|num=3|since=c++17|until=c++20|1=
template< class CharT, class Traits >
constexpr bool operator<( std::basic_string_view<CharT,Traits> lhs,
std::basic_string_view<CharT,Traits> rhs ) noexcept;
dcl|num=4|since=c++17|until=c++20|1=
template< class CharT, class Traits >
constexpr bool operator<=( std::basic_string_view<CharT,Traits> lhs,
std::basic_string_view<CharT,Traits> rhs ) noexcept;
dcl|num=5|since=c++17|until=c++20|1=
template< class CharT, class Traits >
constexpr bool operator>( std::basic_string_view<CharT,Traits> lhs,
std::basic_string_view<CharT,Traits> rhs ) noexcept;
dcl|num=6|since=c++17|until=c++20|1=
template< class CharT, class Traits >
constexpr bool operator>=( std::basic_string_view<CharT,Traits> lhs,
std::basic_string_view<CharT,Traits> rhs ) noexcept;
dcl|num=7|since=c++20|1=
template< class CharT, class Traits >
constexpr /*comp-cat*/ operator<=>(
std::basic_string_view<CharT,Traits> lhs,
std::type_identity_t<std::basic_string_view<CharT,Traits>> rhs ) noexcept;
```

Compares two views.
All comparisons are done via the `compare()` member function (which itself is defined in terms of `Traits::compare()`):
* Two views are equal if both the size of `lhs` and `rhs` are equal and each character in `lhs` has an equivalent character in `rhs` at the same position.
* The ordering comparisons are done lexicographically – the comparison is performed by a function equivalent to `std::lexicographical_compare`.
rrev multi
|rev1=
The implementation provides sufficient additional `constexpr` and `noexcept` overloads of these functions so that a `basic_string_view<CharT,Traits>` object `sv` may be compared to another object `t` with an implicit conversion to `basic_string_view<CharT,Traits>`, with semantics identical to comparing `sv` and `basic_string_view<CharT,Traits>(t)`.
|since2=c++20|rev2=
The return type of three-way comparison operators (`/*comp-cat*/`) is `Traits::comparison_category` if that qualified-id denotes a type, `std::weak_ordering` otherwise. If `/*comp-cat*/` is not a comparison category type, the program is ill-formed.

## Parameters


### Parameters

- `lhs, rhs` - views to compare

## Return value

@1-6@ `true` if the corresponding comparison holds, `false` otherwise.
7. `1=static_cast</*comp-cat*/>(lhs.compare(rhs) <=> 0)`.

## Complexity

Linear in the size of the views.

## Notes

rrev multi
|rev1=
Sufficient additional overloads can be implemented through non-deduced context in one parameter type.
|since2=c++20|rev2=
Three-way comparison result type of `std::string_view`, `std::wstring_view`, `std::u8string_view`, `std::u16string_view` and `std::u32string_view` is `std::strong_ordering`.
`std::type_identity_t` is used for non-deduced context, which makes arguments that implicitly convertible to the string view type comparable with the string view.

## Example


### Example

```cpp
#include <string_view>

int main()
{
    using namespace std::literals;

    static_assert(""sv == ""sv);

    static_assert(""sv == "", "Selects an additional overload until C++20.");

    static_assert("" == ""sv, "Selects an additional overload until C++20."
                              "Uses a rewritten candidate since C++20.");

    static_assert(!(""sv != ""sv), "Uses the rewritten candidate since C++20.");

    static_assert(!(""sv != ""), "Selects an additional overload until C++20;"
                                 "Uses a rewritten candidate since C++20.");

    static_assert(!("" != ""sv), "Selects an additional overload until C++20."
                                 "Uses a rewritten candidate since C++20.");
}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3950 | C++20 | redundant additional overloads were still required | overload sets reduced |

