---
title: std::bind1st
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/bind12
---


```cpp
**Header:** `<`functional`>`
dcl|deprecated=c++11|until=c++17|num=1|
template< class F, class T >
std::binder1st<F> bind1st( const F& f, const T& x );
dcl|deprecated=c++11|until=c++17|num=2|
template< class F, class T >
std::binder2nd<F> bind2nd( const F& f, const T& x );
```

Binds a given argument `x` to a first or second parameter of the given binary function object `f`. That is, stores `x` within the resulting wrapper, which, if called, passes `x` as the first or the second parameter of `f`.
1. Binds the first argument of `f` to `x`. Effectively calls `std::binder1st<F>(f, typename F::first_argument_type(x))`.
2. Binds the second argument of `f` to `x`. Effectively calls `std::binder2nd<F>(f, typename F::second_argument_type(x))`.

## Parameters


### Parameters

- `f` - pointer to a function to bind an argument to
- `x` - argument to bind to `f`

## Return value

A function object wrapping `f` and `x`.

## Example


### Example


**Output:**
```
<nowiki/>
  0° = 0.000000 rad
 30° = 0.523599 rad
 45° = 0.785398 rad
 60° = 1.047198 rad
 90° = 1.570796 rad
180° = 3.141593 rad
```


## See also


| cpp/utility/functional/dsc binder12 | (see dedicated page) |
| cpp/utility/functional/dsc bind_front | (see dedicated page) |

