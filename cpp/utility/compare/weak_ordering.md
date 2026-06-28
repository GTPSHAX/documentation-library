---
title: std::weak_ordering
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/compare/weak_ordering
---

ddcl|since=c++20|header=compare|1=
class weak_ordering;
The class type `std::weak_ordering` is the result type of a three-way comparison that:
* Admits all six relational operators (`1===`, `1=!=`, `<`, `1=<=`, `>`, `1=>=`).
* [Connected relation|Does not allow incomparable values](https://en.wikipedia.org/wiki/Connected relation|Does not allow incomparable values): exactly one of `a < b`, `1=a == b`, or `a > b` must be `true`.

## Constants

The type `std::weak_ordering` has three valid values, implemented as const static data members of its type:


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Conversions

`std::weak_ordering` is implicitly-convertible to `std::partial_ordering`, while `std::strong_ordering` is implicitly-convertible to `weak_ordering`.
member|operator partial_ordering|2=
ddcl|1=
constexpr operator partial_ordering() const noexcept;

## Return value

`std::partial_ordering::less` if `v` is `less`, `std::partial_ordering::greater` if `v` is `greater`,
`std::partial_ordering::equivalent` if `v` is `equivalent`.

## Comparisons

Comparison operators are defined between values of this type and literal `0`. This supports the expressions `1=a <=> b == 0` or `1=a <=> b < 0` that can be used to convert the result of a three-way comparison operator to a boolean relationship; see  `cpp/utility/compare/named_comparison_functions|std::is_eq`, `cpp/utility/compare/named_comparison_functions|std::is_lt`, etc.
The behavior of a program that attempts to compare a `weak_ordering` with anything other than the integer literal `0` is undefined.


| cpp/utility/compare/weak_ordering|inlinemem=true|title=operator==<br>operator<<br>operator><br>operator<=<br>operator>=<br>operator<=>|compares with zero or a `weak_ordering` | |

member|operator|2=

```cpp
dcl|num=1|1=
friend constexpr bool operator==( weak_ordering v, /*unspecified*/ u ) noexcept;
dcl|num=2|1=
friend constexpr bool operator==( weak_ordering v, weak_ordering w ) noexcept = default;
```


## Parameters


### Parameters

- `v, w` - `std::weak_ordering` values to check
- `u` - an unused parameter of any type that accepts literal zero argument

## Return value

1. `true` if `v` is `equivalent`, `false` if `v` is `less` or `greater`
2. `true` if both parameters hold the same value, `false` otherwise
member|operator&lt;|2=

```cpp
dcl|num=1|1=
friend constexpr bool operator<( weak_ordering v, /*unspecified*/ u ) noexcept;
dcl|num=2|1=
friend constexpr bool operator<( /*unspecified*/ u, weak_ordering v ) noexcept;
```


## Parameters


### Parameters

- `v` - a `std::weak_ordering` value to check
- `u` - an unused parameter of any type that accepts literal zero argument

## Return value

1. `true` if `v` is `less`, and `false` if `v` is `greater` or `equivalent`
2. `true` if `v` is `greater`, and `false` if `v` is `less` or `equivalent`
member|operator&lt;|2=

```cpp
dcl|num=1|1=
friend constexpr bool operator<=( weak_ordering v, /*unspecified*/ u ) noexcept;
dcl|num=2|1=
friend constexpr bool operator<=( /*unspecified*/ u, weak_ordering v ) noexcept;
```


## Parameters


### Parameters

- `v` - a `std::weak_ordering` value to check
- `u` - an unused parameter of any type that accepts literal zero argument

## Return value

1. `true` if `v` is `less` or `equivalent`, and `false` if `v` is `greater`
2. `true` if `v` is `greater` or `equivalent`, and `false` if `v` is `less`
member|operator&gt;|2=

```cpp
dcl|num=1|1=
friend constexpr bool operator>( weak_ordering v, /*unspecified*/ u ) noexcept;
dcl|num=2|1=
friend constexpr bool operator>( /*unspecified*/ u, weak_ordering v ) noexcept;
```


## Parameters


### Parameters

- `v` - a `std::weak_ordering` value to check
- `u` - an unused parameter of any type that accepts literal zero argument

## Return value

1. `true` if `v` is `greater`, and `false` if `v` is `less` or `equivalent`
2. `true` if `v` is `less`, and `false` if `v` is `greater` or `equivalent`
member|operator&gt;|2=

```cpp
dcl|num=1|1=
friend constexpr bool operator>=( weak_ordering v, /*unspecified*/ u ) noexcept;
dcl|num=2|1=
friend constexpr bool operator>=( /*unspecified*/ u, weak_ordering v ) noexcept;
```


## Parameters


### Parameters

- `v` - a `std::weak_ordering` value to check
- `u` - an unused parameter of any type that accepts literal zero argument

## Return value

1. `true` if `v` is `greater` or `equivalent`, and `false` if `v` is `less`
2. `true` if `v` is `less` or `equivalent`, and `false` if `v` is `greater`
member|operator<>|2=

```cpp
dcl|num=1|1=
friend constexpr weak_ordering operator<=>( weak_ordering v, /*unspecified*/ u ) noexcept;
dcl|num=2|1=
friend constexpr weak_ordering operator<=>( /*unspecified*/ u, weak_ordering v ) noexcept;
```


## Parameters


### Parameters

- `v` - a `std::weak_ordering` value to check
- `u` - an unused parameter of any type that accepts literal zero argument

## Return value

1. `v`.
2. `greater` if `v` is `less`, `less` if `v` is `greater`, otherwise `v`.

## Example

