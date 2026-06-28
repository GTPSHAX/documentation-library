---
title: std::pointer_to_binary_function
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/pointer_to_binary_function
---

ddcl|deprecated=c++11|until=c++17|
template<
class Arg1,
class Arg2,
class Result
> class pointer_to_binary_function : public std::binary_function<Arg1, Arg2, Result>;
`std::pointer_to_binary_function` is a function object that acts as a wrapper around a binary function.

## Member functions

member|pointer_to_binary_function|2=
ddcl|1=
explicit pointer_to_binary_function( Result (*f)(Arg1,Arg2) );
Constructs a `pointer_to_binary_function` function object with the stored function `f`.

## Parameters


### Parameters

- `f` - pointer to a function to store
member|operator()|2=
ddcl|1=
Result operator()( Arg1 x1, Arg2 x2 ) const;
Calls the stored function.

## Parameters


### Parameters

- `x1, x2` - arguments to pass to the function

## Return value

The value returned by the called function.

## See also


| cpp/utility/functional/dsc pointer_to_unary_function | (see dedicated page) |
| cpp/utility/functional/dsc ptr_fun | (see dedicated page) |

