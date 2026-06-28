---
title: std::ranges::chunk_view::outer-iterator::outer-iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/outer_iterator/outer_iterator
---


```cpp
dcl|num=1|since=c++23|1=
/*outer-iterator*/( /*outer-iterator*/&& other ) = default;
|1=
private:
constexpr explicit /*outer-iterator*/( chunk_view& parent );
```

Construct an iterator.
1. Move constructor. Move-initializes the underlying pointer  with .
2. A private constructor which is used by `cpp/ranges/chunk_view/begin|chunk_view::begin`. This constructor is not accessible to users. Initializes  with `std::addressof(parent)`.

## Parameters


### Parameters

- `other` - an `iterator`
- `parent` - the enclosing `ranges::chunk_view` object

## Example


## See also

