---
title: std::expected::emplace
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/expected/emplace
---


```cpp
dcl|num=1|since=c++23|
template< class... Args >
constexpr T& emplace( Args&&... args ) noexcept;
dcl|num=2|since=c++23|
template< class U, class... Args >
constexpr T& emplace( std::initializer_list<U> il, Args&&... args ) noexcept;
dcl|num=3|since=c++23|
constexpr void emplace() noexcept;
```

Constructs an expected value in-place. After the call,  returns true.
1. Destroys the contained value, then direct-initializes the expected value contained in `*this` with `std::forward<Args>(args)...`.
@@ .
2. Destroys the contained value, then direct-initializes the expected value contained in `*this` with `il` and `std::forward<Args>(args)...`.
@@ .
3. If `*this` contains an unexpected value, destroys that value.

## Parameters


### Parameters

- `args` - the arguments to pass to the constructor
- `il` - the initializer list to pass to the constructor

## Return value

1.
2.

## Notes

If the construction of `T` is potentially-throwing, `1=operator=` can be used instead.

## Example

