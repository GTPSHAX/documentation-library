---
title: std::ranges::split_view::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/split_view/iterator
---

ddcla|since=c++20|expos=yes|
class /*iterator*/;
The return type of `cpp/ranges/split_view|split_view::begin`. This is a , so it is expected that `V` models at least .

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions

member|''iterator''|2=

```cpp
dcl|since=c++20|num=1|1=
/*iterator*/() = default;
dcl|since=c++20|num=2|1=
constexpr /*iterator*/( split_view& parent, ranges::iterator_t<V> current,
ranges::subrange<ranges::iterator_t<V>> next );
```

1. Value-initializes non-static data members with their default member initializers, that is
* `1=ranges::split_view* parent_ = nullptr;`,
* `1=ranges::iterator_t<V> cur_ = ranges::iterator_t<V>();`,
* `1=ranges::subrange<ranges::iterator_t<V>> next_ = ranges::subrange<ranges::iterator_t<V>>();`, and
* `1=bool trailing_empty_ = false;`.
2. Initializes non-static data members:
* `1=ranges::split_view* parent_ = std::addressof(parent);`,
* `1=ranges::iterator_t<V> cur_ = std::move(current);`,
* `1=ranges::subrange<ranges::iterator_t<V>> next_ = std::move(next);`, and
* `1=bool trailing_empty_ = false;`.
member|base|2=

```cpp
dcl|since=c++20|1=
constexpr const ranges::iterator_t<V> base() const;
```

Equivalent to `return cur_;`.
member|operator*|2=

```cpp
dcl|since=c++20|1=
constexpr value_type operator*() const;
```

Equivalent to }.
member|operator++|2=

```cpp
dcl|since=c++20|num=1|1=
constexpr /*iterator*/& operator++();
dcl|since=c++20|num=2|1=
constexpr void operator++( int );
```

1. Equivalent to<br>c|1=
cur_ = next_.begin();
if (cur_ != ranges::end(parent_->base_))
{
if (cur_ = next_.end(); cur_ == ranges::end(parent_->base_))
{
trailing_empty_ = true;
next_ = {cur_, cur_};
}
else
next_ = parent_->find_next(cur_);
}
else
trailing_empty_ = false;
return *this;
2. Equivalent to `1=auto tmp = *this; ++*this; return tmp;`.

## Non-member functions


| nolink=true|operator | |

member|1=operator==|2=
ddcl|since=c++20|1=
friend constexpr bool operator==( const /*iterator*/& x, const /*iterator*/& y );
Equivalent to `1=return x.cur_ == y.cur_ and x.trailing_empty_ == y.trailing_empty_;`.
