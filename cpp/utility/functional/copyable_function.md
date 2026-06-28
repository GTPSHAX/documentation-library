---
title: std::copyable_function
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/copyable_function
---


```cpp
**Header:** `<`functional`>`
dcl|num=1|since=c++26|
template< class... >
class copyable_function; // not defined
dcl|num=2|since=c++26|
template< class R, class... Args >
class copyable_function<R(Args...)>;
template< class R, class... Args >
class copyable_function<R(Args...) noexcept>;
template< class R, class... Args >
class copyable_function<R(Args...) &>;
template< class R, class... Args >
class copyable_function<R(Args...) & noexcept>;
template< class R, class... Args >
class copyable_function<R(Args...) &&>;
template< class R, class... Args >
class copyable_function<R(Args...) && noexcept>;
template< class R, class... Args >
class copyable_function<R(Args...) const>;
template< class R, class... Args >
class copyable_function<R(Args...) const noexcept>;
template< class R, class... Args >
class copyable_function<R(Args...) const &>;
template< class R, class... Args >
class copyable_function<R(Args...) const & noexcept>;
template< class R, class... Args >
class copyable_function<R(Args...) const &&>;
template< class R, class... Args >
class copyable_function<R(Args...) const && noexcept>;
```

Class template `std::copyable_function` is a general-purpose polymorphic function wrapper. `std::copyable_function` objects can store and invoke any *CopyConstructible* *Callable* ''target'' — functions, lambda expressions, bind expressions, or other function objects, as well as pointers to member functions and pointers to member objects.
The stored callable object is called the ''target'' of `std::copyable_function`. If a `std::copyable_function` contains no target, it is called ''empty''. Unlike `std::function`, invoking an ''empty'' `std::copyable_function` results in undefined behavior.
`std::copyable_function`s supports every possible combination of cv-qualifiers (not including `volatile`), ref-qualifiers, and noexcept-specifiers  provided in its template parameter. These qualifiers and specifier (if any) are added to its .
`std::copyable_function` satisfies the requirements of *CopyConstructible* and *CopyAssignable*.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/utility/functional/copyable_function/dsc constructor | (see dedicated page) |
| cpp/utility/functional/copyable_function/dsc destructor | (see dedicated page) |
| cpp/utility/functional/copyable_function/dsc operator{{= | (see dedicated page) |
| cpp/utility/functional/copyable_function/dsc swap | (see dedicated page) |
| cpp/utility/functional/copyable_function/dsc operator_bool | (see dedicated page) |
| cpp/utility/functional/copyable_function/dsc operator() | (see dedicated page) |


## Non-member functions


| cpp/utility/functional/copyable_function/dsc swap2 | (see dedicated page) |
| cpp/utility/functional/copyable_function/dsc operator{{== | (see dedicated page) |


## Notes

Implementations may store a callable object of small size within the `std::copyable_function` object. Such small object optimization is effectively required for function pointers and `std::reference_wrapper` specializations, and can only be applied to types `T` for which `std::is_nothrow_move_constructible_v<T>` is `true`.

## Example

