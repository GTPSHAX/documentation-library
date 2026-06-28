---
title: std::ranges::views::join_with
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_with_view
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++23|
template< ranges::input_range V, ranges::forward_range Pattern >
requires ranges::view<V> &&
ranges::input_range<ranges::range_reference_t<V>> &&
ranges::view<Pattern> &&
/*concatable*/<ranges::range_reference_t<V>, Pattern>
class join_with_view :
ranges::view_interface<join_with_view<V, Pattern>>
dcl|num=2|since=c++23|1=
namespace views {
inline constexpr /* unspecified */ join_with = /* unspecified */;
}
dcl|since=c++23|1=
template< ranges::viewable_range R, class Pattern >
requires /* see below */
constexpr ranges::view auto join_with( R&& r, Pattern&& pattern );
dcl|since=c++23|1=
template< class Pattern >
constexpr /* range adaptor closure */ join_with( Pattern&& pattern );
```

1. A range adaptor that represents  consisting of the sequence obtained from flattening a view of ranges, with every element of the delimiter inserted in between elements of the view. The delimiter can be a single element or a view of elements.
@@ For the definition of `/*concatable*/`, see .
2. *RangeAdaptorObject*. The expression `views::join_with(e, f)` is expression-equivalent to `join_with_view(e, f)` for any suitable subexpressions `e` and `f`.
`join_with_view` models .
`join_with_view` models  when:
* `ranges::range_reference_t<V>` is a reference, and
* `V` and `ranges::range_reference_t<V>` each model .
`join_with_view` models  when:
* `ranges::range_reference_t<V>` is a reference,
* `V`, `ranges::range_reference_t<V>`, and `Pattern` each models , and
* `ranges::range_reference_t<V>` and `Pattern` each model .
`join_with_view` models  when:
* `ranges::range_reference_t<V>` is a reference, and
* `V` and `ranges::range_reference_t<V>` each model  and .

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/dsc constructor|join_with_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc base|join_with_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc begin|join_with_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|join_with_view | (see dedicated page) |


## 


## Nested classes


## Notes


### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_ranges_join_with` | 202202L | C++23 | `std::ranges::join_with_view` |


## Example


### Example

```cpp
#include <print>
#include <ranges>
#include <string_view>
#include <list>

int main()
{
    std::list<std::string_view> v{"_", "cpp", "lib", "ranges", "join", "with"};
    std::println("{:s}", v {{!
```

}
|output=
__cpp_lib_ranges_join_with

## Defect reports


## See also


| cpp/ranges/dsc join_view | (see dedicated page) |
| cpp/ranges/dsc concat_view | (see dedicated page) |

