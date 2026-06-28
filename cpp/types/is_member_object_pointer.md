---
title: std::is_member_object_pointer
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_member_object_pointer
---

cpp/types/traits/is| 1=is_member_object_pointer
| description=
Checks whether `T` is a non-static member object pointer. Provides the member constant `value` which is equal to `true`, if `T` is a non-static member object pointer type. Otherwise, `value` is equal to `false`.
| inherit_desc=`T` is a pointer to member object

## Possible implementation

eq fun
| 1=
template<class T>
struct is_member_object_pointer : std::integral_constant<
bool,
std::is_member_pointer<T>::value &&
!std::is_member_function_pointer<T>::value
> {};

## Example


### Example


**Output:**
```
Is member object pointer?
true: int(C::*)
false: int(C::*)()
```


## See also

