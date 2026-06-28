---
title: std::enable_shared_from_this::weak_from_this
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/enable_shared_from_this/weak_from_this
---


```cpp
dcla|num=1|since=c++17|constexpr=c++26|
std::weak_ptr<T> weak_from_this() noexcept;
dcla|num=2|since=c++17|constexpr=c++26|
std::weak_ptr<const T> weak_from_this() const noexcept;
```

Returns a `std::weak_ptr` that tracks ownership of `*this` by all existing `std::shared_ptr` that refer to `*this`.

## Return value


## Notes


## Example

