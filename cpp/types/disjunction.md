---
title: std::disjunction
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/disjunction
---

ddcl|header=type_traits|since=c++17|
template< class... B >
struct disjunction;
Forms the [Logical disjunction|logical disjunction](https://en.wikipedia.org/wiki/Logical disjunction|logical disjunction) of the type traits `B...`, effectively performing a logical OR on the sequence of traits.
The specialization `std::disjunction<B1, ..., BN>` has a public and unambiguous base that is
* if `1=sizeof...(B) == 0`, `std::false_type`; otherwise
* the first type `Bi` in `B1, ..., BN` for which `1=bool(Bi::value) == true`, or `BN` if there is no such type.
The member names of the base class, other than `disjunction` and `1=operator=`, are not hidden and are unambiguously available in `disjunction`.
Disjunction is short-circuiting: if there is a template type argument `Bi` with `1=bool(Bi::value) != false`, then instantiating `disjunction<B1, ..., BN>::value` does not require the instantiation of `Bj::value` for `j > i`.

## Template parameters


### Parameters

- `B...` - every template argument `Bi` for which `Bi::value` is instantiated must be usable as a base class and define member `value` that is convertible to `bool`

## Helper variable template


```cpp
dcl|since=c++17|1=
template< class... B >
constexpr bool disjunction_v = disjunction<B...>::value;
```


## Possible implementation

eq fun
|1=
template<class...>
struct disjunction : std::false_type {};
template<class B1>
struct disjunction<B1> : B1 {};
template<class B1, class... Bn>
struct disjunction<B1, Bn...>
: std::conditional_t<bool(B1::value), B1, disjunction<Bn...>>  {};

## Notes

A specialization of `disjunction` does not necessarily inherit from of either `std::true_type` or `std::false_type`: it simply inherits from the first `B` whose `::value`, explicitly converted to `bool`, is `true`, or from the very last `B` when all of them convert to `false`. For example, `std::disjunction<std::integral_constant<int, 2>, std::integral_constant<int, 4>>::value` is `2`.
The short-circuit instantiation differentiates `disjunction` from fold expressions: a fold expression like `(...  instantiates every `B` in `Bs`, while `std::disjunction_v<Bs...>` stops instantiation once the value can be determined. This is particularly useful if the later type is expensive to instantiate or can cause a hard error when instantiated with the wrong type.

## Example


## See also


| cpp/types/dsc negation | (see dedicated page) |
| cpp/types/dsc conjunction | (see dedicated page) |

