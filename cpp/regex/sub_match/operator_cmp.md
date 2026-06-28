---
title: operators (std::sub_match)
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/sub_match/operator_cmp
---


# 1=operator==,!=,<,<=,>,>=,<=>petty|(std::sub_match)


```cpp
**Header:** `<`regex`>`
dcl|num=1|since=c++11|1=
template< class BidirIt >
bool operator== ( const std::sub_match<BidirIt>& lhs,
const std::sub_match<BidirIt>& rhs );
dcl|num=2|since=c++11|until=c++20|1=
template< class BidirIt >
bool operator!= ( const std::sub_match<BidirIt>& lhs,
const std::sub_match<BidirIt>& rhs );
dcl|num=3|since=c++11|until=c++20|
template< class BidirIt >
bool operator<  ( const std::sub_match<BidirIt>& lhs,
const std::sub_match<BidirIt>& rhs );
dcl|num=4|since=c++11|until=c++20|1=
template< class BidirIt >
bool operator<= ( const std::sub_match<BidirIt>& lhs,
const std::sub_match<BidirIt>& rhs );
dcl|num=5|since=c++11|until=c++20|
template< class BidirIt >
bool operator>  ( const std::sub_match<BidirIt>& lhs,
const std::sub_match<BidirIt>& rhs );
dcl|num=6|since=c++11|until=c++20|1=
template< class BidirIt >
bool operator>= ( const std::sub_match<BidirIt>& lhs,
const std::sub_match<BidirIt>& rhs );
dcl|num=7|since=c++20|1=
template< class BidirIt >
auto operator<=>( const std::sub_match<BidirIt>& lhs,
const std::sub_match<BidirIt>& rhs );
dcl|num=8|since=c++11|1=
template< class BidirIt, class Traits, class Alloc >
bool operator== ( const std::sub_match<BidirIt>& lhs,
const std::basic_string</*value-type-of*/<BidirIt>,
Traits, Alloc>& str );
dcl|num=9|since=c++11|until=c++20|1=
template< class BidirIt, class Traits, class Alloc >
bool operator!= ( const std::sub_match<BidirIt>& lhs,
const std::basic_string</*value-type-of*/<BidirIt>,
Traits, Alloc>& str );
dcl|num=10|since=c++11|until=c++20|
template< class BidirIt, class Traits, class Alloc >
bool operator<  ( const std::sub_match<BidirIt>& lhs,
const std::basic_string</*value-type-of*/<BidirIt>,
Traits, Alloc>& str );
dcl|num=11|since=c++11|until=c++20|1=
template< class BidirIt, class Traits, class Alloc >
bool operator<= ( const std::sub_match<BidirIt>& lhs,
const std::basic_string</*value-type-of*/<BidirIt>,
Traits, Alloc>& str );
dcl|num=12|since=c++11|until=c++20|
template< class BidirIt, class Traits, class Alloc >
bool operator>  ( const std::sub_match<BidirIt>& lhs,
const std::basic_string</*value-type-of*/<BidirIt>,
Traits, Alloc>& str );
dcl|num=13|since=c++11|until=c++20|1=
template< class BidirIt, class Traits, class Alloc >
bool operator>= ( const std::sub_match<BidirIt>& lhs,
const std::basic_string</*value-type-of*/<BidirIt>,
Traits, Alloc>& str );
dcl|num=14|since=c++20|1=
template< class BidirIt, class Traits, class Alloc >
auto operator<=>( const std::sub_match<BidirIt>& lhs,
const std::basic_string</*value-type-of*/<BidirIt>,
Traits, Alloc>& str );
dcl|num=15|since=c++11|until=c++20|1=
template< class BidirIt, class Traits, class Alloc >
bool operator== ( const std::basic_string</*value-type-of*/<BidirIt>,
Traits, Alloc>& str,
const std::sub_match<BidirIt>& rhs );
dcl|num=16|since=c++11|until=c++20|1=
template< class BidirIt, class Traits, class Alloc >
bool operator!= ( const std::basic_string</*value-type-of*/<BidirIt>,
Traits, Alloc>& str,
const std::sub_match<BidirIt>& rhs );
dcl|num=17|since=c++11|until=c++20|
template< class BidirIt, class Traits, class Alloc >
bool operator<  ( const std::basic_string</*value-type-of*/<BidirIt>,
Traits, Alloc>& str,
const std::sub_match<BidirIt>& rhs );
dcl|num=18|since=c++11|until=c++20|1=
template< class BidirIt, class Traits, class Alloc >
bool operator<= ( const std::basic_string</*value-type-of*/<BidirIt>,
Traits, Alloc>& str,
const std::sub_match<BidirIt>& rhs );
dcl|num=19|since=c++11|until=c++20|
template< class BidirIt, class Traits, class Alloc >
bool operator>  ( const std::basic_string</*value-type-of*/<BidirIt>,
Traits, Alloc>& str,
const std::sub_match<BidirIt>& rhs );
dcl|num=20|since=c++11|until=c++20|1=
template< class BidirIt, class Traits, class Alloc >
bool operator>= ( const std::basic_string</*value-type-of*/<BidirIt>,
Traits, Alloc>& str,
const std::sub_match<BidirIt>& rhs );
dcl|num=21|since=c++11|1=
template< class BidirIt >
bool operator== ( const std::sub_match<BidirIt>& lhs,
const /*value-type-of*/<BidirIt>* s );
dcl|num=22|since=c++11|until=c++20|1=
template< class BidirIt >
bool operator!= ( const std::sub_match<BidirIt>& lhs,
const /*value-type-of*/<BidirIt>* s );
dcl|num=23|since=c++11|until=c++20|
template< class BidirIt >
bool operator<  ( const std::sub_match<BidirIt>& lhs,
const /*value-type-of*/<BidirIt>* s );
dcl|num=24|since=c++11|until=c++20|1=
template< class BidirIt >
bool operator<= ( const std::sub_match<BidirIt>& lhs,
const /*value-type-of*/<BidirIt>* s );
dcl|num=25|since=c++11|until=c++20|
template< class BidirIt >
bool operator>  ( const std::sub_match<BidirIt>& lhs,
const /*value-type-of*/<BidirIt>* s );
dcl|num=26|since=c++11|until=c++20|1=
template< class BidirIt >
bool operator>= ( const std::sub_match<BidirIt>& lhs,
const /*value-type-of*/<BidirIt>* s );
dcl|num=27|since=c++20|1=
template< class BidirIt >
auto operator<=>( const std::sub_match<BidirIt>& lhs,
const /*value-type-of*/<BidirIt>* s );
dcl|num=28|since=c++11|until=c++20|1=
template< class BidirIt >
bool operator== ( const /*value-type-of*/<BidirIt>* s,
const std::sub_match<BidirIt>& rhs );
dcl|num=29|since=c++11|until=c++20|1=
template< class BidirIt >
bool operator!= ( const /*value-type-of*/<BidirIt>* s,
const std::sub_match<BidirIt>& rhs );
dcl|num=30|since=c++11|until=c++20|
template< class BidirIt >
bool operator<  ( const /*value-type-of*/<BidirIt>* s,
const std::sub_match<BidirIt>& rhs );
dcl|num=31|since=c++11|until=c++20|1=
template< class BidirIt >
bool operator<= ( const /*value-type-of*/<BidirIt>* s,
const std::sub_match<BidirIt>& rhs );
dcl|num=32|since=c++11|until=c++20|
template< class BidirIt >
bool operator>  ( const /*value-type-of*/<BidirIt>* s,
const std::sub_match<BidirIt>& rhs );
dcl|num=33|since=c++11|until=c++20|1=
template< class BidirIt >
bool operator>= ( const /*value-type-of*/<BidirIt>* s,
const std::sub_match<BidirIt>& rhs );
dcl|num=34|since=c++11|1=
template< class BidirIt >
bool operator== ( const std::sub_match<BidirIt>& lhs,
const /*value-type-of*/<BidirIt>& ch );
dcl|num=35|since=c++11|until=c++20|1=
template< class BidirIt >
bool operator!= ( const std::sub_match<BidirIt>& lhs,
const /*value-type-of*/<BidirIt>& ch );
dcl|num=36|since=c++11|until=c++20|
template< class BidirIt >
bool operator<  ( const std::sub_match<BidirIt>& lhs,
const /*value-type-of*/<BidirIt>& ch );
dcl|num=37|since=c++11|until=c++20|1=
template< class BidirIt >
bool operator<= ( const std::sub_match<BidirIt>& lhs,
const /*value-type-of*/<BidirIt>& ch );
dcl|num=38|since=c++11|until=c++20|
template< class BidirIt >
bool operator>  ( const std::sub_match<BidirIt>& lhs,
const /*value-type-of*/<BidirIt>& ch );
dcl|num=39|since=c++11|until=c++20|1=
template< class BidirIt >
bool operator>= ( const std::sub_match<BidirIt>& lhs,
const /*value-type-of*/<BidirIt>& ch );
dcl|num=40|since=c++20|1=
template< class BidirIt >
auto operator<=>( const std::sub_match<BidirIt>& lhs,
const /*value-type-of*/<BidirIt>& ch );
dcl|num=41|since=c++11|until=c++20|1=
template< class BidirIt >
bool operator== ( const /*value-type-of*/<BidirIt>& ch,
const std::sub_match<BidirIt>& rhs );
dcl|num=42|since=c++11|until=c++20|1=
template< class BidirIt >
bool operator!= ( const /*value-type-of*/<BidirIt>& ch,
const std::sub_match<BidirIt>& rhs );
dcl|num=43|since=c++11|until=c++20|
template< class BidirIt >
bool operator<  ( const /*value-type-of*/<BidirIt>& ch,
const std::sub_match<BidirIt>& rhs );
dcl|num=44|since=c++11|until=c++20|1=
template< class BidirIt >
bool operator<= ( const /*value-type-of*/<BidirIt>& ch,
const std::sub_match<BidirIt>& rhs );
dcl|num=45|since=c++11|until=c++20|
template< class BidirIt >
bool operator>  ( const /*value-type-of*/<BidirIt>& ch,
const std::sub_match<BidirIt>& rhs );
dcl|num=46|since=c++11|until=c++20|1=
template< class BidirIt >
bool operator>= ( const /*value-type-of*/<BidirIt>& ch,
const std::sub_match<BidirIt>& rhs );
dcla|num=47|expos=yes|1=
template< class BidirIt >
using /*value-type-of*/ =
typename std::iterator_traits<BidirIt>::value_type;
dcla|num=48|since=c++20|expos=yes|1=
template< class BidirIt >
using /*cat-type-of*/ =
std::compare_three_way_result_t
<std::basic_string</*value-type-of*/<BidirIt>>>;
```

Compares a `sub_match` to another `sub_match`, a `std::string`, a C-style string or a single character.
@1-7@ Compares two `sub_match` directly.
@8-20@ Compares a `sub_match` with a `std::basic_string`.
@21-33@ Compares a `sub_match` with a C-style string.
@34-46@ Compares a `sub_match` with a single character.
rrev|since=c++20|
47. `<BidirIt>` is the value type of `BidirIt`.
48. `<BidirIt>` is the result type of three-way comparison of `std::sub_match<BidirIt>`.

## Parameters


### Parameters

- `lhs, rhs` - a `sub_match` to compare
- `str` - a `std::basic_string` to compare
- `s` - a pointer to a C-style string to compare
- `ch` - a character to compare

## Return value

Let `target` be the following values:
@1-7@ `rhs`
@8-20@ `typename std::sub_match<BidirIt>::string_type(str.data(), str.size())`
@21-33@ `s`
@34-46@ `typename std::sub_match<BidirIt>::string_type(1, ch)`
The return values are defined as follows:


| rowspan=2 | Operator |
| colspan=2 | Return value |
| - |
| Overloads v | 1-14,21-27,34-40<br>normal | small | (overloads with parameter c | lhs) |
| nbsp | 6Overloads v | 15-20,28-33,41-46nbsp | 6<br>normal | small | (overloads without parameter c | lhs) |
| - |
| tt | 1=== |
| c | 1=lhs.compare(target) == 0 |
| c | 1=rhs.compare(target) == 0 |
| - |
| tt | 1=!= |
| c | 1=lhs.compare(target) != 0 |
| c | 1=rhs.compare(target) != 0 |
| - |
| tt | < |
| c | lhs.compare(target) < 0 |
| c | rhs.compare(target) > 0 |
| - |
| tt | 1=<= |
| c | 1=lhs.compare(target) <= 0 |
| c | 1=rhs.compare(target) >= 0 |
| - |
| tt | > |
| c | lhs.compare(target) > 0 |
| c | rhs.compare(target) < 0 |
| - |
| tt | 1=>= |
| c | 1=lhs.compare(target) >= 0 |
| c | 1=rhs.compare(target) <= 0 |
| - |
| tt | 1=<=> |
| <span style="text-align: start;">box | c/core | static_cast<tti | cat-type-ofc/core | 1=<BidirIt>><br>nbspt | 4c/core | 1=(lhs.compare(target) <=> 0)</span> |
|  |


## Notes

The return type of `1=operator<=>` is guaranteed to be a comparison category type. If `<BidirIt>` is `char`, `wchar_t`, `char8_t`, `char16_t`, or `char32_t`, the return type of `1=operator<=>` is .

## Example


## See also


| cpp/regex/sub_match/dsc compare | (see dedicated page) |

