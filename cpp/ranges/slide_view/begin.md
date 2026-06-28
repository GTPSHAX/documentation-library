---
title: std::ranges::slide_view::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/slide_view/begin
---


```cpp
dcla|num=1|since=c++23|
constexpr auto begin()
requires (!(/*simple-view*/<V> && /*slide-caches-nothing*/<const V>));
dcla|num=2|since=c++23|
constexpr auto begin() const
requires /*slide-caches-nothing*/<const V>;
```

Returns an iterator to the first element of the `slide_view`.
1. If `V` models , equivalent to
@@box|
`return``<false>(ranges::begin(``),`<br><!--
-->`ranges::next(ranges::begin(``),``- 1, ranges::end(``)),`<br><!--
-->`);`
@@ Otherwise, equivalent to .
@@ If `V` models  this function caches the result within the  for use on subsequent calls. This is necessary to provide the amortized constant-time complexity required by the .
2. Equivalent to .

## Parameters

(none)

## Return value

An `iterator` to the first element of `slide_view`, which points to the -sized subrange of the underlying view type: `V` for overload  or `const V` for overload .

## Example


### Example

```cpp
#include <iostream>
#include <ranges>
#include <string_view>
using namespace std::literals;

int main()
{
    static constexpr auto source = {"∀x"sv, "∃y"sv, "ε"sv, "δ"sv};
    auto view{std::ranges::slide_view(source, 2)};
    const auto subrange{*(view.begin())};
    for (std::string_view const s : subrange)
        std::cout << s << ' ';
    std::cout << '\n';
}
```


**Output:**
```
∀x ∃y
```


## See also


| cpp/ranges/adaptor/dsc end|slide_view | (see dedicated page) |
| cpp/ranges/adaptor/sentinel/dsc operator cmp|slide_view | (see dedicated page) |

