---
title: operators (std::pair)
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/pair/operator_cmp
---


# 1=operator==,!=,<,<=,>,>=,<=><small>(std::pair)</small>


```cpp
**Header:** `<`utility`>`
dcl rev multi|num=1
|until1=c++14|dcl1=
template< class T1, class T2, class U1, class U2 >
bool operator==( const std::pair<T1, T2>& lhs, const std::pair<U1, U2>& rhs );
|dcl2=
template< class T1, class T2, class U1, class U2 >
constexpr bool operator==( const std::pair<T1, T2>& lhs,
const std::pair<U1, U2>& rhs );
dcl rev multi|num=2
|until1=c++14|dcl1=
template< class T1, class T2, class U1, class U2 >
bool operator!=( const std::pair<T1, T2>& lhs, const std::pair<U1, U2>& rhs );
|until2=c++20|dcl2=
template< class T1, class T2, class U1, class U2 >
constexpr bool operator!=( const std::pair<T1, T2>& lhs,
const std::pair<U1, U2>& rhs );
dcl rev multi|num=3
|until1=c++14|dcl1=
template< class T1, class T2, class U1, class U2 >
bool operator<( const std::pair<T1, T2>& lhs, const std::pair<U1, U2>& rhs );
|until2=c++20|dcl2=
template< class T1, class T2, class U1, class U2 >
constexpr bool operator<( const std::pair<T1, T2>& lhs,
const std::pair<U1, U2>& rhs );
dcl rev multi|num=4
|until1=c++14|dcl1=
template< class T1, class T2, class U1, class U2 >
bool operator<=( const std::pair<T1, T2>& lhs, const std::pair<U1, U2>& rhs );
|until2=c++20|dcl2=
template< class T1, class T2, class U1, class U2 >
constexpr bool operator<=( const std::pair<T1, T2>& lhs,
const std::pair<U1, U2>& rhs );
dcl rev multi|num=5
|until1=c++14|dcl1=
template< class T1, class T2, class U1, class U2 >
bool operator>( const std::pair<T1, T2>& lhs, const std::pair<U1, U2>& rhs );
|until2=c++20|dcl2=
template< class T1, class T2, class U1, class U2 >
constexpr bool operator>( const std::pair<T1, T2>& lhs,
const std::pair<U1, U2>& rhs );
dcl rev multi|num=6
|until1=c++14|dcl1=
template< class T1, class T2, class U1, class U2 >
bool operator>=( const std::pair<T1, T2>& lhs, const std::pair<U1, U2>& rhs );
|until2=c++20|dcl2=
template< class T1, class T2, class U1, class U2 >
constexpr bool operator>=( const std::pair<T1, T2>& lhs,
const std::pair<U1, U2>& rhs );
dcl|num=7|since=c++20|1=
template< class T1, class T2, class U1, class U2 >
constexpr std::common_comparison_category_t<synth-three-way-result<T1, U1>,
synth-three-way-result<T2, U2>>
operator<=>( const std::pair<T1, T2>& lhs, const std::pair<U1, U2>& rhs );
```

@1,2@ Tests if both elements of `lhs` and `rhs` are equal, that is, compares `lhs.first` with `rhs.first` and `lhs.second` with `rhs.second`.<br /><!--
-->rrev multi|rev1=
The behavior is undefined if the type and value category of either `1=lhs.first == rhs.first` or `1=lhs.second == rhs.second` do not meet the *BooleanTestable* requirements.
|since2=c++26|rev2=
.
@3-6@ Compares `lhs` and `rhs` lexicographically by `operator<`, that is, compares the first elements and only if they are equivalent, compares the second elements. The behavior is undefined if the type and value category of any of `1=lhs.first < rhs.first`, `1=rhs.first < lhs.first`, or `1=lhs.second < rhs.second` do not meet the *BooleanTestable* requirements.
7. Compares `lhs` and `rhs` lexicographically by , that is, compares the first elements and only if they are equivalent, compares the second elements.  is the return type of .
rrev|since=c++20|

## Parameters


### Parameters

- `lhs, rhs` - pairs to compare

## Return value

1. `true` if both `1=lhs.first == rhs.first` and `1=lhs.second == rhs.second`, otherwise `false`.
2. `1=!(lhs == rhs)`
3. If `lhs.first < rhs.first`, returns `true`. Otherwise, if `rhs.first < lhs.first`, returns `false`. Otherwise, if `lhs.second < rhs.second`, returns `true`. Otherwise, returns `false`.
4. `!(rhs < lhs)`
5. `rhs < lhs`
6. `!(lhs < rhs)`
7.  if it is not equal to `0`, otherwise .

## Notes

rrev multi|rev1=
The relational operators are defined in terms of each element's `operator<`.
|since2=c++20|rev2=
The relational operators are defined in terms of , which uses `1=operator<=>` if possible, or `operator<` otherwise.
Notably, if an element type does not itself provide `1=operator<=>`, but is implicitly convertible to a three-way comparable type, that conversion will be used instead of `operator<`.

## Example


### Example

```cpp
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

int main()
{
    std::vector<std::pair<int, std::string>> v = {<!---->{2, "baz"}, {2, "bar"}, {1, "foo"}<!---->};
    std::sort(v.begin(), v.end());

    for (auto p : v)
        std::cout << '{' << p.first << ", " << std::quoted(p.second) << "}\n";
}
```


**Output:**
```
{1, "foo"}
{2, "bar"}
{2, "baz"}
```


## Defect reports


## See also


| cpp/utility/tuple/dsc operator_cmp | (see dedicated page) |

