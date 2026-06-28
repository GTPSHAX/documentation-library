---
title: std::ranges::subrange::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/subrange/begin
---


```cpp
dcl|num=1|since=c++20|
constexpr I begin() const requires std::copyable<I>;
dcl|num=2|since=c++20|
constexpr I begin() requires (!std::copyable<I>);
```

Obtains the iterator to the beginning of the `subrange`.

## Return value

1. .
2. .

## Example

