---
title: std::ranges::ref_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/ref_view
---

ddcl|header=ranges|since=c++20|
template< ranges::range R >
requires std::is_object_v<R>
class ref_view
: public ranges::view_interface<ref_view<R>>
`ref_view` is a  of the elements of some other . It wraps a reference to that `range`.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions

member|ref_view|2=
ddcl|since=c++20|
template< /*different-from*/<ref_view> T >
requires std::convertible_to<T, R&> &&
requires { _FUN(std::declval<T>()); }
constexpr ref_view( T&& t );
Initializes  with `std::addressof(static_cast<R&>(std::forward<T>(t)))`.
`/*different-from*/<T, U>` is satisfied if and only if `std::remove_cvref_t<T>` and `std::remove_cvref_t<U>` are not the same type, and overloads of  are declared as `1=void _FUN(R&); void _FUN(R&&) = delete;`.

## Parameters


### Parameters

- `t` - range to reference
member|base|
ddcl|since=c++20|
constexpr R& base() const;
Returns .
member|begin|
ddcl|since=c++20|
constexpr ranges::iterator_t<R> begin() const;
Returns .
member|end|
ddcl|since=c++20|
constexpr ranges::sentinel_t<R> end() const;
Returns .
member|empty|
ddcl|since=c++20|
constexpr bool empty() const
requires requires { ranges::empty(*r_); };
Returns .
member|size|
ddcl|since=c++20|
constexpr auto size() const
requires ranges::sized_range<R>;
Returns .
member|reserve_hint|
ddcl|since=c++26|
constexpr auto size() const
requires ranges::approximately_sized_range<R>;
Returns .
member|data|
ddcl|since=c++20|
constexpr auto data() const
requires ranges::contiguous_range<R>;
Returns .

## Deduction guides

ddcl|since=c++20|
template< class R >
ref_view( R& ) -> ref_view<R>;

## Helper templates

ddcl|since=c++20|1=
template< class T >
constexpr bool enable_borrowed_range<ranges::ref_view<T>> = true;
This specialization of `std::ranges::enable_borrowed_range` makes `ref_view` satisfy .

## Notes


## Example


### Example

```cpp
#include <iostream>
#include <ranges>

int main()
{
    const std::string s{"cosmos"};

    const std::ranges::take_view tv{s, 3};
    const std::ranges::ref_view rv{tv};

    std::cout
        << std::boolalpha
        << "call empty(): " << rv.empty() << '\n'
        << "call size() : " << rv.size() << '\n'
        << "call begin(): " << *rv.begin() << '\n'
        << "call end()  : " << *(rv.end() - 1) << '\n'
        << "call data() : " << rv.data() << '\n'
        << "call base() : " << rv.base().size() << '\n' // ~> tv.size()
        << "range-for   : ";

    for (const auto c : rv)
        std::cout << c;
    std::cout << '\n';
}
```


**Output:**
```
call empty(): false
call size() : 3
call begin(): c
call end()  : s
call data() : cosmos
call base() : 3
range-for   : cos
```


## Defect reports


## See also


| cpp/utility/functional/dsc reference_wrapper | (see dedicated page) |
| cpp/ranges/dsc owning_view | (see dedicated page) |
| cpp/ranges/dsc all_view | (see dedicated page) |

