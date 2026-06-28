---
title: std::rethrow_if_nested
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/rethrow_if_nested
---

ddcla|header=exception|since=c++11|constexpr=c++26|
template< class E >
void rethrow_if_nested( const E& e );
If `E` is not a polymorphic class type, or if `std::nested_exception` is an inaccessible or ambiguous base class of `E`, there is no effect.
Otherwise, performs

```cpp
if (auto p = dynamic_cast<const std::nested_exception*>(std::addressof(e)))
    p->rethrow_nested();
```


## Parameters


### Parameters

- `e` - the exception object to rethrow

## Notes

Unlike many related functions, this function is ''not'' intended to be called with a `std::exception_ptr` but rather an actual exception reference.

### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_constexpr_exceptions` | 202411L | C++26 | `constexpr` for exception types |


## Possible implementation

eq fun|1=
namespace details
{
template<class E>
struct can_dynamic_cast
: std::integral_constant<bool,
std::is_polymorphic<E>::value &&
(!std::is_base_of<std::nested_exception, E>::value
std::is_convertible<E*, std::nested_exception*>::value)
> {};
template<class T>
void rethrow_if_nested_impl(const T& e, std::true_type)
{
if (auto nep = dynamic_cast<const std::nested_exception*>(std::addressof(e)))
nep->rethrow_nested();
}
template<class T>
void rethrow_if_nested_impl(const T&, std::false_type) {}
}
template<class T>
void rethrow_if_nested(const T& t)
{
details::rethrow_if_nested_impl(t, details::can_dynamic_cast<T>());
}

## Example


## See also


| cpp/error/dsc nested_exception | (see dedicated page) |
| cpp/error/dsc throw_with_nested | (see dedicated page) |

