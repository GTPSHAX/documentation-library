---
title: std::expected::expected
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/expected/expected
---


```cpp
dcl|num=1|since=c++23|
constexpr expected();
dcl|num=2|since=c++23|
constexpr expected( const expected& other );
dcl|num=3|since=c++23|
constexpr expected( expected&& other ) noexcept(/* see below */);
dcl|num=4|since=c++23|
template< class U, class G >
constexpr explicit(/* see below */) expected( const expected<U, G>& other );
dcl|num=5|since=c++23|
template< class U, class G >
constexpr explicit(/* see below */) expected( expected<U, G>&& other );
dcla|num=6|since=c++23|notes=|1=
template< class U = std::remove_cv_t<T> >
constexpr explicit(!std::is_convertible_v<U, T>) expected( U&& v );
dcl|num=7|since=c++23|
template< class G >
constexpr explicit(!std::is_convertible_v<const G&, E>)
expected( const std::unexpected<G>& e );
dcl|num=8|since=c++23|
template< class G >
constexpr explicit(!std::is_convertible_v<G, E>)
expected( std::unexpected<G>&& e );
|
template< class... Args >
constexpr explicit expected( std::in_place_t, Args&&... args );
|
template< class U, class... Args >
constexpr explicit expected( std::in_place_t,
std::initializer_list<U> il, Args&&... args );
|
constexpr explicit expected( std::in_place_t ) noexcept;
dcl|num=12|since=c++23|
template< class... Args >
constexpr explicit expected( std::unexpect_t, Args&&... args );
dcl|num=13|since=c++23|
template< class U, class... Args >
constexpr explicit expected( std::unexpect_t,
std::initializer_list<U> il, Args&&... args );
```

Constructs a new `expected` object.
1. Default constructor. If `T` is not (possibly cv-qualified) `void`, constructs an object that contains an expected value, which is value-initialized.
@@ After construction, `has_value()` returns `true`.
@@ .
2. Copy constructor. If `other.has_value()` is `false`, the new object contains an unexpected value, which is direct-initialized from `other.error()`. Otherwise, if `T` is not (possibly cv-qualified) `void`, the new object contains an expected value, which is direct-initialized from `*other`.
@@ After construction, `has_value()` is equal to `other.has_value()`.
@@ This constructor is defined as deleted unless
* either `T` is (possibly cv-qualified) `void`, or `std::is_copy_constructible_v<T>` is `true`, and
* `std::is_copy_constructible_v<E>` is `true`.
@@ This constructor is trivial if
* either `T` is (possibly cv-qualified) `void`, or `std::is_trivially_copy_constructible_v<T>` is `true`, and
* `std::is_trivially_copy_constructible_v<E>` is `true`.
3. Move constructor. If `other.has_value()` is `false`, the new object contains an unexpected value, which is direct-initialized from `std::move(other.error())`. Otherwise, if `T` is not (possibly cv-qualified) `void`, the new object contains an expected value, which is direct-initialized from `std::move(*other)`.
@@ After construction, `has_value()` is equal to `other.has_value()`.
@@ This constructor participates in overload resolution only if
* either `T` is (possibly cv-qualified) `void`, or `std::is_move_constructible_v<T>` is `true`, and
* `std::is_move_constructible_v<E>` is `true`.
@@ This constructor is trivial if
* `std::is_trivially_move_constructible_v<T>` is `true`, and
* `std::is_trivially_move_constructible_v<E>` is `true`.
@4,5@ Let
* `UF` be `std::add_lvalue_reference_t<const U>` for  and `U` for , and
* `GF` be `const G&` for  and `G` for .
@@ If `other.has_value()` is `false`, the new object contains an unexpected value, which is direct-initialized from `std::forward<GF>(other.error())`. Otherwise, if `T` is not (possibly cv-qualified) `void`, the new object contains an expected value, which is direct-initialized from `std::forward<UF>(*other)`.
@@ After construction, `has_value()` is equal to `other.has_value()`.
@@ Each of these constructors does not participate in overload resolution unless the following conditions are met respectively:
* Either
** `T` is (possibly cv-qualified) `void`, and `std::is_void_v<U>` is `true`, or
** `std::is_constructible_v<T, UF>` is `true`.
* `std::is_constructible_v<E, GF>` is `true`.
* If `T` is not (possibly cv-qualified) `bool`, `T` is not constructible or convertible from any expression of type (possibly `const`) `std::expected<U, G>`, i.e., the following 8 values are all `false`:
** `std::is_constructible_v<T, std::expected<U, G>&`
** `std::is_constructible_v<T, std::expected<U, G>`
** `std::is_constructible_v<T, const std::expected<U, G>&`
** `std::is_constructible_v<T, const std::expected<U, G>`
** `std::is_convertible_v<std::expected<U, G>&, T>`
** `std::is_convertible_v<std::expected<U, G>, T>`
** `std::is_convertible_v<const std::expected<U, G>&, T>`
** `std::is_convertible_v<const std::expected<U, G>, T>`
* `std::unexpected<E>` is not constructible from any expression of type (possibly `const`) `std::expected<U, G>`, i.e., the following 4 values are all `false`:
** `std::is_constructible_v<std::unexpected<E>, std::expected<U, G>&`
** `std::is_constructible_v<std::unexpected<E>, std::expected<U, G>`
** `std::is_constructible_v<std::unexpected<E>, const std::expected<U, G>&`
** `std::is_constructible_v<std::unexpected<E>, const std::expected<U, G>`
@@ These constructors are `explicit` if `std::is_convertible_v<UF, T>` or `std::is_convertible_v<GF, E>` is `false`.
6. Constructs an object that contains an expected value, initialized as if direct-initializing (but not direct-list-initializing) an object of type `T` with the expression `std::forward<U>(v)`.
@@ After construction, `has_value()` returns `true`.
@@ This constructor does not participate in overload resolution unless the following conditions are met:
* `T` is not (possibly cv-qualified) `void`.
* `std::is_same_v<std::remove_cvref_t<U>, std::in_place_t>` is `false`.
* `std::is_same_v<expected, std::remove_cvref_t<U>>` is `false`.
* `std::is_constructible_v<T, U>` is `true`.
* `std::remove_cvref_t<U>` is not a specialization of `std::unexpected`.
* If `T` is (possibly cv-qualified) `bool`, `std::remove_cvref_t<U>` is not a specialization of `std::expected`.
@7,8@ Let `GF` be `const G&` for  and `G` for .
Constructs an object that contains an unexpected value, which is direct-initialized from `std::forward<GF>(e.error())`.
@@ After construction, `has_value()` returns `false`.
@@ .
9. Constructs an object that contains an expected value, which is direct-initialized from the arguments `std::forward<Args>(args)...`.
@@ After construction, `has_value()` returns `true`.
@@ .
10. Constructs an object that contains an expected value, which is direct-initialized from the arguments `il, std::forward<Args>(args)...`.
@@ After construction, `has_value()` returns `true`.
@@ .
11. Constructs an object such that after construction, `has_value()` returns `true`.
12. Constructs an object that contains an unexpected value, which is direct-initialized from the arguments `std::forward<Args>(args)...`.
@@ After construction, `has_value()` returns `false`.
@@ .
13. Constructs an object that contains an unexpected value, which is direct-initialized from the arguments `il, std::forward<Args>(args)...`.
@@ After construction, `has_value()` returns `false`.
@@ .

## Parameters


### Parameters

- `other` - another `expected` object whose contained value is copied
- `e` - `std::unexpected` object whose contained value is copied
- `v` - value with which to initialize the contained value
- `args...` - arguments with which to initialize the contained value
- `il` - initializer list with which to initialize the contained value

## Exceptions

1. Throws any exception thrown by the constructor of `T`.
@@ If `T` is (possibly cv-qualified) `void`,
2. Throws any exception thrown by the constructor of `T` or `E`.
3. If `T` is (possibly cv-qualified) `void`,
@@ Otherwise, noexcept|std::is_nothrow_move_constructible_v<T>
&& std::is_nothrow_move_constructible_v<E>
@4,5@ Throws any exception thrown by the constructor of `T` or `E`.
6. Throws any exception thrown by the constructor of `T`.
@7,8@ Throws any exception thrown by the constructor of `E`.
@9,10@ Throws any exception thrown by the constructor of `T`.
@12,13@ Throws any exception thrown by the constructor of `E`.

## Example


## See also


| cpp/utility/expected/dsc unexpected | (see dedicated page) |
| cpp/utility/dsc in_place | (see dedicated page) |
| cpp/utility/expected/dsc unexpect_t | (see dedicated page) |

