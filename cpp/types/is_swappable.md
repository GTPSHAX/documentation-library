---
title: std::is_nothrow_swappable
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_swappable
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++17|num=1|1=
template< class T, class U >
struct is_swappable_with;
dcl|since=c++17|num=2|1=
template< class T >
struct is_swappable;
dcl|since=c++17|num=3|1=
template< class T, class U >
struct is_nothrow_swappable_with;
dcl|since=c++17|num=4|1=
template< class T >
struct is_nothrow_swappable;
```

1. If the expressions `swap(std::declval<T>(), std::declval<U>())` and
`swap(std::declval<U>(), std::declval<T>())` are both well-formed in unevaluated context after `using std::swap;` (see *Swappable*), provides the member constant `value` equal `true`. Otherwise, `value` is `false`. Access checks are performed as if from a context unrelated to either type.
2. If `T` is not a referenceable type (i.e., possibly cv-qualified `void` or a function type with a ''cv-qualifier-seq'' or a ''ref-qualifier''), provides a member constant `value` equal to `false`. Otherwise, provides a member constant `value` equal to `std::is_swappable_with<T&, T&>::value`.
3. Same as , but evaluations of both expressions from  are known not to throw exceptions.
4. Same as , but uses `std::is_nothrow_swappable_with`.

## Helper variable templates


```cpp
dcl|since=c++17|1=
template< class T, class U >
inline constexpr bool is_swappable_with_v = is_swappable_with<T, U>::value;
dcl|since=c++17|1=
template< class T >
inline constexpr bool is_swappable_v = is_swappable<T>::value;
dcl|since=c++17|1=
template< class T, class U >
inline constexpr bool is_nothrow_swappable_with_v = is_nothrow_swappable_with<T, U>::value;
dcl|since=c++17|1=
template< class T >
inline constexpr bool is_nothrow_swappable_v = is_nothrow_swappable<T>::value;
```


## Notes

This trait does not check anything outside the immediate context of the swap expressions: if the use of `T` or `U` would trigger template specializations, generation of implicitly-defined special member functions etc, and those have errors, the actual swap may not compile even if `std::is_swappable_with<T, U>::value` compiles and evaluates to `true`.

## Example

