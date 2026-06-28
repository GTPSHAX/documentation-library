---
title: std::ranges::lazy_split_view::outer_iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/lazy_split_view/outer_iterator
---

ddcla|since=c++20|expos=yes|
template< bool Const >
struct /*outer_iterator*/;
The return type of `lazy_split_view::begin`, and of `lazy_split_view::end` when the underlying view is a  and .
If either `V` or `Pattern` is not a simple view (e.g. if `ranges::iterator_t<const V>` is invalid or different from `ranges::iterator_t<V>`), `Const` is `true` for iterators returned from the const overloads, and `false` otherwise. If `V` is a simple view, `Const` is `true` if and only if `V` is a .

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |
| dsc|`iterator_concept`| | |
| * `std::forward_iterator_tag`, if  models , | |
| * `std::input_iterator_tag`, otherwise | |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


## Member functions

member|''outer_iterator''|2=

```cpp
dcl|num=1|since=c++20|1=
/*outer_iterator*/() = default;
dcl|num=2|since=c++20|
constexpr explicit /*outer_iterator*/( Parent& parent )
requires (!ranges::forward_range<Base>);
dcl|num=3|since=c++20|
constexpr /*outer_iterator*/( Parent& parent,
ranges::iterator_t<Base> current )
requires ranges::forward_range<Base>;
dcla|num=4|anchor=ctor4|since=c++20|
constexpr /*outer_iterator*/( /*outer_iterator*/<!Const> i )
requires Const && std::convertible_to<ranges::iterator_t<V>,
ranges::iterator_t<Base>>;
```

1. Value initializes the non-static data members with their default member initializer, that is:
* `1=parent_ = nullptr;`,
* `1=current_ = iterator_t<Base>();` (present only if `V` models ),
2. Initializes  with `std::addressof(parent)`.
3. Initializes  with `std::addressof(parent)` and  with `std::move(current)`.
4. Initializes  with `i.parent_`,  with `std::move(i.current_)`, and  with `t.trailing_empty_`.
The  is initialized with its default member initializer to `false`.
member|operator*|2=
ddcl|since=c++20|
constexpr value_type operator*() const;
Equivalent to }.
member|operator++|2=

```cpp
dcl|num=1|since=c++20|1=
constexpr /*outer_iterator*/& operator++();
dcl|num=2|since=c++20|1=
constexpr decltype(auto) operator++(int);
```

1. The function body is equivalent to

```cpp
const auto end = ranges::end(parent_->base_);
if (/*cur*/() == end)
{
    trailing_empty_ = false;
    return *this;
}
const auto [pbegin, pend] = ranges::subrange{parent_->pattern_};
if (pbegin == pend)
    ++/*cur*/();
else if constexpr (/*tiny_range*/<Pattern>)
{
    /*cur*/() = ranges::find(std::move(/*cur*/()), end, *pbegin);
    if (/*cur*/() != end)
    {
        ++/*cur*/();
        if (/*cur*/() == end)
            trailing_empty_ = true;
    }
}
else
{
    do
    {
        auto [b, p] = ranges::mismatch(/*cur*/(), end, pbegin, pend);
        if (p == pend)
        {
            /*cur*/() = b;
            if (/*cur*/() == end)
                trailing_empty_ = true;
            break; // The pattern matched; skip it
        }
    } while (++/*cur*/() != end);
}
return *this;
```

2. Equivalent to

```cpp
if constexpr (ranges::forward_range<Base>)
{
    auto tmp = *this;
    ++*this;
    return tmp;
}
else
{
    ++*this; // no return statement
}
```

member|''cur''()|2=

```cpp
dcla|anchor=no|num=1|since=c++20|expos=yes|
constexpr auto& /*cur*/() noexcept;
dcla|anchor=no|num=2|since=c++20|expos=yes|
constexpr auto& /*cur*/() const noexcept;
```

This convenience member function is referred to from `/*outer_iterator*/::operator++()`, from the non-member `1=operator==(const /*outer_iterator*/&, std::default_sentinel_t)`, and from some member functions of the possible implementation of .
@1,2@ Equivalent to

```cpp
if constexpr (ranges::forward_range<V>)
    return current_;
else
    return *parent->current_;
```


## Non-member functions


| nolink=true|operator | |

member|1= operator==<small>(std::ranges::split_view::''outer_iterator'')</small>|2=

```cpp
dcl|num=1|since=c++20|1=
friend constexpr bool operator==( const /*outer_iterator*/& x,
const /*outer_iterator*/& y )
requires forward_range<Base>;
dcl|num=2|since=c++20|1=
friend constexpr bool operator==( const /*outer_iterator*/& x,
std::default_sentinel_t );
```

1. Equivalent to `1=return x.current_ == y.current_ and x.trailing_empty_ == y.trailing_empty_;`.
2. Equivalent to `1=return x./*cur*/() == ranges::end(x.parent_->base_) and !x.trailing_empty_;`.

## Defect reports

