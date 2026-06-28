---
title: std::vector::reference
type: Containers
source: https://en.cppreference.com/w/cpp/container/vector_bool/reference
---


# petty|vector<bool, Alloc>::

reference
ddcl|
class reference;
The `std::vector``<bool, Alloc>` specializations define `std::vector``<bool, Alloc>::reference` as a publicly-accessible nested class. `std::vector``<bool, Alloc>::reference` proxies the behavior of references to a single bit in `std::vector``<bool, Alloc>`.
The primary use of `std::vector``<bool, Alloc>::reference` is to provide an lvalue that can be returned from `operator[]`.
Any reads or writes to a vector that happen via a `std::vector``<bool, Alloc>::reference` potentially read or write to the entire underlying vector.

## Member functions


| cpp/container/vector_bool/reference/dsc operator bool | (see dedicated page) |

member|reference|2=
ddcla|since=c++11|constexpr=c++20|1=
reference( const reference& ) = default;
Constructs the reference from another reference.<sup>(until C++11)</sup>  The copy constructor is implicitly declared.
Other constructors can only be accessed by `std::vector``<bool, Alloc>`.
member|~reference|2=
ddcla|constexpr=c++20|
~reference();
Destroys the reference.
member|operator|2=

```cpp
dcla|num=1|noexcept=c++11|constexpr=c++20|1=
reference& operator=( bool x );
dcl|num=2|since=c++23|1=
constexpr const reference& operator=( bool x ) const noexcept;
dcla|num=3|noexcept=c++11|constexpr=c++20|1=
reference& operator=( const reference& x );
```

Assigns a value to the referenced bit.

## Parameters


### Parameters

- `x` - value to assign

## Return value

`*this`
member|operator bool|2=
ddcla|noexcept=c++11|constexpr=c++20|
operator bool() const;
Returns the value of the referenced bit.

## Return value

The referenced bit.
member|flip|2=
ddcla|noexcept=c++11|constexpr=c++20|
void flip();
Inverts the referenced bit.

## Helper classes

member|formatter|2=
ddcl|since=c++23|
template< class T, class CharT >
requires /*is-vector-bool-reference*/<T>
struct formatter<T, CharT>;
Specializes the `std::formatter` for `std::vector``<bool, Alloc>::reference`. The specialization uses `std::formatter<bool, CharT>` as its underlying formatter (denoted as ) where the referenced bit is converted to `bool` to be formatted.
The exposition-only constant `/*is-vector-bool-reference*/<T>` is `true` if and only if `T` denotes the type `std::vector``<bool, Alloc>::reference` for some type `Alloc` and `std::vector``<bool, Alloc>` is not a program-defined specialization.

### Member functions


```cpp
dcl|num=1|since=c++23|
template< class ParseContext >
constexpr ParseContext::iterator parse( ParseContext& ctx );
dcl|num=2|since=c++23|
template< class FormatContext >
FormatContext::iterator format( const T& r, FormatContext& ctx ) const;
```

1. Equivalent to .
2. Equivalent to .

## Example


## External links

