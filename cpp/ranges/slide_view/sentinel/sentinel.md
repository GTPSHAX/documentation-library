---
title: std::ranges::slide_view::sentinel::sentinel
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/slide_view/sentinel/sentinel
---


```cpp
dcl|num=1|since=c++23|1=
/*sentinel*/() = default;
|1=
private:
constexpr /*sentinel*/( ranges::sentinel_t<V> end );
```

Constructs a `sentinel`.
1. Default constructor. Value-initializes the underlying sentinel  with `ranges::sentinel_t<V>()`.
2. A private constructor which is used by `slide_view::end`. This constructor is not accessible to users. Initializes  with `end`.

## Parameters


### Parameters

- `end` - a sentinel

## Example

