---
title: std::greater
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/greater
---


```cpp
**Header:** `<`functional`>`
dcl rev multi
|dcl1=
template< class T >
struct greater;
|since2=c++14|dcl2=
template< class T = void >
struct greater;
```

Function object for performing comparisons. The main template invokes `operator>` on type `T`.

## Specializations


| cpp/utility/functional/dsc greater_void | (see dedicated page) |


## Member functions

member|operator()|2=

```cpp
dcla|constexpr=c++14|1=
bool operator()( const T& lhs, const T& rhs ) const;
```

Checks whether `lhs` is ''greater'' than `rhs`.

## Parameters


### Parameters

- `lhs, rhs` - values to compare

## Return value

`lhs > rhs`.
If `T` is a pointer type, the result is consistent with the implementation-defined strict total order over pointers.

## Possible implementation

eq fun|1=
constexpr bool operator()(const T& lhs, const T& rhs) const
{
return lhs > rhs; // assumes that the implementation handles pointer total order
}

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2562 | C++98 | the pointer total order might be inconsistent | guaranteed to be consistent |


## See also


| cpp/utility/functional/dsc less | (see dedicated page) |
| cpp/utility/functional/ranges/dsc {{SUBPAGENAMEE | (see dedicated page) |

