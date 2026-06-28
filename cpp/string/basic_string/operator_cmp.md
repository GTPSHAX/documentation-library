---
title: operators (std::basic_string)
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/operator_cmp
---


# 1=operator==,!=,<,<=,>,>=,<=>small|(std::basic_string)


```cpp
**Header:** `<`string`>`
<br><sup>(constexpr C++20)</sup>|1=
template< class CharT, class Traits, class Alloc >
bool operator==( const std::basic_string<CharT,Traits,Alloc>& lhs,
const std::basic_string<CharT,Traits,Alloc>& rhs );
|1=
template< class CharT, class Traits, class Alloc >
bool operator!=( const std::basic_string<CharT,Traits,Alloc>& lhs,
const std::basic_string<CharT,Traits,Alloc>& rhs );
|1=
template< class CharT, class Traits, class Alloc >
bool operator<( const std::basic_string<CharT,Traits,Alloc>& lhs,
const std::basic_string<CharT,Traits,Alloc>& rhs );
|1=
template< class CharT, class Traits, class Alloc >
bool operator<=( const std::basic_string<CharT,Traits,Alloc>& lhs,
const std::basic_string<CharT,Traits,Alloc>& rhs );
|1=
template< class CharT, class Traits, class Alloc >
bool operator>( const std::basic_string<CharT,Traits,Alloc>& lhs,
const std::basic_string<CharT,Traits,Alloc>& rhs );
|1=
template< class CharT, class Traits, class Alloc >
bool operator>=( const std::basic_string<CharT,Traits,Alloc>& lhs,
const std::basic_string<CharT,Traits,Alloc>& rhs );
dcl|num=7|since=c++20|1=
template< class CharT, class Traits, class Alloc >
constexpr /*comp-cat*/
operator<=>( const std::basic_string<CharT,Traits,Alloc>& lhs,
const std::basic_string<CharT,Traits,Alloc>& rhs ) noexcept;
|1=
template< class CharT, class Traits, class Alloc >
bool operator==( const std::basic_string<CharT,Traits,Alloc>& lhs,
const CharT* rhs );
dcl|num=9|until=c++20|1=
template< class CharT, class Traits, class Alloc >
bool operator==( const CharT* lhs,
const std::basic_string<CharT,Traits,Alloc>& rhs );
dcl|num=10|until=c++20|1=
template< class CharT, class Traits, class Alloc >
bool operator!=( const std::basic_string<CharT,Traits,Alloc>& lhs,
const CharT* rhs );
dcl|num=11|until=c++20|1=
template< class CharT, class Traits, class Alloc >
bool operator!=( const CharT* lhs,
const std::basic_string<CharT,Traits,Alloc>& rhs );
dcl|num=12|until=c++20|1=
template< class CharT, class Traits, class Alloc >
bool operator<( const std::basic_string<CharT,Traits,Alloc>& lhs,
const CharT* rhs );
dcl|num=13|until=c++20|1=
template< class CharT, class Traits, class Alloc >
bool operator<( const CharT* lhs,
const std::basic_string<CharT,Traits,Alloc>& rhs );
dcl|num=14|until=c++20|1=
template< class CharT, class Traits, class Alloc >
bool operator<=( const std::basic_string<CharT,Traits,Alloc>& lhs,
const CharT* rhs );
dcl|num=15|until=c++20|1=
template< class CharT, class Traits, class Alloc >
bool operator<=( const CharT* lhs,
const std::basic_string<CharT,Traits,Alloc>& rhs );
dcl|num=16|until=c++20|1=
template< class CharT, class Traits, class Alloc >
bool operator>( const std::basic_string<CharT,Traits,Alloc>& lhs,
const CharT* rhs );
dcl|num=17|until=c++20|1=
template< class CharT, class Traits, class Alloc >
bool operator>( const CharT* lhs,
const std::basic_string<CharT,Traits,Alloc>& rhs );
dcl|num=18|until=c++20|1=
template< class CharT, class Traits, class Alloc >
bool operator>=( const std::basic_string<CharT,Traits,Alloc>& lhs,
const CharT* rhs );
dcl|num=19|until=c++20|1=
template< class CharT, class Traits, class Alloc >
bool operator>=( const CharT* lhs,
const std::basic_string<CharT,Traits,Alloc>& rhs );
dcl|num=20|since=c++20|1=
template< class CharT, class Traits, class Alloc >
constexpr /*comp-cat*/
operator<=>( const std::basic_string<CharT,Traits,Alloc>& lhs,
const CharT* rhs );
```

Compares the contents of a string with another string or a null-terminated array of `CharT`.
All comparisons are done via the `compare()` member function (which itself is defined in terms of `Traits::compare()`):
* Two strings are equal if both the size of `lhs` and `rhs` are equal and each character in `lhs` has equivalent character in `rhs` at the same position.
* The ordering comparisons are done lexicographically &ndash; the comparison is performed by a function equivalent to `std::lexicographical_compare`<sup>(since C++20)</sup> or `std::lexicographical_compare_three_way`.
@1-7@ Compares two `basic_string` objects.
@8-20@ Compares a `basic_string` object and a null-terminated array of `CharT`.
rrev|since=c++20|
The return type of three-way comparison operators (`/*comp-cat*/`) is `Traits::comparison_category` if that qualified-id exists and denotes a type, `std::weak_ordering` otherwise. If `/*comp-cat*/` is not a comparison category type, the program is ill-formed.

## Parameters


### Parameters

- `lhs, rhs` - strings whose contents to compare

## Return value

@1-6,8-19@ `true` if the corresponding comparison holds, `false` otherwise.
@7,20@ `1=static_cast</*comp-cat*/>(lhs.compare(rhs) <=> 0)`.

## Complexity

Linear in the size of the strings.

## Notes

rrev|since=c++20|
If at least one parameter is of type `std::string`, `std::wstring`, `std::u8string`, `std::u16string`, or `std::u32string`, the return type of `1=operator<=>` is `std::strong_ordering`.

## Example


## Defect reports

