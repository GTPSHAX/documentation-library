---
title: std::ranges::join_with_view::end
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_with_view/end
---


```cpp
dcl|num=1|since=c++23|
constexpr auto end();
dcl|num=2|since=c++23|
constexpr auto end() const
requires ranges::forward_range<const V> &&
ranges::forward_range<const Pattern> &&
std::is_reference_v<ranges::range_reference_t<const V>>> &&
ranges::input_range<ranges::range_reference_t<const V>> &&
/*concatable*/<ranges::range_reference_t<const V>,
const Pattern>;
```

Returns an `iterator` or a `sentinel` that compares equal to the past-the-end iterator of the `join_with_view`.
1. Returns a mutable iterator/sentinel or const iterator/sentinel.
* If all following conditions are satisfied, returns an iterator:
:* `V` models  and .
:*  is `true`.
:*  models  and .
* Otherwise, returns a sentinel.
2. Returns a const iterator/sentinel.
* If all following conditions are satisfied, returns an iterator:
:* `const V` models .
:* `ranges::range_reference_t<const V>` models  and .
* Otherwise, returns a sentinel.
@@ For the definition of `/*concatable*/`, see .

## Return value


| rowspan=2 | Overload |
| colspan=2 | Return value |
| - |
| Iterator |
| Sentinel |
| - |
| v | 1 |
| <span style="text-align: left;">box | rlpi | iteratorc/core | <lti | cpp/ranges#Helper concepts | simple-viewc/core | <V> &&<br>nbspt | 9lti | cpp/ranges#Helper concepts | simple-viewc/core | <Pattern>><br>nbspt | 4c/core | {*this, ranges::end(rlpsi | /#base_c/core | )}</span> |
| <span style="text-align: left;">box | rlpi | sentinelc/core | <lti | cpp/ranges#Helper concepts | simple-viewc/core | <V> &&<br>nbspt | 9lti | cpp/ranges#Helper concepts | simple-viewc/core | <Pattern>><br>nbspt | 4c/core | {*this}</span> |
| - |
| v | 2 |
| box | rlpi | iteratorc/core | <true>{*this, ranges::end(rlpsi | /#base_c/core | )} |
| box | rlpi | sentinelc/core | <true>{*this} |


## Example

