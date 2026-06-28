---
title: std::reference_wrapper::reference_wrapper
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/reference_wrapper/reference_wrapper
---


```cpp
|
template< class U >
reference_wrapper( U&& x ) noexcept(/*see below*/) ;
|
reference_wrapper( const reference_wrapper& other ) noexcept;
```

Constructs a new reference wrapper.
1. Converts `x` to `T&` as if by `1=T& t = std::forward<U>(x);`, then stores a reference to `t`. , where `FUN` names the set of imaginary functions

```cpp
void FUN(T&) noexcept;
void FUN(T&&) = delete;
```

2. Copy constructor. Stores a reference to `other.get()`.

## Parameters


### Parameters

- `x` - an object to wrap
- `other` - another reference wrapper

## Exceptions

1.  where `FUN` is the set of imaginary functions described in the description above.

## Example


## Defect reports

