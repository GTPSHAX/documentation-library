---
title: std::pmr::polymorphic_allocator::construct
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/polymorphic_allocator/construct
---


```cpp
dcl|since=c++17|num=1|
template< class U, class... Args >
void construct( U* p, Args&&... args );
dcl|since=c++17|until=c++20|num=2|
template< class T1, class T2, class... Args1, class... Args2 >
void construct( std::pair<T1, T2>* p,
std::piecewise_construct_t,
std::tuple<Args1...> x,
std::tuple<Args2...> y );
dcl|since=c++17|until=c++20|num=3|
template< class T1, class T2 >
void construct( std::pair<T1, T2>* p );
dcl|since=c++17|until=c++20|num=4|
template< class T1, class T2, class U, class V >
void construct( std::pair<T1, T2>* p, U&& x, V&& y );
dcl|since=c++17|until=c++20|num=5|
template< class T1, class T2, class U, class V >
void construct( std::pair<T1, T2>* p, const std::pair<U, V>& xy );
dcl|since=c++17|until=c++20|num=6|
template< class T1, class T2, class U, class V >
void construct( std::pair<T1, T2>* p, std::pair<U, V>&& xy );
dcl|num=7|since=c++17|until=c++20|
template< class T1, class T2, class NonPair >
void construct( std::pair<T1, T2>* p, NonPair&& non_pair );
```

Constructs an object in allocated, but not initialized storage pointed to by `p` the provided constructor arguments. If the object is of type that itself uses allocators, or if it is std::pair, passes `*this` down to the constructed object.
1. Creates an object of the given type `U` by means of uses-allocator construction at the uninitialized memory location indicated by *p*, using `*this` as the allocator. <sup>(until C++20)</sup>
rrev|until=c++20|
2. First, if either `T1` or `T2` is allocator-aware, modifies the tuples `x` and `y` to include `this->resource()`, resulting in the two new tuples `xprime` and `yprime`, according to the following three rules:
:@2a@ if `T1` is not allocator-aware (`1=std::uses_allocator<T1, polymorphic_allocator>::value==false`) and `1=std::is_constructible<T1, Args1...>::value==true`, then `xprime` is `x`, unmodified.
:@2b@ if `T1` is allocator-aware (`1=std::uses_allocator<T1, polymorphic_allocator>::value==true`), and its constructor takes an allocator tag (`1=std::is_constructible<T1, std::allocator_arg_t, polymorphic_allocator, Args1...>::value==true`, then `xprime` is
`std::tuple_cat(std::make_tuple(std::allocator_arg, *this), std::move(x))`.
:@2c@ if `T1` is allocator-aware (`1=std::uses_allocator<T1, polymorphic_allocator>::value==true`), and its constructor takes the allocator as the last argument (`1=std::is_constructible<T1, Args1..., polymorphic_allocator>::value==true`), then `xprime` is  `std::tuple_cat(std::move(x), std::make_tuple(*this))`.
:@2d@ Otherwise, the program is ill-formed.
@@Same rules apply to `T2` and the replacement of `y` with `yprime`.
@@Once `xprime` and `yprime` are constructed, constructs the pair `p` in allocated storage as if by `::new((void *) p) pair<T1, T2>(std::piecewise_construct, std::move(xprime), std::move(yprime));`.
3. Equivalent to `construct(p, std::piecewise_construct, std::tuple<>(), std::tuple<>())`, that is, passes the memory resource on to the pair's member types if they accept them.
4. Equivalent to

```cpp
construct(p, std::piecewise_construct, std::forward_as_tuple(std::forward<U>(x)),
                                       std::forward_as_tuple(std::forward<V>(y)))
```

5. Equivalent to

```cpp
construct(p, std::piecewise_construct, std::forward_as_tuple(xy.first),
                                       std::forward_as_tuple(xy.second))
```

6. Equivalent to

```cpp
construct(p, std::piecewise_construct, std::forward_as_tuple(std::forward<U>(xy.first)),
                                       std::forward_as_tuple(std::forward<V>(xy.second)))
```

7. cpp/enable_if|given the exposition-only function template

```cpp
template< class A, class B >
void /*deduce-as-pair*/( const std::pair<A, B>& );
```

, `/*deduce-as-pair*/(non_pair)` is ill-formed when considered as an unevaluated operand. Equivalent to

```cpp
construct<T1, T2, T1, T2>(p, std::forward<NonPair>(non_pair));
```


## Parameters


### Parameters

- `p` - pointer to allocated, but not initialized storage
- `args...` - the constructor arguments to pass to the constructor of `T`
- `x` - the constructor arguments to pass to the constructor of `T1`
- `y` - the constructor arguments to pass to the constructor of `T2`
- `xy` - the pair whose two members are the constructor arguments for `T1` and `T2`
- `non_pair` - non-`pair` argument to convert to `pair` for further construction

## Return value

(none)

## Notes

This function is called (through `std::allocator_traits`) by any allocator-aware object, such as `std::pmr::vector` (or another `std::vector` that was given a `std::pmr::polymorphic_allocator` as the allocator to use).

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2975 | C++17 | first overload is mistakenly used for pair construction in some cases | constrained to not accept pairs |


## See also


| cpp/memory/allocator_traits/dsc construct | (see dedicated page) |
| cpp/memory/allocator/dsc construct | (see dedicated page) |

