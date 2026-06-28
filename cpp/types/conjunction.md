---
title: std::conjunction
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/conjunction
---

ddcl|header=type_traits|since=c++17|
template< class... B >
struct conjunction;
Forms the [logical conjunction](https://en.wikipedia.org/wiki/logical conjunction) of the type traits `B...`, effectively performing a logical AND on the sequence of traits.
The specialization `std::conjunction<B1, ..., BN>` has a public and unambiguous base that is
* if `1=sizeof...(B) == 0`, `std::true_type`; otherwise
* the first type `Bi` in `B1, ..., BN` for which `1=bool(Bi::value) == false`, or `BN` if there is no such type.
The member names of the base class, other than `conjunction` and `1=operator=`, are not hidden and are unambiguously available in `conjunction`.
Conjunction is short-circuiting: if there is a template type argument `Bi` with `1= bool(Bi::value) == false`, then instantiating `conjunction<B1, ..., BN>::value` does not require the instantiation of `Bj::value` for `j > i`.

## Template parameters


### Parameters

- `B...` - every template argument `Bi` for which `Bi::value` is instantiated must be usable as a base class and define member `value` that is convertible to `bool`

## Helper variable template

ddcl|since=c++17|1=
template< class... B >
constexpr bool conjunction_v = conjunction<B...>::value;

## Possible implementation

eq fun
|1=
template<class...>
struct conjunction : std::true_type {};
template<class B1>
struct conjunction<B1> : B1 {};
template<class B1, class... Bn>
struct conjunction<B1, Bn...>
: std::conditional_t<bool(B1::value), conjunction<Bn...>, B1> {};

## Notes

A specialization of `conjunction` does not necessarily inherit from either `std::true_type` or `std::false_type`: it simply inherits from the first `B` whose `::value`, explicitly converted to `bool`, is `false`, or from the very last `B` when all of them convert to `true`. For example, `std::conjunction<std::integral_constant<int, 2>, std::integral_constant<int, 4>>::value` is `4`.
The short-circuit instantiation differentiates `conjunction` from fold expressions: a fold expression, like `(... && Bs::value)`, instantiates every `B` in `Bs`, while `std::conjunction_v<Bs...>` stops instantiation once the value can be determined. This is particularly useful if the later type is expensive to instantiate or can cause a hard error when instantiated with the wrong type.

## Example


### Example

```cpp
#include <iostream>
#include <type_traits>

// func is enabled if all Ts... have the same type as T
template<typename T, typename... Ts>
std::enable_if_t<std::conjunction_v<std::is_same<T, Ts>...>>
func(T, Ts...)
{
    std::cout << "All types in pack are the same.\n";
}

// otherwise
template<typename T, typename... Ts>
std::enable_if_t<!std::conjunction_v<std::is_same<T, Ts>...>>
func(T, Ts...)
{
    std::cout << "Not all types in pack are the same.\n";
}

template<typename T, typename... Ts>
constexpr bool all_types_are_same = std::conjunction_v<std::is_same<T, Ts>...>;

static_assert(all_types_are_same<int, int, int>);
static_assert(not all_types_are_same<int, int&, int>);

int main()
{
    func(1, 2, 3);
    func(1, 2, "hello!");
}
```


**Output:**
```
All types in pack are the same.
Not all types in pack are the same.
```


## See also


| cpp/types/dsc negation | (see dedicated page) |
| cpp/types/dsc disjunction | (see dedicated page) |

