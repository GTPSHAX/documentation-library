---
title: std::atomic_ref::operator=
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_ref/operator=
---


```cpp
dcla|num=1|constexpr=c++26|1=
value_type operator=( value_type desired ) const noexcept;
dcl|num=2|1=
atomic_ref& operator=( const atomic_ref& ) = delete;
```

1. Equivalent to `store(desired); return desired;`. .
2. `atomic_ref` is not *CopyAssignable*.

## Parameters


### Parameters

- `desired` - value to assign

## Return value

As described above.

## Notes

Unlike most assignment operators, the assignment operator for `atomic_ref` does not return a reference to its left-hand argument. It returns a copy of the stored value instead.

## Defect reports


## See also


| cpp/atomic/atomic_ref/dsc constructor | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc store | (see dedicated page) |

