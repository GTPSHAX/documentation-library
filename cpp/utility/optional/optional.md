---
title: std::optional::optional
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/optional/optional
---


```cpp
dcl|num=1|since=c++17|
constexpr optional() noexcept;
constexpr optional( std::nullopt_t ) noexcept;
dcl|num=2|since=c++17|
constexpr optional( const optional& other );
dcl|num=3|since=c++17|
constexpr optional( optional&& other ) noexcept(/* see below */);
dcla|num=4|since=c++17|constexpr=c++20|notes=|
template < class U >
optional( const optional<U>& other );
dcla|num=5|since=c++17|constexpr=c++20|notes=|
template < class U >
optional( optional<U>&& other );
dcl|num=6|since=c++17|
template< class... Args >
constexpr explicit optional( std::in_place_t, Args&&... args );
dcl|num=7|since=c++17|
template< class U, class... Args >
constexpr explicit optional( std::in_place_t,
std::initializer_list<U> ilist,
Args&&... args );
dcla|num=8|since=c++17|notes=|1=
template < class U = std::remove_cv_t<T> >
constexpr optional( U&& value );
```

Constructs a new optional object.
1. Constructs an object that ''does not contain'' a value.
2. Copy constructor: If `other` contains a value, initializes the contained value as if direct-initializing (but not direct-list-initializing) an object of type `T` with the expression `*other`. If `other` does not contain a value, constructs an object that ''does not contain'' a value.
* This constructor is defined as deleted if `std::is_copy_constructible_v<T>` is `false`.
* It is a trivial constructor if `std::is_trivially_copy_constructible_v<T>` is `true`.
3. Move constructor: If `other` contains a value, initializes the contained value as if direct-initializing (but not direct-list-initializing) an object of type `T` with the expression `std::move(*other)` and ''does not'' make `other` empty: a moved-from `std::optional` still ''contains'' a value, but the value itself is moved from. If `other` does not contain a value, constructs an object that ''does not contain'' a value.
* This constructor does not participate in overload resolution unless `std::is_move_constructible_v<T>` is `true`.
* It is a trivial constructor if `std::is_trivially_move_constructible_v<T>` is `true`.
4. Converting copy constructor: If `other` does not contain a value, constructs an optional object that ''does not contain'' a value. Otherwise, constructs an optional object that ''contains'' a value, initialized as if direct-initializing (but not direct-list-initializing) an object of type `T` with the expression `*other`.
* This constructor does not participate in overload resolution unless the following conditions are met:
** `std::is_constructible_v<T, const U&>` is `true`.
** If `T` is not (possibly cv-qualified) `bool`, `T` is not constructible or convertible from any expression of type (possibly `const`) `std::optional<U>`, i.e., `converts_from_any_cvref<T, std::optional<U>>` is `false`, where `converts_from_any_cvref` is described below.
* This constructor is `explicit` if and only if `std::is_convertible_v<const U&, T>` is `false`.
5. Converting move constructor: If `other` does not contain a value, constructs an optional object that ''does not contain'' a value. Otherwise, constructs an optional object that ''contains'' a value, initialized as if direct-initializing (but not direct-list-initializing) an object of type `T` with the expression `std::move(*other)`.
* This constructor does not participate in overload resolution unless the following conditions are met:
** `std::is_constructible_v<T, U&&>` is `true`.
** If `T` is not (possibly cv-qualified) `bool`, `T` is not constructible or convertible from any expression of type (possibly `const`) `std::optional<U>`, i.e., `converts_from_any_cvref<T, std::optional<U>>` is `false`, where `converts_from_any_cvref` is described below.
* This constructor is `explicit` if and only if `std::is_convertible_v<U&&, T>` is `false`.
6. Constructs an optional object that ''contains'' a value, initialized as if direct-initializing (but not direct-list-initializing) an object of type `T` from the arguments `std::forward<Args>(args)...`.
* If the selected constructor of `T` is a `constexpr` constructor, this constructor is a `constexpr` constructor.
* The function does not participate in the overload resolution unless `std::is_constructible_v<T, Args...>` is `true`.
7. Constructs an optional object that ''contains'' a value, initialized as if direct-initializing (but not direct-list-initializing) an object of type `T` from the arguments `ilist, std::forward<Args>(args)...`.
* If the selected constructor of `T` is a `constexpr` constructor, this constructor is a `constexpr` constructor.
* The function does not participate in the overload resolution unless `std::is_constructible_v<T, std::initializer_list<U>&, Args...>` is `true`.
8. Constructs an optional object that ''contains'' a value, initialized as if  direct-initializing (but not direct-list-initializing) an object of type `T` with the expression `std::forward<U>(value)`.
* If the selected constructor of `T` is a `constexpr` constructor, this constructor is a `constexpr` constructor.
* This constructor does not participate in overload resolution unless the following conditions are met:
** `std::is_constructible_v<T, U&&>` is `true`.
** <sup>(until C++20)</sup> `std::decay_t<U>`<sup>(since C++20)</sup> `std::remove_cvref_t<U>` is neither `std::in_place_t` nor `std::optional<T>`.
** If `T` is (possibly cv-qualified) `bool`, <sup>(until C++20)</sup> `std::decay_t<U>`<sup>(since C++20)</sup> `std::remove_cvref_t<U>` is not a specialization of `std::optional`.
* This constructor is `explicit` if and only if `std::is_convertible_v<U&&, T>` is `false`.
The helper variable template `converts_from_any_cvref` is equivalent to:

```cpp
template< class T, class W >
constexpr bool converts_from_any_cvref =
    std::disjunction_v<std::is_constructible<T, W&>, std::is_convertible<W&, T>,
                       std::is_constructible<T, W>, std::is_convertible<W, T>,
                       std::is_constructible<T, const W&>, std::is_convertible<const W&, T>,
                       std::is_constructible<T, const W>, std::is_convertible<const W, T>>;
```


## Parameters


### Parameters

- `other` - another optional object whose contained value is copied
- `value` - value with which to initialize the contained value
- `args...` - arguments with which to initialize the contained value
- `ilist` - initializer list with which to initialize the contained value

## Exceptions

2. Throws any exception thrown by the constructor of `T`.
3. Throws any exception thrown by the constructor of `T`. Has the following
@4-8@ Throws any exception thrown by the constructor of `T`.

## Notes

Before the resolution of , constructing an `std::optional<bool>` from `std::optional<U>` would select overload  instead of overloads  if `U` is not `bool`. This is because overloads  did not participate in overload resolution if `T` (`bool` in this case) can be constructed or converted from `std::optional<U>`, but `std::optional::operator bool` makes the conversion possible for any `U`.
As a result, the constructed `std::optional<bool>` always contains a value. That value is determined by whether the provided `std::optional<U>` object contains a value, rather than the `bool` value direct-initialized from the contained value:

```cpp
std::optional<bool> op_false(false);
std::optional<int> op_zero(0);

std::optional<int> from_bool(op_false); // OK: contains 0 (initialized from false)
std::optional<bool> from_int(op_zero);  // DEFECT (LWG 3836): contains true because
                                        // op_zero contains a value, even if initializing
                                        // bool from that value gives false
```


## Example


### Example

```cpp
#include <iostream>
#include <optional>
#include <string>

int main()
{
    std::optional<int> o1, // empty
                       o2 = 1, // init from rvalue
                       o3 = o2; // copy-constructor

    // calls std::string( initializer_list<CharT> ) constructor
    std::optional<std::string> o4(std::in_place, {'a', 'b', 'c'});

    // calls std::string( size_type count, CharT ch ) constructor
    std::optional<std::string> o5(std::in_place, 3, 'A');

    // Move-constructed from std::string using deduction guide to pick the type

    std::optional o6(std::string{"deduction"});

    std::cout << *o2 << ' ' << *o3 << ' ' << *o4 << ' ' << *o5  << ' ' << *o6 << '\n';
}
```


**Output:**
```
1 1 abc AAA deduction
```


## Defect reports


## See also


| cpp/utility/optional/dsc make_optional | (see dedicated page) |

