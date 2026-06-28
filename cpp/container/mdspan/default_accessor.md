---
title: std::default_accessor
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/default_accessor
---

ddcl|header=mdspan|since=c++23|1=
template< class ElementType >
class default_accessor;
A specialization of `std::default_accessor` class template is the default *AccessorPolicy* used by `std::mdspan` if no user-specified accessor policy is provided.
Each specialization of `default_accessor` models  and is *TriviallyCopyable*.

## Template parameters


### Parameters

- `ElementType` - the element type. Shall be a complete object type that is neither an abstract class type nor an array type. Otherwise, the program is ill-formed

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions

member|default_accessor|2=

```cpp
dcl|num=1|1=
constexpr default_accessor() noexcept = default;
dcl|num=2|1=
template< class OtherElementType >
constexpr default_accessor( default_accessor<OtherElementType> ) noexcept {}
```

1. Default constructs a `default_accessor`.
2. Constructs a `default_accessor` from `default_accessor<OtherElementType>`. The constructor has no visible effect. This overload participates in overload resolution only if `std::is_convertible_v<OtherElementType(*)[], element_type(*)[]>` is true.
member|access|2=

```cpp
dcl|1=
constexpr reference access( data_handle_type p, std::size_t i ) const noexcept;
```

Equivalent to `return p[i];`.
member|offset|2=

```cpp
dcl|1=
constexpr data_handle_type offset( data_handle_type p, std::size_t i ) const noexcept;
```

Equivalent to `return p + i;`.

## Example

