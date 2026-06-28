---
title: std::generator::iterator
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/generator/iterator
---


# small|generator<Ref,V,Allocator>::

''iterator''
ddcla|expos=yes|
class /*iterator*/;
The return type of `generator::begin`. Models  and .

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions

member|''iterator''|2=
ddcl|since=c++23|
/*iterator*/( /*iterator*/&& other ) noexcept;
Initializes  with }.
member|1=operator=|2=
ddcl|since=c++23|1=
/*iterator*/& operator=( /*iterator*/&& other ) noexcept;
Equivalent to }.
Returns: `*this`.
member|operator*|2=
ddcl|since=c++23|
reference operator*() const
noexcept( std::is_nothrow_copy_constructible_v<reference> );
# Let  be the `std::generator`'s underlying type.
# Let for some generator object `x` its  be in the stack `*x.active_`.
# Let `x.active_->top()` refer to a suspended coroutine with promise object `p`.
Equivalent to `return static_cast<reference>(*p.value_);`.
member|operator++|2=

```cpp
dcl|since=c++23|num=1|
constexpr /*iterator*/& operator++();
dcl|since=c++23|num=2|
constexpr void operator++( int );
```

1. Let for some generator object `x` the  be in the stack `*x.active_`.
@@ Equivalent to `x.active_->top().resume()`.
@@ Returns: `*this`.
2. Equivalent to `++*this;`.

## Non-member functions


| #compare|title=operator | |

member|1=operator==|2=
ddcl|since=c++23|1=
friend bool operator==( const /*iterator*/& i, std::default_sentinel_t );
Equivalent to `return i.coroutine_.done();`.

## Example

