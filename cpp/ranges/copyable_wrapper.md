---
title: Assignable wrapper
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/copyable_wrapper
---


# Assignable wrapper mark c++20


```cpp
dcl rev multi
|since1=c++20|notes1=|dcl1=
template< class T >
requires std::copy_constructible<T> && std::is_object_v<T>
class /*copyable-box*/;
|since2=c++23|notes2=|dcl2=
template< class T >
requires std::move_constructible<T> && std::is_object_v<T>
class /*movable-box*/;
```

`cpp/ranges/single_view|ranges::single_view`<sup>(since C++23)</sup> , `cpp/ranges/repeat_view|ranges::repeat_view`, and range adaptors that store an invocable object are specified in terms of an exposition-only class template <sup>(until C++23)</sup> <sup>(since C++23)</sup> . The name shown here is for exposition purposes only.
The wrapper behaves exactly like `std::optional<T>`, except that the default constructor, copy assignment operator, and move assignment operator are (conditionally) different from those of `std::optional`, which augments `T` with assignability when needed and makes it always satisfy <sup>(since C++23)</sup> or .
rrev multi
|rev1=
If `T` is already , or both `std::is_nothrow_move_constructible_v<T>` and `std::is_nothrow_copy_constructible_v<T>` are `true`, `/*copyable-box*/<T>` may store only a `T` object, because it always contains a value.
|since2=c++23|rev2=
If `T`
* is already , or
* is  and both `std::is_nothrow_move_constructible_v<T>` and `std::is_nothrow_copy_constructible_v<T>` are `true`, or
* does not satisfy  but satisfies , or
* does not satisfy  but `std::is_nothrow_move_constructible_v<T>` is `true`,
`/*movable-box*/<T>` may store only a `T` object, because it always contains a value.

## Template parameters


### Parameters

- `T` - the type of the contained value, must be an object type that models <sup>(until C++23)</sup> <sup>(since C++23)</sup> 

## Member functions

member|Default constructor|

```cpp
dcl rev multi
|since1=c++20|dcl1=
constexpr /*copyable-box*/() noexcept(std::is_nothrow_default_constructible_v<T>)
requires std::default_initializable<T>
: /*copyable-box*/(std::in_place) { }
|since2=c++23|dcl2=
constexpr /*movable-box*/() noexcept(std::is_nothrow_default_constructible_v<T>)
requires std::default_initializable<T>
: /*movable-box*/(std::in_place) { }
```

The default constructor is provided if and only if `T` models .
A default-constructed wrapper contains a value-initialized `T` object.
member|Assignment operators|

```cpp
dcl rev multi|num=1
|since1=c++20|dcl1=
constexpr /*copyable-box*/& operator=(const /*copyable-box*/& other);
noexcept(/* see below */);
|since2=c++23|dcl2=
constexpr /*movable-box*/& operator=(const /*movable-box*/& other);
noexcept(/* see below */) requires std::copy_constructible<T>;
dcl rev multi|num=2
|since1=c++20|dcl1=
constexpr /*copyable-box*/& operator=(/*copyable-box*/&& other)
noexcept(std::is_nothrow_move_constructible_v<T>);
|since2=c++23|dcl2=
constexpr /*movable-box*/& operator=(/*movable-box*/&& other)
noexcept(std::is_nothrow_move_constructible_v<T>);
```

1. If `std::copyable<T>` is not modeled, the copy assignment operator is equivalently defined as:
rrev multi
|rev1=
c|1=
constexpr /*copyable-box*/& operator=(const /*copyable-box*/& other)
noexcept(std::is_nothrow_copy_constructible_v<T>)
{
if (this != std::addressof(other))
if (other)
emplace(*other);
else
reset();
return *this;
}
|since2=c++23|rev2=
c|1=
constexpr /*movable-box*/& operator=(const /*movable-box*/& other)
noexcept(std::is_nothrow_copy_constructible_v<T>)
requires std::copy_constructible<T>
{
if (this != std::addressof(other))
if (other)
emplace(*other);
else
reset();
return *this;
}
Otherwise, it is identical to the copy assignment operator of `std::optional`.
2. If `std::movable<T>` is not modeled, the move assignment operator is equivalently defined as:
rrev multi
|rev1=
c|1=
constexpr /*copyable-box*/& operator=(/*copyable-box*/&& other)
noexcept(std::is_nothrow_move_constructible_v<T>)
{
if (this != std::addressof(other))
if (other)
emplace(std::move(*other));
else
reset();
return *this;
}
|since2=c++23|rev2=
c|1=
constexpr /*movable-box*/& operator=(/*movable-box*/&& other)
noexcept(std::is_nothrow_move_constructible_v<T>)
{
if (this != std::addressof(other))
if (other)
emplace(std::move(*other));
else
reset();
return *this;
}
Otherwise, it is identical to the move assignment operator of `std::optional`.
identical|optional|
2=<!--

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |

-->

## Member functions


| cpp/utility/optional/dsc constructor | (see dedicated page) |
| cpp/utility/optional/dsc destructor | (see dedicated page) |
| cpp/utility/optional/dsc operator{{= | (see dedicated page) |

#### Observers

| cpp/utility/optional/dsc operator* | (see dedicated page) |
| cpp/utility/optional/dsc operator bool | (see dedicated page) |
| cpp/utility/optional/dsc value | (see dedicated page) |
| cpp/utility/optional/dsc value_or | (see dedicated page) |

#### Modifiers

| cpp/utility/optional/dsc swap | (see dedicated page) |
| cpp/utility/optional/dsc reset | (see dedicated page) |
| cpp/utility/optional/dsc emplace | (see dedicated page) |


## Notes

A <sup>(until C++23)</sup> <sup>(since C++23)</sup>  does not contain a value only if
* `T` does not model  or , and an exception is thrown on move assignment or copy assignment respectively, or
* it is initialized/assigned from another valueless wrapper.
Before `P2325R3`, the wrapper was called `''semiregular-box''` in the standard and always satisfied , as the default constructor was always provided (which might construct a valueless wrapper).

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3572 | C++20 | conditionally different assignment operators were not constexpr | made constexpr |


## See also


| cpp/ranges/dsc single_view | (see dedicated page) |
| cpp/ranges/dsc repeat_view | (see dedicated page) |
| cpp/ranges/dsc filter_view | (see dedicated page) |
| cpp/ranges/dsc transform_view | (see dedicated page) |
| cpp/ranges/dsc take_while_view | (see dedicated page) |
| cpp/ranges/dsc drop_while_view | (see dedicated page) |
| cpp/ranges/dsc zip_transform_view | (see dedicated page) |
| cpp/ranges/dsc adjacent_transform_view | (see dedicated page) |

