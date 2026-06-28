---
title: std::variant_alternative_t
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variant/variant_alternative
---


```cpp
**Header:** `<`variant`>`
dcl |since=c++17|num=1|
template <std::size_t I, class T>
struct variant_alternative; /* undefined */
dcl |since=c++17|num=2|
template <std::size_t I, class... Types>
struct variant_alternative<I, variant<Types...>>;
dcl |since=c++17|num=3|
template <std::size_t I, class T> class variant_alternative<I, const T>;
dcl |since=c++17|deprecated=c++20|num=3|
template <std::size_t I, class T>
class variant_alternative<I, volatile T>;
template <std::size_t I, class T>
class variant_alternative<I, const volatile T>;
```

Provides compile-time indexed access to the types of the alternatives of the possibly cv-qualified variant, combining cv-qualifications of the variant (if any) with the cv-qualifications of the alternative.
Formally,
2. meets the *TransformationTrait* requirements with a member typedef `type` equal to the type of the alternative with index `I`
3. meets the *TransformationTrait* requirements with a member typedef `type` that names, respectively, `std::add_const_t<std::variant_alternative_t<I,T>>`, `std::add_volatile_t<std::variant_alternative_t<I,T>>`, and `std::add_cv_t<std::variant_alternative_t<I,T>>`

## Member types


## Helper template alias


```cpp
dcl|since=c++17|1=
template <size_t I, class T>
using variant_alternative_t = typename variant_alternative<I, T>::type;
```


## Example


## Defect reports


## See also

