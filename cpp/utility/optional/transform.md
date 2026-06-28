---
title: std::optional::transform
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/optional/transform
---


```cpp
dcl | num=1 | since=c++23 | 1=
template< class F >
constexpr auto transform( F&& f ) &;
dcl | num=2 | since=c++23 | 1=
template< class F >
constexpr auto transform( F&& f ) const&;
dcl | num=3 | since=c++23 | 1=
template< class F >
constexpr auto transform( F&& f ) &&;
dcl | num=4 | since=c++23 | 1=
template< class F >
constexpr auto transform( F&& f ) const&&;
```

If `*this` contains a value, invokes `f` with the contained value as an argument, and returns an `std::optional` that contains the result of that invocation; otherwise, returns an empty `std::optional`.
The type of contained value in the result (denoted by `U` below) must be a non-array object type, and must not be `std::in_place_t` or `std::nullopt_t`). Otherwise, the program is ill-formed.
1. Let `U` be `std::remove_cv_t<std::invoke_result_t<F, T&>>`. If `*this` contains a value, returns a `std::optional<U>` whose contained value is direct-initialized from `std::invoke(std::forward<F>(f), **this)` (unlike `and_then()`, which must return an `std::optional` directly). Otherwise, returns an empty `std::optional<U>`.
* The program is ill-formed if the variable definition `U x(std::invoke(std::forward<F>(f), **this));` is ill-formed.
2. Same as , except that `U` is `std::remove_cv_t<std::invoke_result_t<F, const T&>>`.
3. Let `U` be `std::remove_cv_t<std::invoke_result_t<F, T>>`. If `*this` contains a value, returns a `std::optional<U>` whose contained value is direct-initialized from `std::invoke(std::forward<F>(f), std::move(**this))`. Otherwise, returns an empty `std::optional<U>`.
* The program is ill-formed if the variable definition `U x(std::invoke(std::forward<F>(f), std::move(**this)));` is ill-formed.
4. Same as , except that `U` is `std::remove_cv_t<std::invoke_result_t<F, const T>>`.

## Parameters


### Parameters


## Return value

An `std::optional` containing the result of `f` or an empty `std::optional`, as described above.

## Notes

Because `transform` directly constructs a `U` object at the right location, rather than passing it to a constructor, `std::is_move_constructible_v<U>` can be `false`.
As the callable `f` can't return a reference type, it cannot be a pointer to data member.
Some languages call this operation ''map''.

## Example


### Example


**Output:**
```
o_A has a value
A => B
B => C
C => D
o_D has a value

o_A is empty
o_D is empty
```


## See also

