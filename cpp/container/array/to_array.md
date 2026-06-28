---
title: std::to_array
type: Containers
source: https://en.cppreference.com/w/cpp/container/array/to_array
---


```cpp
**Header:** `<`array`>`
dcla|num=1|since=c++20|
template< class T, std::size_t N >
constexpr std::array<std::remove_cv_t<T>, N> to_array( T (&a)[N] );
dcla|num=2|since=c++20|
template< class T, std::size_t N >
constexpr std::array<std::remove_cv_t<T>, N> to_array( T (&&a)[N] );
```

Creates a `std::array` from the one dimensional built-in array `a`. Copying or moving multidimensional built-in array is not supported.
1. For every `i` in `0, ..., N - 1`, copy-initializes result's correspond element with `a[i]`. This overload is ill-formed when `std::is_constructible_v<T, T&>` is `false`.
2. For every `i` in `0, ..., N - 1`, move-initializes result's correspond element with `std::move(a[i])`. This overload is ill-formed when `std::is_move_constructible_v<T>` is `false`.
Both overloads are ill-formed when `std::is_array_v<T>` is `true`.

## Parameters


### Parameters

- `a` - the built-in array to be converted the `std::array`

**Type requirements:**

- `T`
- `T`

## Return value

1. }
2. }

## Notes

There are some occasions where class template argument deduction of `std::array` cannot be used while `to_array` is available:
* `to_array` can be used when the element type of the `std::array` is manually specified and the length is deduced, which is preferable when implicit conversion is wanted.
* `to_array` can copy a string literal, while class template argument deduction constructs a `std::array` of a single pointer to its first character.

```cpp
std::to_array<long>({3, 4}); // OK: implicit conversion
// std::array<long>{3, 4};   // error: too few template arguments
std::to_array("foo");        // creates std::array<char, 4>{'f', 'o', 'o', '\0'}
std::array{"foo"};           // creates std::array<const char*, 1>{"foo"}
```


## Possible implementation

eq impl
|title1=to_array (1)|ver1=1|1=
namespace detail
{
template<class T, std::size_t N, std::size_t... I>
constexpr std::array<std::remove_cv_t<T>, N>
to_array_impl(T (&a)[N], std::index_sequence<I...>)
{
return ;
}
}
template<class T, std::size_t N>
constexpr std::array<std::remove_cv_t<T>, N> to_array(T (&a)[N])
{
return detail::to_array_impl(a, std::make_index_sequence<N>{});
}
|title2=to_array (2)|ver2=2|2=
namespace detail
{
template<class T, std::size_t N, std::size_t... I>
constexpr std::array<std::remove_cv_t<T>, N>
to_array_impl(T (&&a)[N], std::index_sequence<I...>)
{
return ;
}
}
template<class T, std::size_t N>
constexpr std::array<std::remove_cv_t<T>, N> to_array(T (&&a)[N])
{
return detail::to_array_impl(std::move(a), std::make_index_sequence<N>{});
}

## Example


## See also


| cpp/experimental/dsc make_array | (see dedicated page) |

