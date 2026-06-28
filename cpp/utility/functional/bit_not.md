---
title: std::bit_not
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/bit_not
---


```cpp
**Header:** `<`functional`>`
dcl|since=c++14|1=
template< class T = void >
struct bit_not;
```

Function object for performing bitwise NOT. Effectively calls `operator~` on type `T`.

## Specializations

The standard library provides a specialization of `std::bit_not` when `T` is not specified, which leaves the parameter types and return type to be deduced.


| cpp/utility/functional/dsc bit_not_void | (see dedicated page) |


## Member functions

member|operator()|2=

```cpp
dcl|since=c++14|
constexpr T operator()( const T& arg ) const;
```

Returns the result of bitwise NOT of `arg`.

## Parameters


### Parameters

- `arg` - value to compute bitwise NOT of

## Return value

The result of `~arg`.

## Possible implementation

eq fun|1=
constexpr T operator()(const T& arg) const
{
return ~arg;
}

## Notes

Although `std::bit_not` is added via post-C++11 proposal `N3421`, it is treated as a part of the resolution for  (except for its transparent specialization `std::bit_not<>`) by common implementations, and thus available in their C++98/03 mode.
