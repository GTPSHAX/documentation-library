---
title: std::is_base_of
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_base_of
---

ddcl|header=type_traits|since=c++11|1=
template< class Base, class Derived >
struct is_base_of;
`std::is_base_of` is a *BinaryTypeTrait*.
If `Derived` is derived from `Base` or if both are the same non-union class (in both cases ignoring cv-qualification), provides the member constant `value` equal to `true`. Otherwise `value` is `false`.
If both `Base` and `Derived` are non-union class types, and they are not the same type (ignoring cv-qualification), `Derived` should be a complete type; otherwise the behavior is undefined.

## Helper variable template

ddcl|since=c++17|1=
template< class Base, class Derived >
constexpr bool is_base_of_v = is_base_of<Base, Derived>::value;

## Notes

`std::is_base_of<A, B>::value` is `true` even if `A` is a private, protected, or ambiguous base class of `B`. In many situations, `std::is_convertible<B*, A*>` is the more appropriate test.
Although no class is its own base, `std::is_base_of<T, T>::value` is true because the intent of the trait is to model the "is-a" relationship, and `T` is a `T`. Despite that, `std::is_base_of<int, int>::value` is `false` because only classes participate in the relationship that this trait models.

## Possible Implementation

eq fun|1=
namespace details
{
template<typename B>
std::true_type test_ptr_conv(const volatile B*);
template<typename>
std::false_type test_ptr_conv(const volatile void*);
template<typename B, typename D>
auto test_is_base_of(int) -> decltype(test_ptr_conv<B>(static_cast<D*>(nullptr)));
template<typename, typename>
auto test_is_base_of(...) -> std::true_type; // private or ambiguous base
}
template<typename Base, typename Derived>
struct is_base_of :
std::integral_constant<
bool,
std::is_class<Base>::value &&
std::is_class<Derived>::value &&
decltype(details::test_is_base_of<Base, Derived>(0))::value
> {};

## Example


### Example

```cpp
#include <type_traits>

class A {};
class B : A {};
class C : B {};
class D {};
union E {};
using I = int;

static_assert
(
    std::is_base_of_v<A, A> == true &&
    std::is_base_of_v<A, B> == true &&
    std::is_base_of_v<A, C> == true &&
    std::is_base_of_v<A, D> != true &&
    std::is_base_of_v<B, A> != true &&
    std::is_base_of_v<E, E> != true &&
    std::is_base_of_v<I, I> != true
);

int main() {}
```


## Defect reports


## See also


| cpp/types/dsc is_virtual_base_of | (see dedicated page) |
| cpp/types/dsc is_convertible | (see dedicated page) |
| cpp/concepts/dsc derived_from | (see dedicated page) |

