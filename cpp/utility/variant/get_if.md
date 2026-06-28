---
title: std::get_if
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variant/get_if
---


# get_if small|(std::variant)


```cpp
**Header:** `<`variant`>`
dcl|since=c++17|num=1|
template< std::size_t I, class... Types >
constexpr std::add_pointer_t<std::variant_alternative_t<I, std::variant<Types...>>>
get_if( std::variant<Types...>* pv ) noexcept;
dcl|since=c++17|num=2|
template< std::size_t I, class... Types >
constexpr std::add_pointer_t<const std::variant_alternative_t<I, std::variant<Types...>>>
get_if( const std::variant<Types...>* pv ) noexcept;
dcl|since=c++17|num=3|
template< class T, class... Types >
constexpr std::add_pointer_t<T>
get_if( std::variant<Types...>* pv ) noexcept;
dcl|since=c++17|num=4|
template< class T, class... Types >
constexpr std::add_pointer_t<const T>
get_if( const std::variant<Types...>* pv ) noexcept;
```

@1,2@ Index-based non-throwing accessor: If `pv` is not a null pointer and `1=pv->index() == I`, returns a pointer to the value stored in the variant pointed to by `pv`. Otherwise, returns a null pointer value. The call is ill-formed if `I` is not a valid index in the variant.
@3,4@ Type-based non-throwing accessor: Equivalent to  with `I` being the zero-based index of `T` in `Types...`. The call is ill-formed if `T` is not a unique element of `Types...`.

## Template parameters


### Parameters

- `I` - index to look up
- `Type` - unique type to look up

## Parameters


### Parameters

- `pv` - pointer to a variant

## Return value

Pointer to the value stored in the pointed-to variant or null pointer on error.

## Example


### Example


**Output:**
```
variant value: 12
failed to get value!
```


## See also


| cpp/utility/variant/dsc get | (see dedicated page) |

