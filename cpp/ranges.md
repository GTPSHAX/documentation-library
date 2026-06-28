---
title: Ranges library
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges
---


# Ranges library mark since c++20

The ranges library is an extension and generalization of the algorithms and iterator libraries that makes them more powerful by making them composable and less error-prone.
The library creates and manipulates range ''views'', lightweight objects that indirectly represent iterable sequences (''ranges''). Ranges are an abstraction on top of
*  &ndash; iterator pairs, e.g. ranges made by implicit conversion from containers. All algorithms that take iterator pairs now have overloads that accept ranges (e.g. `cpp/algorithm/ranges/sort|ranges::sort`)
*  &ndash; counted sequences, e.g. range returned by `cpp/ranges/view_counted|views::counted`
*  &ndash; conditionally-terminated sequences, e.g. range returned by `cpp/ranges/take_while_view|views::take_while`
*  &ndash; unbounded sequences, e.g. range returned by `cpp/ranges/iota_view|views::iota`
The ranges library includes range algorithms, which are applied to ranges eagerly, and , which are applied to views lazily. Adaptors can be composed into pipelines, so that their actions take place as the view is iterated.
ddcl|header=ranges|since=c++20|1=
namespace std {
namespace views = ranges::views;
}
The namespace alias `std::views` is provided as a shorthand for `std::ranges::views`.


| std::ranges | |

#### Range access

| ranges | |
| iterator | |
| cpp/ranges/dsc begin | (see dedicated page) |
| cpp/ranges/dsc end | (see dedicated page) |
| cpp/ranges/dsc cbegin | (see dedicated page) |
| cpp/ranges/dsc cend | (see dedicated page) |
| cpp/ranges/dsc rbegin | (see dedicated page) |
| cpp/ranges/dsc rend | (see dedicated page) |
| cpp/ranges/dsc crbegin | (see dedicated page) |
| cpp/ranges/dsc crend | (see dedicated page) |
| cpp/ranges/dsc reserve_hint | (see dedicated page) |
| cpp/ranges/dsc size | (see dedicated page) |
| cpp/ranges/dsc ssize | (see dedicated page) |
| cpp/ranges/dsc empty | (see dedicated page) |
| cpp/ranges/dsc data | (see dedicated page) |
| cpp/ranges/dsc cdata | (see dedicated page) |

#### Range primitives

| ranges | |
| cpp/ranges/dsc iterator_t | (see dedicated page) |
| cpp/ranges/dsc range_size_t | (see dedicated page) |
| cpp/ranges/dsc range_reference_t | (see dedicated page) |

#### Dangling iterator handling

| ranges | |
| cpp/ranges/dsc dangling | (see dedicated page) |
| cpp/ranges/dsc borrowed_iterator_t | (see dedicated page) |

#### Other utilities

| ranges | |
| cpp/ranges/dsc elements_of | (see dedicated page) |

#### Range concepts

| ranges | |
| cpp/ranges/dsc range | (see dedicated page) |
| cpp/ranges/dsc borrowed_range | (see dedicated page) |
| cpp/ranges/dsc approximately_sized_range | (see dedicated page) |
| cpp/ranges/dsc sized_range | (see dedicated page) |
| cpp/ranges/dsc view | (see dedicated page) |
| cpp/ranges/dsc input_range | (see dedicated page) |
| cpp/ranges/dsc output_range | (see dedicated page) |
| cpp/ranges/dsc forward_range | (see dedicated page) |
| cpp/ranges/dsc bidirectional_range | (see dedicated page) |
| cpp/ranges/dsc random_access_range | (see dedicated page) |
| cpp/ranges/dsc contiguous_range | (see dedicated page) |
| cpp/ranges/dsc common_range | (see dedicated page) |
| cpp/ranges/dsc viewable_range | (see dedicated page) |
| cpp/ranges/dsc constant_range | (see dedicated page) |
| cpp/ranges/dsc sized-random-access-range | (see dedicated page) |

#### Range conversions

| ranges | |
| cpp/ranges/dsc to | (see dedicated page) |

#### Views

| ranges | |
| cpp/ranges/dsc view_interface | (see dedicated page) |
| cpp/ranges/dsc subrange | (see dedicated page) |


## Range factories


| ranges | |
| std::ranges | |
| cpp/ranges/dsc empty_view | (see dedicated page) |
| cpp/ranges/dsc single_view | (see dedicated page) |
| cpp/ranges/dsc iota_view | (see dedicated page) |
| cpp/ranges/dsc views indices | (see dedicated page) |
| cpp/ranges/dsc repeat_view | (see dedicated page) |
| cpp/ranges/dsc basic_istream_view | (see dedicated page) |


## Range adaptors


| ranges | |
| std::ranges | |
| cpp/ranges/dsc range_adaptor_closure | (see dedicated page) |
| cpp/ranges/dsc all_view | (see dedicated page) |
| cpp/ranges/dsc ref_view | (see dedicated page) |
| cpp/ranges/dsc owning_view | (see dedicated page) |
| cpp/ranges/dsc as_rvalue_view | (see dedicated page) |
| cpp/ranges/dsc filter_view | (see dedicated page) |
| cpp/ranges/dsc transform_view | (see dedicated page) |
| cpp/ranges/dsc take_view | (see dedicated page) |
| cpp/ranges/dsc take_while_view | (see dedicated page) |
| cpp/ranges/dsc drop_view | (see dedicated page) |
| cpp/ranges/dsc drop_while_view | (see dedicated page) |
| cpp/ranges/dsc join_view | (see dedicated page) |
| cpp/ranges/dsc join_with_view | (see dedicated page) |
| cpp/ranges/dsc lazy_split_view | (see dedicated page) |
| cpp/ranges/dsc split_view | (see dedicated page) |
| cpp/ranges/dsc concat_view | (see dedicated page) |
| cpp/ranges/dsc view_counted | (see dedicated page) |
| cpp/ranges/dsc common_view | (see dedicated page) |
| cpp/ranges/dsc reverse_view | (see dedicated page) |
| cpp/ranges/dsc as_const_view | (see dedicated page) |
| cpp/ranges/dsc elements_view | (see dedicated page) |
| cpp/ranges/dsc keys_view | (see dedicated page) |
| cpp/ranges/dsc values_view | (see dedicated page) |
| cpp/ranges/dsc enumerate_view | (see dedicated page) |
| cpp/ranges/dsc zip_view | (see dedicated page) |
| cpp/ranges/dsc zip_transform_view | (see dedicated page) |
| cpp/ranges/dsc adjacent_view | (see dedicated page) |
| cpp/ranges/dsc views pairwise | (see dedicated page) |
| cpp/ranges/dsc adjacent_transform_view | (see dedicated page) |
| cpp/ranges/dsc views pairwise_transform | (see dedicated page) |
| cpp/ranges/dsc chunk_view | (see dedicated page) |
| cpp/ranges/dsc slide_view | (see dedicated page) |
| cpp/ranges/dsc chunk_by_view | (see dedicated page) |
| cpp/ranges/dsc stride_view | (see dedicated page) |
| cpp/ranges/dsc cartesian_product_view | (see dedicated page) |
| cpp/ranges/dsc cache_latest_view | (see dedicated page) |
| cpp/ranges/dsc as_input_view | (see dedicated page) |


## Range generators <sup>(C++23)</sup>


| generator | |
| std | |
| cpp/ranges/dsc generator | (see dedicated page) |


## Helper items


### Range adaptor objects

See *RangeAdaptorObject* (RAO).

### Range adaptor closure objects

See *RangeAdaptorClosureObject* (RACO).

### Customization point objects

See  (CPO).

### Assignable wrapper

Some range adaptors wrap their elements or function objects with the <sup>(until C++23)</sup> <sup>(since C++23)</sup> . The wrapper augments the wrapped object with assignability when needed.

### Non-propagating cache

Some range adaptors are specified in terms of an exposition-only class template , which behaves almost like `std::optional<T>` (see description for differences).

### Conditionally-`const` type


```cpp
dcla|anchor=maybe-const|expos=yes|1=
template< bool Const, class T >
using /*maybe-const*/ = std::conditional_t<Const, const T, T>;
```

The alias template `/*maybe-const*/` is a shorthand used to conditionally apply a `const` qualifier to the type `T`.

### Integer-like type helper templates


```cpp
dcla|num=1|anchor=make-signed-like-t|expos=yes|1=
template< /*is-integer-like*/ T >
using /*make-signed-like-t*/<T> = /* see description */;
dcla|num=2|anchor=make-unsigned-like-t|expos=yes|1=
template< /*is-integer-like*/ T >
using /*make-unsigned-like-t*/<T> = /* see description */;
dcla|num=3|anchor=to-unsigned-like|expos=yes|
template< /*is-integer-like*/ T >
/*make-unsigned-like-t*/<T> /*to-unsigned-like*/( T t )
{
return static_cast</*make-unsigned-like-t*/<T>>(t);
}
```

1. For an integer-like type `T`:
* If `T` is an integer type, `/*make-signed-like-t*/<T>` is `std::make_signed_t<T>`.
* Otherwise, `/*make-signed-like-t*/<T>` is a corresponding unspecified signed-integer-like type of the same width as `T`.
2. For an integer-like type `T`:
* If `T` is an integer type, `/*make-unsigned-like-t*/<T>` is `std::make_unsigned_t<T>`.
* Otherwise, `/*make-signed-like-t*/<T>` is a corresponding unspecified unsigned-integer-like type of the same width as `T`.
3. Explicitly converts `t` to `/*make-unsigned-like-t*/<T>`.

### Customization point object helpers


```cpp
dcla|num=1|anchor=possibly-const-range|expos=yes|
template< ranges::input_range R >
constexpr auto& /*possibly-const-range*/(R& r) noexcept
{
if constexpr (ranges::input_range<const R>)
return const_cast<const R&>(r);
else
return r;
}
dcla|num=2|anchor=as-const-pointer|expos=yes|
template< class T >
constexpr auto /*as-const-pointer*/( const T* p ) noexcept
{
return p;
}
```

Some range access customization point objects are specified in terms of these exposition-only function templates.
1. `/*possibly-const-range*/` returns the const-qualified version of `r` if `const R` models ; otherwise, returns `r` without any casting.
2. `/*as-const-pointer*/` returns a pointer to object of constant type.

### Range adaptor helpers


```cpp
dcla|num=1|anchor=tuple-transform|expos=yes|
template< class F, class Tuple >
constexpr auto /*tuple-transform*/( F&& f, Tuple&& tuple )
{
return std::apply([&]<class... Ts>(Ts&&... args)
{
return std::tuple<std::invoke_result_t<F&, Ts>...>
(std::invoke(f, std::forward<Ts>(args))...);
}, std::forward<Tuple>(tuple));
}
dcla|num=2|anchor=tuple-for-each|expos=yes|
template< class F, class Tuple >
constexpr void /*tuple-for-each*/( F&& f, Tuple&& tuple )
{
std::apply([&]<class... Ts>(Ts&&... args)
{
(static_cast<void>(std::invoke(f, std::forward<Ts>(args))), ...);
}, std::forward<Tuple>(tuple));
}
dcla|num=3|anchor=as-lvalue|expos=yes|
template< class T >
constexpr T& /*as-lvalue*/( T&& t )
{
return static_cast<T&>(t);
}
```

Some range adaptors are specified in terms of these exposition-only function templates.
1. `/*tuple-transform*/` returns a new tuple constructed by applying `f` to each element of `tuple`.
2. `/*tuple-for-each*/` applies `f` to each element of `tuple` and returns nothing.
3. `/*as-lvalue*/` forwards rvalue `t` as lvalue.

### Helper concepts

Following exposition-only concepts are used for several types, but they are not parts of the interface of standard library.

```cpp
dcla|num=1|anchor=simple-view|expos=yes|1=
template< class R >
concept /*simple-view*/ =
ranges::view<R> && ranges::range<const R> &&
std::same_as<ranges::iterator_t<R>, ranges::iterator_t<const R>> &&
std::same_as<ranges::sentinel_t<R>, ranges::sentinel_t<const R>>;
dcla|num=2|anchor=has-arrow|expos=yes|1=
template< class I >
concept /*has-arrow*/ =
ranges::input_iterator<I> &&
(std::is_pointer_v<I>  requires(const I i) { i.operator->(); });
dcla|num=3|anchor=different-from|expos=yes|1=
template< class T, class U >
concept /*different-from*/ =
!std::same_as<std::remove_cvref_t<T>, std::remove_cvref_t<U>>;
dcla|num=4|anchor=range-with-movable-references|expos=yes|1=
template< class R >
concept /*range-with-movable-references*/ =
ranges::input_range<R> &&
std::move_constructible<ranges::range_reference_t<R>> &&
std::move_constructible<ranges::range_rvalue_reference_t<R>>;
dcla|num=5|anchor=all-random-access|expos=yes|1=
template< bool C, class... Views >
concept /*all-random-access*/ =
(ranges::random_access_range
<std::conditional_t<C, const Views, Views>> && ...);
dcla|num=6|anchor=all-bidirectional|expos=yes|1=
template< bool C, class... Views >
concept /*all-bidirectional*/ =
(ranges::bidirectional_range
<std::conditional_t<C, const Views, Views>> && ...);
dcla|num=7|anchor=all-forward|expos=yes|1=
template< bool C, class... Views >
concept /*all-forward*/ =
(ranges::forward_range
<std::conditional_t<C, const Views, Views>> && ...);
```


## Notes


## Example

std::cout << i << ' ';
std::cout << '\n';
// a traditional "functional" composing syntax:
for (int i : std::views::transform(std::views::filter(ints, even), square))
std::cout << i << ' ';
}
|output=
0 4 16
0 4 16

## Defect reports


## See also

* Iterator library
* Constrained algorithms
