---
title: std::ranges::chunk_by_view::chunk_by_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_by_view/chunk_by_view
---


```cpp
dcl|num=1|since=c++23|1=
chunk_by_view()
requires std::default_initializable<V> &&
std::default_initializable<Pred>
= default;
dcl|num=2|since=c++23|1=
constexpr explicit chunk_by_view( V base, Pred pred );
```

Constructs a `chunk_by_view`.
1. Default constructor. Value-initializes the underlying data members via their respective default member initializers:
* the view `''base_''` via `1= = V()`,
* the binary predicate `''pred_''` via `1= = Pred()`.
2. Move constructs the underlying data members:
* the view `''base_''` with `std::move(base)`,
* the binary predicate `''pred_''` with `std::move(pred)`.

## Parameters


### Parameters

- `base` - the view to split
- `pred` - the function object (a binary predicate) used as a splitting criteria

## Example

