---
title: std::ranges::chunk_view::inner-iterator::inner-iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/inner_iterator/inner_iterator
---


```cpp
dcl|num=1|since=c++23|1=
/*inner-iterator*/( /*inner-iterator*/&& other ) = default;
|1=
private:
constexpr explicit /*inner-iterator*/( chunk_view& parent );
```

Construct an iterator.
1. A move constructor which move-initializes the underlying pointer  with .
2. A private constructor which is used by `cpp/ranges/chunk_view/begin|chunk_view::begin`. This constructor is not accessible to users. Initializes  with `std::addressof(parent)`.

## Parameters


### Parameters

- `other` - an `iterator`
- `parent` - the enclosing `ranges::chunk_view` object

## Example


## See also

