---
title: std::ranges::lazy_split_view::inner_iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/lazy_split_view/inner_iterator
---

ddcla|num=1|since=c++20|expos=yes|
template< bool Const >
struct /*inner_iterator*/;
The return type of `lazy_split_view::``::value_type::begin()`.
`Const` matches the template argument of .

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |
| dsc|`iterator_concept`| | |
| * `<Const>::iterator_concept`, that is `std::forward_iterator_tag`, if  models . | |
| * `std::input_iterator_tag`, otherwise. | |
| dsc|`iterator_category`<br>| | |
| Present only if  models . | |
| * `std::forward_iterator_tag` if `std::iterator_traits<ranges::iterator_t<Base>>::iterator_category` models `std::derived_from<std::forward_iterator_tag>`. | |
| * `std::iterator_traits<ranges::iterator_t<Base>>::iterator_category` otherwise. | |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


## Member functions

member|''inner_iterator''|2=

```cpp
dcl|num=1|since=c++20|1=
/*inner_iterator*/() = default;
dcl|num=2|since=c++20|
constexpr explicit /*inner_iterator*/( /*outer_iterator*/<Const> i );
```

1. Value initializes data member  via its default member initializer (= `/*outer_iterator*/<Const>()`).
2. Initializes  with `std::move(i)`.
The data member  is initialized with its default member initializer to `false`.
member|''base''|2=

```cpp
dcl|num=1|since=c++20|1=
constexpr const ranges::iterator_t<Base>& base() const & noexcept;
dcl|num=2|since=c++20|
constexpr ranges::iterator_t<Base> base() &&
requires ranges::forward_range<V>;
```

Returns a copy of the underlying iterator.
1. Copy constructs the result from the underlying iterator. Equivalent to `return i_./*cur*/();`.
2. Move constructs the result from the underlying iterator. Equivalent to `return std::move(i_./*cur*/());`.
member|operator*|2=
ddcl|since=c++20|
constexpr decltype(auto) operator*() const;
Returns the element the underlying iterator points to.
Equivalent to `return *i_./*cur*/();`.
member|operator++|2=

```cpp
dcl|num=1|since=c++20|1=
constexpr /*inner_iterator*/& operator++();
dcl|num=2|since=c++20|1=
constexpr decltype(auto) operator++(int);
```

1. The function body is equivalent to<br>c|1=
incremented_ = true;
if constexpr (!ranges::forward_range<Base>)
{
if constexpr (Pattern::size() == 0)
return *this;
}
++i_./*cur*/();
return *this;
2. Equivalent to<br>c|1=
if constexpr (ranges::forward_range<Base>)
{
auto tmp = *this;
++*this;
return tmp;
}
else
++*this; // no return statement

## Non-member functions


| nolink=true|operator | |
| nolink=true|iter_move|casts the result of dereferencing the underlying iterator to its associated rvalue reference type|notes= | |
| nolink=true|iter_swap|swaps the objects pointed to by two underlying iterators|notes= | |

member|1= operator==|2=

```cpp
dcl|num=1|since=c++20|1=
friend constexpr bool operator==( const /*inner_iterator*/& x,
const /*inner_iterator*/& y )
requires forward_range<Base>;
dcl|num=2|since=c++20|1=
friend constexpr bool operator==( const /*inner_iterator*/& x,
std::default_sentinel_t );
```

1. Equivalent to `1=return x.i_./*cur*/() == y.i_./*cur*/();`.
2. The function body is equivalent to

```cpp
auto [pcur, pend] = ranges::subrange{x.i_.parent_->pattern_};
auto end = ranges::end(x.i_.parent_->base_);
if constexpr (/*tiny_range*/<Pattern>)
{
    const auto& cur = x.i_./*cur*/();
    if (cur == end)
        return true;
    if (pcur == pend)
        return x.incremented_;
    return *cur == *pcur;
}
else
{
    auto cur = x.i_./*cur*/();
    if (cur == end)
        return true;
    if (pcur == pend)
        return x.incremented_;
    do
    {
        if (*cur != *pcur)
            return false;
        if (++pcur == pend)
            return true;
    }
    while (++cur != end);
    return false;
}
```

member|1= iter_move|2=
ddcl|since=c++20|
friend constexpr decltype(auto) iter_move( const /*inner_iterator*/& i )
noexcept(noexcept(ranges::iter_move(i.i_./*cur*/())));
Equivalent to `1=return ranges::iter_move(i.i_./*cur*/());`.
member|1= iter_swap|2=
ddcl|since=c++20|
friend constexpr void iter_swap( const /*inner_iterator*/& x,
const /*inner_iterator*/& y )
noexcept(noexcept(ranges::iter_swap(x.i_.current, y.i_.current)))
requires std::indirectly_swappable<ranges::iterator_t<Base>>;
Equivalent to `ranges::iter_swap(x.i_./*cur*/(), y.i_./*cur*/())`.

## Defect reports

