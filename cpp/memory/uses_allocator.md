---
title: std::uses_allocator
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/uses_allocator
---

ddcl|header=memory|since=c++11|
template< class T, class Alloc >
struct uses_allocator;
If `T` has a nested type `allocator_type` which is convertible from `Alloc`, the member constant `value` is `true`. Otherwise `value` is `false`.

## Helper variable template

ddcl|since=c++17|1=
template< class T, class Alloc >
constexpr bool uses_allocator_v = uses_allocator<T, Alloc>::value;

## Uses-allocator construction

There are three conventions of passing an allocator `alloc` to a constructor of some type `T`:
* If `T` does not use a compatible allocator (`std::uses_allocator_v<T, Alloc>` is `false`), then `alloc` is ignored.
* Otherwise, `std::uses_allocator_v<T, Alloc>` is `true`, and
:* if `T` uses the ''leading-allocator convention'' (is invocable as `T(std::allocator_arg, alloc, args...)`), then uses-allocator construction uses this form.
:* if `T` uses the ''trailing-allocator convention'' (is invocable as `T(args..., alloc)`), then uses-allocator construction uses this form.
:* Otherwise, the program is ill-formed (this means `std::uses_allocator_v<T, Alloc>` is `true`, but the type does not follow either of the two allowed conventions).
* As a special case, `std::pair` is treated as a uses-allocator type even though `std::uses_allocator` is `false` for pairs (unlike e.g. `std::tuple`): see pair-specific overloads of <sup>(until C++20)</sup> `std::pmr::polymorphic_allocator::construct` and `std::scoped_allocator_adaptor::construct`<sup>(since C++20)</sup> `std::uses_allocator_construction_args`.
rrev|since=c++20|
The utility functions `std::make_obj_using_allocator`, and `std::uninitialized_construct_using_allocator` may be used to explicitly create an object following the above protocol, and `std::uses_allocator_construction_args` can be used to prepare the argument list that matches the flavor of uses-allocator construction expected by the type.

## Specializations

Given a  `T` that does not have a nested `allocator_type`, a program can specialize `std::uses_allocator` to derive from `std::true_type` for `T` if any of the following requirements is satisfied:
* `T` has a constructor which takes `std::allocator_arg_t` as the first argument, and `Alloc` as the second argument.
* `T` has a constructor which takes `Alloc` as the last argument.
In the above, `Alloc` is a type that satisfies *Allocator*.
The following specializations are already provided by the standard library:


| cpp/utility/tuple/dsc uses_allocator | (see dedicated page) |
| cpp/container/dsc uses_allocator|queue | (see dedicated page) |
| cpp/container/dsc uses_allocator|priority_queue | (see dedicated page) |
| cpp/container/dsc uses_allocator|stack | (see dedicated page) |
| cpp/container/dsc uses_allocator|flat_map | (see dedicated page) |
| cpp/container/dsc uses_allocator|flat_set | (see dedicated page) |
| cpp/container/dsc uses_allocator|flat_multimap | (see dedicated page) |
| cpp/container/dsc uses_allocator|flat_multiset | (see dedicated page) |
| cpp/utility/functional/function/dsc uses_allocator | (see dedicated page) |
| cpp/thread/promise/dsc uses_allocator | (see dedicated page) |
| cpp/thread/packaged_task/dsc uses_allocator | (see dedicated page) |


## Notes

This type trait is used by `std::tuple`, `std::scoped_allocator_adaptor`, and `std::pmr::polymorphic_allocator`. It may also be used by custom allocators or wrapper types to determine whether the object or member being constructed is itself capable of using an allocator (e.g. is a container), in which case an allocator should be passed to its constructor.

## See also


| cpp/memory/dsc allocator_arg | (see dedicated page) |
| cpp/memory/dsc uses_allocator_construction_args | (see dedicated page) |
| cpp/memory/dsc make_obj_using_allocator | (see dedicated page) |
| cpp/memory/dsc uninitialized_construct_using_allocator | (see dedicated page) |
| cpp/memory/dsc scoped_allocator_adaptor | (see dedicated page) |

