---
title: voidify
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/voidify
---


# ''voidify''

ddcla|expos=yes|constexpr=c++17|
template< class T >
void* /*voidify*/( T& obj ) noexcept;
Returns the address of `obj` (implicitly converted to `void*`).

## Parameters


### Parameters

- `obj` - the object whose address will be taken

## Return value

rev|until=c++11|
`&obj`
rev|since=c++11|
`std::addressof(obj)`

## Notes

This exposition-only function template is introduced by . It is used to describe the effects of specialized `<memory>` algorithms. The result pointer is used as the *placement-params* of a placement `new` expression.
Initially, the return value was `const_cast<void*>(static_cast<const volatile void*>(std::addressof(obj)))`, which breaks const-correctness. The explicit casts were removed by the resolution of , and the only conversion left is the implicit conversion to `void*`.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3870 | C++98 | the explicit casts broke const-correctness | removed these casts |


## See also


| cpp/memory/dsc construct_at | (see dedicated page) |
| cpp/memory/dsc uninitialized_copy | (see dedicated page) |
| cpp/memory/dsc uninitialized_copy_n | (see dedicated page) |
| cpp/memory/dsc uninitialized_fill | (see dedicated page) |
| cpp/memory/dsc uninitialized_fill_n | (see dedicated page) |
| cpp/memory/dsc uninitialized_move | (see dedicated page) |
| cpp/memory/dsc uninitialized_move_n | (see dedicated page) |
| cpp/memory/dsc uninitialized_default_construct | (see dedicated page) |
| cpp/memory/dsc uninitialized_default_construct_n | (see dedicated page) |
| cpp/memory/dsc uninitialized_value_construct | (see dedicated page) |
| cpp/memory/dsc uninitialized_value_construct_n | (see dedicated page) |

