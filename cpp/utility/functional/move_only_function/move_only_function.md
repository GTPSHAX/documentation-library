---
title: std::move_only_function::move_only_function
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/move_only_function/move_only_function
---


```cpp
dcl|num=1|since=c++23|
move_only_function() noexcept;
dcl|num=2|since=c++23|
move_only_function( std::nullptr_t ) noexcept;
dcl|num=3|since=c++23|
move_only_function( move_only_function&& other ) noexcept;
dcl|num=4|since=c++23|1=
move_only_function( const move_only_function& ) = delete;
dcl|num=5|since=c++23|
template< class F >
move_only_function( F&& f );
dcl|num=6|since=c++23|
template< class T, class... CArgs >
explicit move_only_function( std::in_place_type_t<T>, CArgs&&... args );
dcl|num=7|since=c++23|
template< class T, class U, class... CArgs >
explicit move_only_function( std::in_place_type_t<T>,
std::initializer_list<U> il, CArgs&&... args );
```

Creates a new `std::move_only_function`.
@1,2@ Default constructor and the constructor taking `nullptr` construct an empty `std::move_only_function`.
3. Move constructor constructs a `std::move_only_function` whose target is that of `other`. `other` is in a valid but unspecified state after move construction.
4. Copy constructor is deleted. `std::move_only_function` does not satisfy *CopyConstructible*.
5. Let `VT` be `std::decay_t<F>`. If `f` is a null function pointer, a null pointer to member value, or an empty `std::move_only_function` (may be any other specialization), then constructs an empty `std::move_only_function`. Otherwise, constructs a `std::move_only_function` whose target is of type `VT` and direct-non-list-initialized with `std::forward<F>(f)`.
* .
* The program is ill-formed if `std::is_constructible_v<VT, F>` is not `true`.
6. Let `VT` be `std::decay_t<T>`. Constructs a `std::move_only_function` whose target is of type `VT` and direct-non-list-initialized with `std::forward<CArgs>(args)...`.
* .
* The program is ill-formed if `VT` is not the same type as `T`.
7. Let `VT` be `std::decay_t<T>`. Constructs a `std::move_only_function` whose target is of type `VT` and direct-non-list-initialized with `il, std::forward<CArgs>(args)...`.
* .
* The program is ill-formed if `VT` is not the same type as `T`.
For constructors , the behavior is undefined if `VT` does not satisfy the *Destructible* requirements, or `std::is_move_constructible_v<VT>` is `true` but `VT` does not satisfy the *MoveConstructible* requirements.

## Parameters


### Parameters

- `other` - another `std::move_only_function` to move from
- `f` - a function or a *Callable* object to wrap
- `args` - arguments to construct the target object
- `il` - `std::initializer_list` to construct the target object

## Exceptions

@5-7@ May throw `std::bad_alloc` on allocation failure or propagate the exception thrown by the initialization of the target. No exception is thrown if `VT` is a function pointer type or a specialization of `std::reference_wrapper`.

## Example

