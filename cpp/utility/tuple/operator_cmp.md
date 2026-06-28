---
title: operators (std::tuple)
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/tuple/operator_cmp
---


# 1=operator==,!=,<,<=,>,>=,<=>petty|(std::tuple)


```cpp
**Header:** `<`tuple`>`
dcla|num=1|since=c++11|constexpr=c++14|1=
template< class... TTypes, class... UTypes >
bool operator==( const std::tuple<TTypes...>& lhs,
const std::tuple<UTypes...>& rhs );
dcla|num=2|since=c++11|constexpr=c++14|until=c++20|1=
template< class... TTypes, class... UTypes >
bool operator!=( const std::tuple<TTypes...>& lhs,
const std::tuple<UTypes...>& rhs );
dcla|num=3|since=c++11|constexpr=c++14|until=c++20|1=
template< class... TTypes, class... UTypes >
bool operator<( const std::tuple<TTypes...>& lhs,
const std::tuple<UTypes...>& rhs );
dcla|num=4|since=c++11|constexpr=c++14|until=c++20|1=
template< class... TTypes, class... UTypes >
bool operator<=( const std::tuple<TTypes...>& lhs,
const std::tuple<UTypes...>& rhs );
dcla|num=5|since=c++11|constexpr=c++14|until=c++20|1=
template< class... TTypes, class... UTypes >
bool operator>( const std::tuple<TTypes...>& lhs,
const std::tuple<UTypes...>& rhs );
dcla|num=6|since=c++11|constexpr=c++14|until=c++20|1=
template< class... TTypes, class... UTypes >
bool operator>=( const std::tuple<TTypes...>& lhs,
const std::tuple<UTypes...>& rhs );
dcl|num=7|since=c++20|1=
template< class... TTypes, class... UTypes >
constexpr std::common_comparison_category_t<
synth-three-way-result<TTypes, Elems>...>
operator<=>( const std::tuple<TTypes...>& lhs,
const std::tuple<UTypes...>& rhs );
dcl|num=8|since=c++23|1=
template< class... TTypes, tuple-like UTuple >
constexpr bool operator==( const tuple<TTypes...>& lhs, const UTuple& rhs );
dcl|num=9|since=c++23|1=
template< class... TTypes, tuple-like UTuple >
constexpr std::common_comparison_category_t<
synth-three-way-result<TTypes, /* Elems */>...>
operator<=>( const tuple<TTypes...>& lhs, const UTuple& rhs );
```

@1,2@ Compares every element of the tuple `lhs` with the corresponding element of the tuple `rhs` by `1=operator==`.
:@1@ Returns `true` if all pairs of corresponding elements are equal.
:@2@ Returns `1=!(lhs == rhs)`.
rrev multi|rev1=
@@ If `sizeof...(TTypes)` does not equal `sizeof...(UTypes)`, or `1=std::get<i>(lhs) == std::get<i>(rhs)` is not a valid expression for any `i` in [0, sizeof...(Types)), the program is ill-formed.
@@ If the type and value category of `1=std::get<i>(lhs) == std::get<i>(rhs)` do not meet the *BooleanTestable* requirements for any `i` in [0, sizeof...(Types)), the behavior is undefined.
|since2=c++26|rev2=
@@ .
@3-6@ Compares `lhs` and `rhs` lexicographically by `operator<`, that is, compares the first elements, if they are equivalent, compares the second elements, if those are equivalent, compares the third elements, and so on.
:@3@ For empty tuples, returns `false`. For non-empty tuples, the effect is equivalent to<br>c|
if (std::get<0>(lhs) < std::get<0>(rhs)) return true;
if (std::get<0>(rhs) < std::get<0>(lhs)) return false;
if (std::get<1>(lhs) < std::get<1>(rhs)) return true;
if (std::get<1>(rhs) < std::get<1>(lhs)) return false;
...
return std::get<N - 1>(lhs) < std::get<N - 1>(rhs);
:@4@ Returns `!(rhs < lhs)`.
:@5@ Returns `rhs < lhs`.
:@6@ Returns `!(lhs < rhs)`.
@@ If `sizeof...(TTypes)` does not equal `sizeof...(UTypes)`, or any of the comparison expression shown in the equivalent-to statements is not a valid expression, the program is ill-formed.
@@ If the type and value category of any of the comparison expression shown in the equivalent-to statements do not meet the *BooleanTestable* requirements, the behavior is undefined.
7. Compares `lhs` and `rhs` lexicographically by , that is, compares the first elements, if they are equivalent, compares the second elements, if those are equivalent, compares the third elements, and so on.
* For empty tuples, returns `cpp/utility/compare/strong_ordering|std::strong_ordering::equal`.
* For non-empty tuples, the effect is equivalent to
:@@ box|
`1=if (auto c =``1=(std::get<0>(lhs), std::get<0>(rhs)); c != 0) return c;`<br>
`1=if (auto c =``1=(std::get<1>(lhs), std::get<1>(rhs)); c != 0) return c;`<br>
`...`<br>
`return``(std::get<N - 1>(lhs), std::get<N - 1>(rhs));`
8. Same as , except that `rhs` is a  object, and the number of elements of `rhs` is determined by `std::tuple_size_v<UTuple>` instead. This overload can only be found via argument-dependent lookup.
9. Same as , except that `rhs` is a  object. `/* Elems */` denotes the pack of types `std::tuple_element_t<i, UTuple>` for each `i` in [0, std::tuple_size_v<UTuple>) in increasing order. This overload can only be found via argument-dependent lookup.
All comparison operators are short-circuited; they do not access tuple elements beyond what is necessary to determine the result of the comparison.
rrev|since=c++20|

## Parameters


### Parameters

- `lhs, rhs` - tuples to compare

## Return value

@1,8@ `true` if `1=std::get<i>(lhs) == std::get<i>(rhs)` for all `i` in [0, sizeof...(Types)), otherwise `false`. For two empty tuples returns `true`.
2. `1=!(lhs == rhs)`
3. `true` if the first non-equivalent element in `lhs` is less than the one in `rhs`, `false` if the first non-equivalent element in `rhs` is less than the one in `lhs` or there is no non-equivalent element. For two empty tuples, returns `false`.
4. `!(rhs < lhs)`
5. `rhs < lhs`
6. `!(lhs < rhs)`
@7,9@ The relation between the first pair of non-equivalent elements if there is any, `cpp/utility/compare/strong_ordering|std::strong_ordering::equal` otherwise. For two empty tuples, returns `cpp/utility/compare/strong_ordering|std::strong_ordering::equal`.

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
#include <iostream>
#include <tuple>
#include <vector>

int main()
{
    std::vector<std::tuple<int, std::string, float>> v
    {
        {2, "baz", -0.1},
        {2, "bar", 3.14},
        {1, "foo", 10.1},
        {2, "baz", -1.1},
    };
    std::sort(v.begin(), v.end());

    for (const auto& p: v)
        std::cout << "{ " << get<0>(p)
                  << ", " << get<1>(p)
                  << ", " << get<2>(p)
                  << " }\n";
}
```


**Output:**
```
{ 1, foo, 10.1 }
{ 2, bar, 3.14 }
{ 2, baz, -1.1 }
{ 2, baz, -0.1 }
```


## Defect reports


## See also


| cpp/utility/pair/dsc operator cmp | (see dedicated page) |

