---
title: std::expected::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/expected/operator=
---


```cpp
dcla|num=1|since=c++23|1=
constexpr expected& operator=( const expected& other );
dcla|num=2|since=c++23|1=
constexpr expected& operator=( expected&& other ) noexcept(/*see below*/);
dcla|num=3|since=c++23|notes=|1=
template< class U = std::remove_cv_t<T> >
constexpr expected& operator=( U&& v );
dcla|num=4|since=c++23|1=
template< class G >
constexpr expected& operator=( const unexpected<G>& other );
dcla|num=5|since=c++23|1=
template< class G >
constexpr expected& operator=( unexpected<G>&& other );
```

Assigns a new value to an existing `expected` object.
@1,2@ Assigns the state of `other`.
* If `this->has_value()` equals `other.has_value()`, assigns the value contained in `other`. Does nothing if `T` is (possibly cv-qualified) `void` and `other.has_value()` is .
* Otherwise, destroys the currently contained value (does nothing if `this->has_value()` is  and `T` is (possibly cv-qualified) `void`), and makes `*this` contain a copy of the value contained in `other`.
: If `other.has_value()` is  and `T` is (possibly cv-qualified) `void`, does not construct the new value. Otherwise, the new value is copy-constructed  or move-constructed  from `*other` or `other.error()`, as appropriate. If an exception is thrown, the old value is retained; `*this` does not become valueless.
If no exception was thrown, after assignment, `has_value()` is equal to `other.has_value()`.
* Overload  is defined as deleted unless
** either `T` is (possibly cv-qualified) `void` or `std::is_copy_assignable_v<T>` is , and
** either `T` is (possibly cv-qualified) `void` or `std::is_copy_constructible_v<T>` is , and
** `std::is_copy_assignable_v<E>` is , and
** `std::is_copy_constructible_v<E>` is , and
** at least one of the following is :
*** `T` is (possibly cv-qualified) `void`
*** `std::is_nothrow_move_constructible_v<T>`
*** `std::is_nothrow_move_constructible_v<E>`
* Overload  participates in overload resolution only if
** either `T` is (possibly cv-qualified) `void` or `std::is_move_assignable_v<T>` is , and
** either `T` is (possibly cv-qualified) `void` or `std::is_move_constructible_v<T>` is , and
** `std::is_move_assignable_v<E>` is , and
** `std::is_move_constructible_v<E>` is , and
** at least one of the following is :
*** `T` is (possibly cv-qualified) `void`
*** `std::is_nothrow_move_constructible_v<T>`
*** `std::is_nothrow_move_constructible_v<E>`
3. Assigns from expected value.
* If `this->has_value()` is , equivalent to `1=**this = std::forward<U>(v)`.
* Otherwise, destroys the value contained in `*this`, and makes `*this` contain a value initialized from `std::forward<U>(v)`. If an exception is thrown, the old value is retained; `*this` does not become valueless.
If no exception was thrown, after assignment, `this->has_value()` is .
* cpp/enable_if|
** `std::is_same_v<expected, std::remove_cvref_t<U>>` is , and
** `std::remove_cvref_t<U>` is not a specialization of `std::unexpected`, and
** `std::is_constructible_v<T, U>` is , and
** `std::is_assignable_v<T&, U>` is , and
** at least one of the following is :
*** `std::is_nothrow_constructible_v<T, U>`
*** `std::is_nothrow_move_constructible_v<T>`
*** `std::is_nothrow_move_constructible_v<E>`
@4,5@ Assigns from unexpected value.
Let `GF` be `const G&` for overload , and `G` for overload .
* If `this->has_value()` is , destroys the value contained in `*this` (does nothing if `T` is (possibly cv-qualified) `void`), and makes `*this` contain a value initialized from `std::forward<GF>(e.error())`. If an exception is thrown, the old value is retained; `*this` does not become valueless.
* Otherwise, equivalent to `1=this->error() = std::forward<GF>(e.error())`.
If no exception was thrown, after assignment, `this->has_value()` is .
* cpp/enable_if|
** `std::is_constructible_v<E, GF>` is , and
** `std::is_assignable_v<E&, GF>` is , and
** at least one of the following is :
*** `T` is (possibly cv-qualified) `void`
*** `std::is_nothrow_constructible_v<E, GF>`
*** `std::is_nothrow_move_constructible_v<T>`
*** `std::is_nothrow_move_constructible_v<E>`
In all cases, if `T` is not (possibly cv-qualified) `void`, the destruction of old value and construction of new value is performed as if by the following exposition-only function `reinit_expected`.

```cpp
template<class NewType, class OldType, class... Args>
constexpr void reinit_expected(NewType& new_val, OldType& old_val, Args&&... args)
{
    if constexpr (std::is_nothrow_constructible_v<NewType, Args...>)
    {
        std::destroy_at(std::addressof(old_val));
        std::construct_at(std::addressof(new_val), std::forward<Args>(args)...);
    }
    else if constexpr (std::is_nothrow_move_constructible_v<NewType>)
    {
        NewType temp(std::forward<Args>(args)...); // may throw
        std::destroy_at(std::addressof(old_val));
        std::construct_at(std::addressof(new_val), std::move(temp));
    }
    else
    {
        OldType temp(std::move(old_val));
        std::destroy_at(std::addressof(old_val));
        try
        {
            std::construct_at(std::addressof(new_val), std::forward<Args>(args)...); // may throw
        }
        catch (...)
        {
            std::construct_at(std::addressof(old_val), std::move(temp));
            throw;
        }
    }
}
```


## Parameters


### Parameters

- `other` - another `expected` object whose contained value to assign
- `value` - value to assign to the contained value
- `e` - `cpp/utility/expected/unexpected|std::unexpected` object whose contained value to assign

## Return value

`*this`

## Exceptions

1. Throws any exception thrown by the copy constructor or copy assignment operator of `T` or `E`.
2. If `T` is (possibly cv-qualified) `void`,
Otherwise, noexcept|
std::is_nothrow_move_constructible_v<T> && std::is_nothrow_move_assignable_v<T> &&
std::is_nothrow_move_constructible_v<E> && std::is_nothrow_move_assignable_v<E>
3. Throws any exception thrown by the constructor or assignment operator of `T`.
@4,5@ Throws any exception thrown by the constructor or assignment operator of `E`.

## Example


## See also


| cpp/utility/expected/dsc emplace | (see dedicated page) |

