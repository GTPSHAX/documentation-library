---
title: std::ranges::to
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/to
---


```cpp
**Header:** `<`ranges`>`
dcla|num=1|since=c++23|
template< class C, ranges::input_range R, class... Args >
requires (!ranges::view<C>)
constexpr C to( R&& r, Args&&... args );
dcl|num=2|since=c++23|
template< template< class... > class C,
ranges::input_range R, class... Args >
constexpr auto to( R&& r, Args&&... args );
dcla|num=3|since=c++23|
template< class C, class... Args >
requires (!ranges::view<C>)
constexpr /*range adaptor closure*/ to( Args&&... args );
dcl|num=4|since=c++23|
template< template< class... > class C, class... Args >
constexpr /*range adaptor closure*/ to( Args&&... args );
dcla|num=5|expos=yes|anchor=reservable-container|1=
template< class Container >
constexpr bool /*reservable-container*/ =
ranges::sized_range<Container> &&
requires (Container& c, ranges::range_size_t<Container> n)
{
c.reserve(n);
{ c.capacity() } -> std::same_as<decltype(n)>;
{ c.max_size() } -> std::same_as<decltype(n)>;
};
dcla|num=6|expos=yes|anchor=container-appendable|1=
template< class Container, class Reference >
constexpr bool /*container-appendable*/ =
requires (Container& c, Reference&& ref)
{
requires
(
requires { c.emplace_back(std::forward<Reference>(ref)); }
requires { c.push_back(std::forward<Reference>(ref)); }
requires { c.emplace(c.end(), std::forward<Reference>(ref)); }
requires { c.insert(c.end(), std::forward<Reference>(ref)); }
);
};
dcla|num=7|expos=yes|anchor=container-appender|1=
template< class Reference, class C >
constexpr auto /*container-appender*/( C& c );
dcla|num=8|expos=yes|anchor=container-compatible-range|1=
template< class R, class T >
concept /*container-compatible-range*/ =
ranges::input_range<R> &&
std::convertible_to<ranges::range_reference_t<R>, T>;
```

The overloads of the range conversion function construct a new non-view object from a source range as its first argument by calling a constructor taking a range, a `std::from_range_t` tagged ranged constructor, a constructor taking an iterator-sentinel pair, or by back inserting each element of the source range into the arguments-constructed object.
1. Constructs an object of type `C` from the elements of `r` in the following:
:@a@ If `C` does not satisfy  or `std::convertible_to<ranges::range_reference_t<R>, ranges::range_value_t<C>>` is `true`:
::@1@ Constructing a non-view object as if direct-initializing (but not direct-list-initializing) an object of type `C` from the source range `std::forward<R>(r)` and the rest of the functional arguments `std::forward<Args>(args)...` if `std::constructible_from<C, R, Args...>` is `true`.
::@2@ Otherwise, constructing a non-view object as if direct-initializing (but not direct-list-initializing) an object of type `C` from additional disambiguation tag `std::from_range`, the source range `std::forward<R>(r)` and the rest of the functional arguments `std::forward<Args>(args)...` if `std::constructible_from<C, std::from_range_t, R, Args...>` is `true`.
::@3@ Otherwise, constructing a non-view object as if direct-initializing (but not direct-list-initializing) an object of type `C` from the iterator-sentinel pair (`ranges::begin(r)` as an iterator and `ranges::end(r)` as sentinel, where iterator and sentinel have the same type. In other words, the source range must be a common range), and the rest of function arguments `std::forward<Args>(args)...` if all of the conditions below are `true`:
* `ranges::common_range<R>`
* If `std::iterator_traits<ranges::iterator_t<R>>::iterator_category` is valid and denotes a type that satisfies `std::derived_from<std::input_iterator_tag>`
* `std::constructible_from<C, ranges::iterator_t<R>, ranges::sentinel_t<R>, Args...>`
::@4@ Otherwise, constructing a non-view range object as if direct-initializing (but not direct-list-initializing) an object of type `C` from the rest of the function arguments `std::forward<Args>(args)...` with the following equivalent call below after the construction:
rrev multi|until1=c++26|rev1=
box|
`if constexpr (ranges::sized_range<R> && /*reservable-container*/<C>)`<br />
`c.reserve(static_cast<ranges::range_size_t<C>>(ranges::size(r)));`<br />
`ranges::for_each(r, /*container-appender*/(c));`
|since2=c++26|rev2=
box|
`if constexpr (ranges::approximately_sized_range<R>`<br />
`&& /*reservable-container*/<C>)`<br />
`c.reserve(static_cast<ranges::range_size_t<C>>(ranges::reserve_hint(r)));`<br />
`ranges::for_each(r, /*container-appender*/(c));`
<br />If the `R` satisfies <sup>(until C++26)</sup> <sup>(since C++26)</sup>  and `C` satisfies , the constructed object `c` of type `C` is able to reserve storage with the initial storage size <sup>(until C++26)</sup> `ranges::size(r)`<sup>(since C++26)</sup> `ranges::reserve_hint(r)` to prevent additional allocations during inserting new elements. Each element of `r` is appended to `c`.
The operations above are valid if both of the conditions below are `true`:
* `std::constructible_from<C, Args...>`
*
:@b@ Otherwise, the return expression is equivalent to

```cpp
to<C>(ranges::ref_view(r) {{!
```

{
return to<ranges::range_value_t<C>>(std::forward<decltype(elem)>(elem));
}), std::forward<Args>(args)...)
Which allows nested range constructions within the range if `ranges::input_range<ranges::range_reference_t<C>>` is `true`.
Otherwise, the program is ill-formed.
2. Constructs an object of deduced type from the elements of `r`.
Let `/*input-iterator*/` be an exposition only type that satisfies *InputIterator*:

```cpp
dcla|anchor=no|expos=yes|1=
struct /*input-iterator*/
{
using iterator_category = std::input_iterator_tag;
using value_type = ranges::range_value_t<R>;
using difference_type = std::ptrdiff_t;
using pointer = std::add_pointer_t<ranges::range_reference_t<R>>;
using reference = ranges::range_reference_t<R>;
reference operator*() const;                      // not defined
pointer operator->() const;                       // not defined
/*input-iterator*/& operator++();                 // not defined
/*input-iterator*/ operator++(int);               // not defined
bool operator==(const /*input-iterator*/&) const; // not defined
};
```

Let `/*DEDUCE-EXPR*/` be defined as follows:
* `C(std::declval<R>(), std::declval<Args>()...)`, if that expression is valid.
* Otherwise,
: , if that expression is valid.
* Otherwise,
: , if that expression is valid.
* Otherwise, the program is ill-formed.
The call is equivalent to
.
@3,4@ Returns a perfect forwarding call wrapper that is also a *RangeAdaptorClosureObject*.
5. Is `true` if it satisfies `ranges::sized_range` and is eligible to be reservable.
6. Is `true` if one element of type `Reference` can be appended to `Container` through a member function call `emplace_back`, `push_back`, `emplace` or `insert`.

```cpp
return [&c]<class Reference>(Reference&& ref)
{
    if constexpr (requires { c.emplace_back(std::declval<Reference>()); })
        c.emplace_back(std::forward<Reference>(ref));
    else if constexpr (requires { c.push_back(std::declval<Reference>()); })
        c.push_back(std::forward<Reference>(ref));
    else if constexpr (requires { c.emplace(c.end(),
                                            std::declval<Reference>()); })
        c.emplace(c.end(), std::forward<Reference>(ref));
    else
        c.insert(c.end(), std::forward<Reference>(ref));
};
```

8. Is used in the definition of containers in constructing an input range `R` whose range reference type must be convertible to `T`.

## Parameters


### Parameters

- `r` - a source range object
- `args` - list of the arguments to  construct a range or  bind to the last parameters of range adaptor closure object

**Type requirements:**


## Return value

@1,2@ A constructed non-view object.
@3,4@ A range adaptor closure object of unspecified type, with the following properties:
member| return type|2=

### Member objects

The returned object behaves as if it has no target object, and an `std::tuple` object `tup` constructed with `std::tuple<std::decay_t<Args>...>(std::forward<Args>(args)...)`, except that the returned object's assignment behavior is unspecified and the names are for exposition only.

### Constructors

The return type of `ranges::to`  behaves as if its copy/move constructors perform a memberwise copy/move. It is *CopyConstructible* if all of its member objects (specified above) are , and is *MoveConstructible* otherwise.

### Member function `operator()`

Given an object `G` obtained from an earlier call to `range::to</* see below */>(args...)`, when a glvalue `g` designating `G` is invoked in a function call expression `g(r)`, an invocation of the stored object takes place, as if by
* `ranges::to</* see below */>(r, std::get<Ns>(g.tup)...)`, where
:* `r` is a source range object that must satisfy .
:* `Ns` is an integer pack `0, 1, ..., (sizeof...(Args) - 1)`.
:* `g` is an lvalue in the call expression if it is an lvalue in the call expression, and is an rvalue otherwise. Thus `std::move(g)(r)` can move the bound arguments into the call, where `g(r)` would copy.
:* The specified template argument is  `C` or  the deduced type from a class template `C` that must not satisfy .
The program is ill-formed if `g` has volatile-qualified type.

## Exceptions

Only throws if construction of a non-view object throws.

## Notes

The insertion of elements into the container may involve copy which can be less efficient than move because lvalue references are produced during the indirection call. Users can opt-in to use `views::as_rvalue` to adapt the range in order for their elements to always produce an rvalue reference during the indirection call which implies move.
The parentheses are mandatory when using the pipe syntax.

```cpp
auto vec = r {{!
```

auto vec = r | std::ranges::to<std::vector>(); // OK

## Example


### Example

```cpp
#include <boost/container/devector.hpp>
#include <concepts>
#include <initializer_list>
#include <list>
#include <print>
#include <ranges>
#include <regex>
#include <string>
#include <vector>

int main()
{
    auto vec = std::views::iota(1, 5)
             {{!
```

| std::ranges::to<std::vector>();
static_assert(std::same_as<decltype(vec), std::vector<int>>);
std::println("1) {}", vec);
auto list = vec | std::views::take(3) | std::ranges::to<std::list<double>>();
std::println("2) {}", list);
}
void ctor_demos()
{
// 1.a.1) Direct init
{
char array[]{'a', 'b', '\0', 'c'};
// Argument type is convertible to result value type:
auto str_to = std::ranges::to<std::string>(array);
// Equivalent to
std::string str(array);
// Result type is not an input range:
auto re_to = std::ranges::to<std::regex>(array);
// Equivalent to
std::regex re(array);
}
// 1.a.2) from_range ctor
{
auto list = {'a', 'b', '\0', 'c'};
// Argument type is convertible to result value type:
auto str_to = std::ranges::to<std::string>(list);
// Equivalent to
// std::string str(std::from_range, list);
// Result type is not an input range:
maybe_unused
auto pair_to = std::ranges::to<std::pair<std::from_range_t, bool>>(true);
// Equivalent to
std::pair<std::from_range_t, bool> pair(std::from_range, true);
}
// 1.a.3) iterator pair ctor
{
auto list = {'a', 'b', '\0', 'c'};
// Argument type is convertible to result value type:
auto devector_to = std::ranges::to<boost::container::devector<char>>(list);
// Equivalent to
boost::container::devector<char> devector(std::ranges::begin(list),
std::ranges::end(list));
// Result type is not an input range:
std::regex re;
auto it_to = std::ranges::to<std::cregex_iterator>(list, re);
// Equivalent to
std::cregex_iterator it(std::ranges::begin(list), std::ranges::end(list), re);
}
}
|output=
1) [2, 4, 6, 8]
2) [2, 4, 6]

## Defect reports


## References

