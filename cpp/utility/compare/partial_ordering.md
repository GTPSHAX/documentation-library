---
title: std::partial_ordering
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/compare/partial_ordering
---

ddcl|since=c++20|header=compare|1=
class partial_ordering;
The class type `std::partial_ordering` is the result type of a three-way comparison that:
* Admits all six relational operators (`1===`, `1=!=`, `<`, `1=<=`, `>`, `1=>=`).
* [Connected relation|Admits incomparable values](https://en.wikipedia.org/wiki/Connected relation|Admits incomparable values): `a < b`, `1=a == b`, and `a > b` may all be `false`.

## Constants

The type `std::partial_ordering` has four valid values, implemented as const static data members of its type:


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Conversions

`std::partial_ordering` cannot be implicitly converted to other comparison category types, while both `std::strong_ordering` and `std::weak_ordering` are implicitly-convertible to `partial_ordering`.

## Comparisons

Comparison operators are defined between values of this type and literal `0`. This supports the expressions `1=a <=> b == 0` or `1=a <=> b < 0` that can be used to convert the result of a three-way comparison operator to a boolean relationship; see  `cpp/utility/compare/named comparison functions|std::is_eq`, `cpp/utility/compare/named comparison functions|std::is_lt`, etc.
The behavior of a program that attempts to compare a `partial_ordering` with anything other than the integer literal `0` is undefined.


| cpp/utility/compare/partial_ordering|inlinemem=true|title=operator | |

member|operator|2=

```cpp
dcl|num=1|1=
friend constexpr bool operator==( partial_ordering v, /*unspecified*/ u ) noexcept;
dcl|num=2|1=
friend constexpr bool
operator==( partial_ordering v, partial_ordering w ) noexcept = default;
```


## Parameters


### Parameters

- `v, w` - `std::partial_ordering` values to check
- `u` - an unused parameter of any type that accepts literal zero argument

## Return value

1. `true` if `v` is `equivalent`, `false` if `v` is `less`, `greater`, or `unordered`
2. `true` if both parameters hold the same value, `false` otherwise
member|operator&lt;|2=

```cpp
dcl|num=1|1=
friend constexpr bool operator<( partial_ordering v, /*unspecified*/ u ) noexcept;
dcl|num=2|1=
friend constexpr bool operator<( /*unspecified*/ u, partial_ordering v ) noexcept;
```


## Parameters


### Parameters

- `v` - a `std::partial_ordering` value to check
- `u` - an unused parameter of any type that accepts literal zero argument

## Return value

1. `true` if `v` is `less`, and `false` if `v` is `greater`, `equivalent`, or `unordered`
2. `true` if `v` is `greater`, and `false` if `v` is `less`, `equivalent`, or `unordered`
member|operator&lt;|2=

```cpp
dcl|num=1|1=
friend constexpr bool operator<=( partial_ordering v, /*unspecified*/ u ) noexcept;
dcl|num=2|1=
friend constexpr bool operator<=( /*unspecified*/ u, partial_ordering v ) noexcept;
```


## Parameters


### Parameters

- `v` - a `std::partial_ordering` value to check
- `u` - an unused parameter of any type that accepts literal zero argument

## Return value

1. `true` if `v` is `less` or `equivalent`, and `false` if `v` is `greater` or `unordered`
2. `true` if `v` is `greater` or `equivalent`, and `false` if `v` is `less` or `unordered`
member|operator&gt;|2=

```cpp
dcl|num=1|1=
friend constexpr bool operator>( partial_ordering v, /*unspecified*/ u ) noexcept;
dcl|num=2|1=
friend constexpr bool operator>( /*unspecified*/ u, partial_ordering v ) noexcept;
```


## Parameters


### Parameters

- `v` - a `std::partial_ordering` value to check
- `u` - an unused parameter of any type that accepts literal zero argument

## Return value

1. `true` if `v` is `greater`, and `false` if `v` is `less`, `equivalent`, or `unordered`
2. `true` if `v` is `less`, and `false` if `v` is `greater`, `equivalent`, or `unordered`
member|operator&gt;|2=

```cpp
dcl|num=1|1=
friend constexpr bool operator>=( partial_ordering v, /*unspecified*/ u ) noexcept;
dcl|num=2|1=
friend constexpr bool operator>=( /*unspecified*/ u, partial_ordering v ) noexcept;
```


## Parameters


### Parameters

- `v` - a `std::partial_ordering` value to check
- `u` - an unused parameter of any type that accepts literal zero argument

## Return value

1. `true` if `v` is `greater` or `equivalent`, and `false` if `v` is `less` or `unordered`
2. `true` if `v` is `less` or `equivalent`, and `false` if `v` is `greater` or `unordered`
member|operator<>|2=

```cpp
dcl|num=1|1=
friend constexpr partial_ordering operator<=>( partial_ordering v, /*unspecified*/ u ) noexcept;
dcl|num=2|1=
friend constexpr partial_ordering operator<=>( /*unspecified*/ u, partial_ordering v ) noexcept;
```


## Parameters


### Parameters

- `v` - a `std::partial_ordering` value to check
- `u` - an unused parameter of any type that accepts literal zero argument

## Return value

1. `v`.
2. `greater` if `v` is `less`, `less` if `v` is `greater`, otherwise `v`.

## Notes

The built-in `1= operator<=>` between floating-point values uses this ordering: the positive zero and the negative zero compare `equivalent`, but can be distinguished, and NaN values compare `unordered` with any other value.

## Example

