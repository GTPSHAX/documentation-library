---
title: std::ranges::zip_transform_view::zip_transform_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_transform_view/zip_transform_view
---


```cpp
dcl | num=1 | since=c++23 |1=
zip_transform_view() = default;
dcl | num=2 | since=c++23 |1=
constexpr zip_transform_view( F fun, Views... views );
```

1. Default constructor. Value-initializes the stored invocable object and all adapted  objects.<br>
The default constructor is deleted if
* `F` does not satisfy , or
* `std::is_default_constructible_v` is `false` for at least one type in `Views...`.
2. Move constructs the stored invocable object from `fun` and every adapted  object from the corresponding view in `views...`.

## Parameters


### Parameters


## Example

