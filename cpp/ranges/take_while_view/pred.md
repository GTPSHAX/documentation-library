---
title: std::ranges::take_while_view::pred
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/take_while_view/pred
---


```cpp
dcl|since=c++20|1=
constexpr const Pred& pred() const;
```

Returns a reference to the stored predicate .
If `*this` does not store a predicate (e.g. an exception is thrown on the assignment to `*this`, which copy-constructs or move-constructs a `Pred`), the behavior is undefined.

## Parameters

(none)

## Return value

A reference to the stored predicate.

## Example


### Example

```cpp
#include <ranges>

int main()
{
    static constexpr int a[]{1, 2, 3, 4, 5};
    constexpr auto v = a {{!
```

const auto pred = v.pred();
static_assert(pred(3));
}

## See also


| cpp/ranges/adaptor/dsc base|take_while_view | (see dedicated page) |

