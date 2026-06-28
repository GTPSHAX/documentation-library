---
title: std::ranges::dangling
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/dangling
---


```cpp
dcl | since = c++20 |
struct dangling;
```

`dangling` is a placeholder type and an empty class type, used together with the template aliases `cpp/ranges/borrowed_iterator_t|ranges::borrowed_iterator_t` and `cpp/ranges/borrowed_iterator_t|ranges::borrowed_subrange_t`.
When some constrained algorithms that usually return an iterator or a subrange of a  take a particular rvalue `range` argument that does not model , `dangling` will be returned instead to avoid returning potentially dangling results.

## Member functions

member | dangling | 2=

```cpp
dcl | num=1 |1=
constexpr dangling() noexcept = default;
dcl | num=2 |
template<class... Args>
constexpr dangling(Args&&...) noexcept { }
```

1. `dangling` is trivially default constructible.
2. `dangling` can be constructed from arguments of arbitrary number and arbitrary non-void type. The construction does not have any side-effect itself.
In other words, after replacing the type (e.g. an iterator type) in a well-formed non-aggregate initialization with `dangling`, the resulting initialization is also well-formed.

## Example


## See also

