---
title: std::ranges::chunk_by_view::pred
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_by_view/pred
---

ddcl|since=c++23|
constexpr const Pred& pred() const;
Returns a reference to the contained `Pred` object. Equivalent to .
The behavior is undefined if  does not contain a value.

## Parameters

(none)

## Return value

A reference to the contained `Pred` object.

## Example


### Example

```cpp
#include <cassert>
#include <concepts>
#include <functional>
#include <initializer_list>
#include <ranges>

int main()
{
    const auto v = {1, 1, 2, 2, 1, 1, 1};
    auto chunks = v {{!
```

auto pred = chunks.pred();
static_assert(std::same_as<decltype(pred), std::equal_to<>>);
assert(pred(v.begin()[0], 1));
}
