---
title: std::basic_common_reference<std::reference_wrapper>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/reference_wrapper/basic_common_reference
---


# basic_common_referencesmall|<std::reference_wrapper>


```cpp
**Header:** `<`functional`>`
dcla|num=1|since=c++23|1=
template< class R, class T,
template<class> RQual, template<class> TQual >
requires (/*ref-wrap-common-reference-exists-with*/<R, T, RQual<R>, TQual<T>> &&
!/*ref-wrap-common-reference-exists-with*/<T, R, TQual<T>, RQual<R>>)
struct basic_common_reference<R, T, RQual, TQual>;
dcl|num=2|since=c++23|1=
template< class T, class R,
template<class> TQual, template<class> RQual >
requires (/*ref-wrap-common-reference-exists-with*/<R, T, RQual<R>, TQual<T>> &&
!/*ref-wrap-common-reference-exists-with*/<T, R, TQual<T>, RQual<R>>)
struct basic_common_reference<T, R, TQual, RQual>;
|1=
template< class R, class T, class RQ, class TQ >
concept /*ref-wrap-common-reference-exists-with*/ =
/*is-ref-wrapper*/<R> &&
requires { typename std::common_reference_t<typename R::type&, TQ>; } &&
std::convertible<RQ, std::common_reference_t<typename R::type&, TQ>>;
```

The common reference type of a `reference_wrapper` (denoted as `R`) and a type `T`, correspondingly applied with cv and reference qualifiers (denoted as `RQ` and `TQ` respectively), is equivalent to a common reference type of underlying type of `R` applied with lvalue reference and the `TQ`.
The common reference type is defined only if `R` is the only `reference_wrapper`, the underlying type of `R` applied with lvalue reference and the `TQ` have a common reference type to which `RQ` must be convertible.
The exposition-only constant `/*is-ref-wrapper*/<R>` is `true` if and only if `R` is a specialization of `std::reference_wrapper`.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Notes


## Example


### Example

```cpp
#include <concepts>
#include <functional>

static_assert(std::same_as<std::common_reference_t<int&,
                                                   std::reference_wrapper<int>>,
                                                   int&>);
static_assert(std::same_as<std::common_reference_t<std::reference_wrapper<int>&,
                                                   int&>,
                                                   int&>);
static_assert(std::same_as<std::common_reference_t<int&,
                                                   const std::reference_wrapper<int>&>,
                                                   int&>);
int main() {}
```


## See also


| cpp/types/dsc common_reference | (see dedicated page) |

