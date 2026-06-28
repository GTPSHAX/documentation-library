---
title: std::pointer_to_unary_function
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/pointer_to_unary_function
---

ddcl|deprecated=c++11|until=c++17|
template<
class Arg,
class Result
> class pointer_to_unary_function : public std::unary_function<Arg, Result>;
`std::pointer_to_unary_function` is a function object that acts as a wrapper around a unary function.

## Member functions

member|pointer_to_unary_function|2=
ddcl|1=
explicit pointer_to_unary_function( Result (*f)(Arg) );
Constructs a `pointer_to_unary_function` function object with the stored function `f`.

## Parameters


### Parameters

- `f` - pointer to a function to store
member|operator()|2=
ddcl|1=
Result operator()( Arg x ) const;
Calls the stored function.

## Parameters


### Parameters

- `x` - argument to pass to the function

## Return value

The value returned by the called function.

## See also


| cpp/utility/functional/dsc pointer_to_binary_function | (see dedicated page) |
| cpp/utility/functional/dsc ptr_fun | (see dedicated page) |

