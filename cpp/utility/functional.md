---
title: Function objects
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional
---


# Function objects

A ''function object'' is any object for which the function call operator is defined.  C++ provides many built-in function objects as well as support for creation and manipulation of new function objects.

## Function invocation

rrev|since=c++11|
The exposition-only operation  is defined as follows:
Let type `Obj` be the unqualified type of `arg_0` (i.e., `std::remove_cv<std::remove_reference<decltype(arg_0)>::type>::type`) and `obj` be an object of type `Obj`.
* If `f` is a pointer to member function of class `C`, then  is equivalent to:
:* If `std::is_same<C, Obj>::value  is `true`
::* `(obj.*f)(arg_1, arg_2, ..., arg_N)` (invoke the member function on the object).
:* If `Obj` is a specialization of `std::reference_wrapper`
::* `(obj.get().*f)(arg_1, arg_2, ..., arg_N)` (invoke the member function on the specially referred object).
:* Otherwise
::* `((*obj).*f)(arg_1, arg_2, ..., arg_N)` (invoke the member function on the dereferenced object).
* Otherwise, if `1=N == 0` and `f` is a pointer to data member of class `C`, then  is equivalent to:
:* If `std::is_same<C, Obj>::value  is `true`
::* `obj.*mptr` (access the data member of the object).
:* If `Obj` is a specialization of `std::reference_wrapper`
::* `obj.get().*mptr` (access the data member of the specially referred object).
:* Otherwise
::* `(*obj).*mptr` (access the data member of the dereferenced object).
* Otherwise
:*  is equivalent to `f(arg_0, arg_1, arg_2, ..., arg_N)` (invoke the callable).
The exposition-only operation  is defined as follows:
* If `R` is (possibly cv-qualified) `void`
:* .
* Otherwise
:*  implicitly converted to `R`.
rrev|since=c++23|
Let type `Actual` be `decltype(``(f, arg_0, arg_1, arg_2, ..., arg_N))`
* If  is `true`
:*  is ill-formed.
`std::invoke`<sup>(since C++23)</sup>  and `std::invoke_r` can invoke any *Callable* object with given arguments according to the rules of <sup>(since C++23)</sup>  and .


| cpp/utility/functional/dsc invoke | (see dedicated page) |


## Function wrappers

These polymorphic wrapper classes provide support for storing arbitrary function objects.


| cpp/utility/functional/dsc function | (see dedicated page) |
| cpp/utility/functional/dsc move_only_function | (see dedicated page) |
| cpp/utility/functional/dsc copyable_function | (see dedicated page) |
| cpp/utility/functional/dsc function_ref | (see dedicated page) |
| cpp/utility/functional/dsc bad_function_call | (see dedicated page) |
| cpp/utility/functional/dsc mem_fn | (see dedicated page) |


## Identity

`std::identity` is the identity function object: it returns its argument unchanged.


| cpp/utility/functional/dsc identity | (see dedicated page) |


## Partial function application

`std::bind_front` and `std::bind` provide support for [Partial application|partial function application](https://en.wikipedia.org/wiki/Partial application|partial function application), i.e. binding arguments to functions to produce new functions.


| cpp/utility/functional/dsc bind_front | (see dedicated page) |
| cpp/utility/functional/dsc bind | (see dedicated page) |
| cpp/utility/functional/dsc is_bind_expression | (see dedicated page) |
| cpp/utility/functional/dsc is_placeholder | (see dedicated page) |
| std::placeholders | |
| cpp/utility/functional/dsc placeholders | (see dedicated page) |


## Negators

`std::not_fn` creates a function object that negates the result of the callable object passed to it.


| cpp/utility/functional/dsc not_fn | (see dedicated page) |


## Searchers

Searchers implementing several string searching algorithms are provided and can be used either directly or with `std::search`.


| cpp/utility/functional/dsc default_searcher | (see dedicated page) |
| cpp/utility/functional/dsc boyer_moore_searcher | (see dedicated page) |
| cpp/utility/functional/dsc boyer_moore_horspool_searcher | (see dedicated page) |


## Reference wrappers

Reference wrappers allow reference arguments to be stored in copyable function objects:


| cpp/utility/functional/dsc reference_wrapper | (see dedicated page) |
| cpp/utility/functional/dsc ref | (see dedicated page) |
| cpp/utility/functional/dsc unwrap_reference | (see dedicated page) |

rrev|since=c++14|

## Transparent function objects

<sup>(since C++20)</sup>  and  provide heterogeneous lookup<sup>(since C++23)</sup>  and erasure operations, but they are only enabled if the supplied function object type `T` is ''transparent'': the qualified identifier `T::is_transparent` is valid and denotes a type.
All transparent function object types in the standard library defines a nested type `is_transparent`. However, user-defined transparent function object types do not need to directly provide `is_transparent` as a nested type: it can be defined in a base class, as long as `T::is_transparent` satisfies the transparent requirement stated above.

## Operator function objects

C++ defines the following function objects that represent common arithmetic and logical operations.
rrev|since=c++14|
The `void` specializations deduce their parameter types and return types from their arguments, they are all transparent.


#### Arithmetic operations

| cpp/utility/functional/dsc plus | (see dedicated page) |
| cpp/utility/functional/dsc plus void | (see dedicated page) |
| cpp/utility/functional/dsc minus | (see dedicated page) |
| cpp/utility/functional/dsc minus void | (see dedicated page) |
| cpp/utility/functional/dsc multiplies | (see dedicated page) |
| cpp/utility/functional/dsc multiplies void | (see dedicated page) |
| cpp/utility/functional/dsc divides | (see dedicated page) |
| cpp/utility/functional/dsc divides void | (see dedicated page) |
| cpp/utility/functional/dsc modulus | (see dedicated page) |
| cpp/utility/functional/dsc modulus void | (see dedicated page) |
| cpp/utility/functional/dsc negate | (see dedicated page) |
| cpp/utility/functional/dsc negate void | (see dedicated page) |

#### Comparisons

| cpp/utility/functional/dsc equal_to | (see dedicated page) |
| cpp/utility/functional/dsc equal_to void | (see dedicated page) |
| cpp/utility/functional/dsc not_equal_to | (see dedicated page) |
| cpp/utility/functional/dsc not_equal_to void | (see dedicated page) |
| cpp/utility/functional/dsc greater | (see dedicated page) |
| cpp/utility/functional/dsc greater void | (see dedicated page) |
| cpp/utility/functional/dsc less | (see dedicated page) |
| cpp/utility/functional/dsc less void | (see dedicated page) |
| cpp/utility/functional/dsc greater_equal | (see dedicated page) |
| cpp/utility/functional/dsc greater_equal void | (see dedicated page) |
| cpp/utility/functional/dsc less_equal | (see dedicated page) |
| cpp/utility/functional/dsc less_equal void | (see dedicated page) |

#### Logical operations

| cpp/utility/functional/dsc logical_and | (see dedicated page) |
| cpp/utility/functional/dsc logical_and void | (see dedicated page) |
| cpp/utility/functional/dsc logical_or | (see dedicated page) |
| cpp/utility/functional/dsc logical_or void | (see dedicated page) |
| cpp/utility/functional/dsc logical_not | (see dedicated page) |
| cpp/utility/functional/dsc logical_not void | (see dedicated page) |

#### Bitwise operations

| cpp/utility/functional/dsc bit_and | (see dedicated page) |
| cpp/utility/functional/dsc bit_and void | (see dedicated page) |
| cpp/utility/functional/dsc bit_or | (see dedicated page) |
| cpp/utility/functional/dsc bit_or void | (see dedicated page) |
| cpp/utility/functional/dsc bit_xor | (see dedicated page) |
| cpp/utility/functional/dsc bit_xor void | (see dedicated page) |
| cpp/utility/functional/dsc bit_not | (see dedicated page) |
| cpp/utility/functional/dsc bit_not void | (see dedicated page) |

rrev|since=c++20|

## Constrained comparison function objects

The following comparison function objects are constrained.
* The equality operators (`ranges::equal_to` and `ranges::not_equal_to`) require the types of the arguments to satisfy .
* The relational operators (`ranges::less`, `ranges::greater`, `ranges::less_equal`, and `ranges::greater_equal`) require the types of the arguments to satisfy .
* The three-way comparison operator (`compare_three_way`) requires the type to model .
All these function objects are transparent.


| cpp/utility/functional/ranges/dsc equal_to | (see dedicated page) |
| cpp/utility/functional/ranges/dsc not_equal_to | (see dedicated page) |
| cpp/utility/functional/ranges/dsc less | (see dedicated page) |
| cpp/utility/functional/ranges/dsc greater | (see dedicated page) |
| cpp/utility/functional/ranges/dsc less_equal | (see dedicated page) |
| cpp/utility/functional/ranges/dsc greater_equal | (see dedicated page) |
| cpp/utility/compare/dsc compare_three_way | (see dedicated page) |

rrev|since=c++26|

## Helper items

Following exposition-only items are used for several components in the standard library but they are not part of the interface of the standard library.

```cpp
dcla|num=1|anchor=callable|expos=yes|1=
template< class Fn, class... Args >
concept /*callable*/ =
requires (Fn&& fn, Args&&... args) {
std::forward<Fn>(fn)(std::forward<Args>(args)...);
};
dcla|num=2|anchor=nothrow-callable|expos=yes|1=
template< class Fn, class... Args >
concept /*nothrow-callable*/ =
/*callable*/<Fn, Args...> &&
requires (Fn&& fn, Args&&... args) {
{ std::forward<Fn>(fn)(std::forward<Args>(args)...) } noexcept;
};
dcla|num=3|anchor=call-result-t|expos=yes|1=
template< class Fn, class... Args >
using /*call-result-t*/ = decltype(std::declval<Fn>()(std::declval<Args>()...));
dcla|num=4|anchor=decayed-typeof|expos=yes|1=
template< const auto& T >
using /*decayed-typeof*/ = decltype(auto(T));
```

rrev|until=c++20|

## Old binders and adaptors

Several utilities that provided early functional support are deprecated and removed:


#### Base

| cpp/utility/functional/dsc unary_function | (see dedicated page) |
| cpp/utility/functional/dsc binary_function | (see dedicated page) |

#### Binders

| cpp/utility/functional/dsc binder12 | (see dedicated page) |
| cpp/utility/functional/dsc bind12 | (see dedicated page) |

#### Function adaptors

| cpp/utility/functional/dsc pointer_to_unary_function | (see dedicated page) |
| cpp/utility/functional/dsc pointer_to_binary_function | (see dedicated page) |
| cpp/utility/functional/dsc ptr_fun | (see dedicated page) |
| cpp/utility/functional/dsc mem_fun_t | (see dedicated page) |
| cpp/utility/functional/dsc mem_fun | (see dedicated page) |
| cpp/utility/functional/dsc mem_fun_ref_t | (see dedicated page) |
| cpp/utility/functional/dsc mem_fun_ref | (see dedicated page) |
| cpp/utility/functional/dsc unary_negate | (see dedicated page) |
| cpp/utility/functional/dsc binary_negate | (see dedicated page) |
| cpp/utility/functional/dsc not1 | (see dedicated page) |
| cpp/utility/functional/dsc not2 | (see dedicated page) |


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-185 | C++98 | using function objects improved the program efficiency | removed the claim |
| lwg-660 | C++98 | function objects for bitwise operations are missing | added |
| lwg-2149 | C++98 | function objects taking one or two arguments were required to<br>provide nested types to denote the argument and result types | not required |

