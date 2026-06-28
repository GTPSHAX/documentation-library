---
title: std::is_destructible
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_destructible
---


```cpp
**Header:** `<`type_traits`>`
dcla|since=c++11|num=1|1=
template< class T >
struct is_destructible;
dcla|since=c++11|num=2|1=
template< class T >
struct is_trivially_destructible;
dcla|since=c++11|num=3|1=
template< class T >
struct is_nothrow_destructible;
```

1. If `T` is a reference type, provides the member constant `value` equal to `true`.
@@ If `T` is (possibly cv-qualified) `void`, a function type, or an array of unknown bound, `value` equals `false`.
@@ If `T` is an object type, then, for the type `U` that is `std::remove_all_extents<T>::type`, if the expression `std::declval<U&>().~U()` is well-formed in unevaluated context, `value` equals `true`. Otherwise, `value` equals `false`.
2. Same as  and additionally `std::remove_all_extents<T>::type` is either a non-class type or a class type with a trivial destructor.
3. Same as , but the destructor is `noexcept`.

## Helper variable templates


```cpp
dcl|since=c++17|1=
template< class T >
constexpr bool is_destructible_v = is_destructible<T>::value;
dcl|since=c++17|1=
template< class T >
constexpr bool is_trivially_destructible_v = is_trivially_destructible<T>::value;
dcl|since=c++17|1=
template< class T >
constexpr bool is_nothrow_destructible_v = is_nothrow_destructible<T>::value;
```


## Notes

Because the C++ program terminates if a destructor throws an exception during stack unwinding (which usually cannot be predicted), all practical destructors are non-throwing even if they are not declared noexcept. All destructors found in the C++ standard library are non-throwing.
Storage occupied by trivially destructible objects may be reused without calling the destructor.

## Possible implementation

eq impl
|title1=is_destructible (1)|ver1=1|1=
// C++20 required
template<typename t>
struct is_destructible
: std::integral_constant<bool, requires(t object) { object.~t(); }>
{};
|title2=is_trivially_destructible (2)|ver2=2|2=
// Not real C++. Shall P2996 be approved, the following implementation will be available:
template<typename t>
struct is_trivially_destructible
: std::integral_constant<bool, std::meta::type_is_trivially_destructible(^t)>
{};
|title3=is_nothrow_destructible (3)|ver3=3|3=
// C++20 required
template<typename t>
struct is_nothrow_destructible
: std::integral_constant<bool, requires(t object) { {object.~t()} noexcept; }>
{};

## Example


### Example

```cpp
#include <iostream>
#include <string>
#include <type_traits>

struct Foo
{
    std::string str;
    ~Foo() noexcept {};
};

struct Bar
{
    ~Bar() = default;
};

static_assert(std::is_destructible<std::string>::value == true);
static_assert(std::is_trivially_destructible_v<Foo> == false);
static_assert(std::is_nothrow_destructible<Foo>() == true);
static_assert(std::is_trivially_destructible<Bar>{} == true);

int main() {}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2049 | c++11 | the specification was incompletable because of the imaginary wrapping struct | made complete |


## See also


| cpp/types/dsc is_constructible | (see dedicated page) |
| cpp/types/dsc has_virtual_destructor | (see dedicated page) |
| cpp/concepts/dsc destructible | (see dedicated page) |
| cpp/language/dsc destructor | (see dedicated page) |

