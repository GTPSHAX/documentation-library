---
title: std::basic_string_view::compare
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/compare
---


```cpp
dcl|num=1|since=c++17|
constexpr int compare( basic_string_view v ) const noexcept;
dcl|num=2|since=c++17|
constexpr int compare( size_type pos1, size_type count1,
basic_string_view v ) const;
dcl|num=3|since=c++17|
constexpr int compare( size_type pos1, size_type count1, basic_string_view v,
size_type pos2, size_type count2 ) const;
dcl|num=4|since=c++17|
constexpr int compare( const CharT* s ) const;
dcl|num=5|since=c++17|
constexpr int compare( size_type pos1, size_type count1,
const CharT* s ) const;
dcl|num=6|since=c++17|
constexpr int compare( size_type pos1, size_type count1,
const CharT* s, size_type count2 ) const;
```

Compares two character sequences.
1. The length `rlen` of the sequences to compare is the smaller of `size()` and `v.size()`. The function compares the two views by calling `traits::compare(data(), v.data(), rlen)`, and returns a value according to the following table:


| colspan=2 | Condition |
| Result |
| Return value |
| - |
| colspan=2 style="text-align:left;" | tt | Traits::compare(data(), v.data(), spar | rlen) < 0 |
| tt | this is ''less'' than tt | v |
| c | < 0 |
| - |
| rowspan=3 | tt | 1=Traits::compare(data(), v.data(), spar | rlen) == 0 |
| tt | size() < v.size() |
| tt | this is ''less'' than tt | v |
| c | < 0 |
| - |
| tt | 1=size() == v.size() |
| tt | this is ''equal'' to tt | v |
| c | 0 |
| - |
| tt | size() > v.size() |
| tt | this is ''greater'' than tt | v |
| c | > 0 |
| - |
| colspan=2 style="text-align:left;" | tt | Traits::compare(data(), v.data(), spar | rlen) > 0 |
| tt | this is ''greater'' than tt | v |
| c | > 0 |

2. Equivalent to `substr(pos1, count1).compare(v)`.
3. Equivalent to `substr(pos1, count1).compare(v.substr(pos2, count2))`.
4. Equivalent to `compare(basic_string_view(s))`.
5. Equivalent to `substr(pos1, count1).compare(basic_string_view(s))`.
6. Equivalent to `substr(pos1, count1).compare(basic_string_view(s, count2))`.

## Parameters


### Parameters

- `v` - view to compare
- `s` - pointer to the character string to compare to
- `count1` - number of characters of this view to compare
- `pos1` - position of the first character in this view to compare
- `count2` - number of characters of the given view to compare
- `pos2` - position of the first character of the given view to compare

## Return value

Negative value if this view is less than the other character sequence, zero if the both character sequences are equal, positive value if this view is greater than the other character sequence.

## Complexity

1) Linear in the number of characters compared.

## Example


## See also


| cpp/string/basic_string/dsc {{SUBPAGENAMEE | (see dedicated page) |
| cpp/string/basic_string_view/dsc operator_cmp | (see dedicated page) |

