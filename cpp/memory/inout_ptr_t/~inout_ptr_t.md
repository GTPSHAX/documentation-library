---
title: std::inout_ptr_t::~inout_ptr_t
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/inout_ptr_t/~inout_ptr_t
---

ddcla|since=c++23|constexpr=c++26|
~inout_ptr_t();
Resets the adapted `Smart` object by the value of modified `Pointer` object (or the `void*` object if `operator void**()` has been called) and the captured arguments. `release()` may be called on the adapted `Smart` object if it is not called by the constructor.
Let
* `s` denotes the adapted `Smart` object,
* `args` denotes the captured arguments,
* `p` denotes the value of stored `Pointer`, or `static_cast<Pointer>(*operator void**())` if `operator void**` has been called,
* `SP` be
** `Smart::pointer`, if it is valid and denotes a type, otherwise,
** `Smart::element_type*`, if `Smart::element_type` is valid and denotes a type, otherwise,
** `std::pointer_traits<Smart>::element_type*`, if `std::pointer_traits<Smart>::element_type` is valid and denotes a type, otherwise,
** `Pointer`,
* `/*do-release*/` denotes `s.release()` if the `constructor` does not call `release()`, empty otherwise.
If `Smart` is a pointer type, the destructor performs
:`1=s = static_cast<Smart>(p);`, and the program is ill-formed if `sizeof...(Args) > 0`;
otherwise, if `s.reset(static_cast<SP>(p), std::forward<Args>(args)...)` is well-formed, the destructor performs
:};
otherwise, if `std::is_constructible_v<Smart, SP, Args...>` is `true`, the destructor performs
:};
otherwise, the program is ill-formed.

## Notes

The implementation may allocate the storage for the data structure needed for `Smart` (e.g. a control block) on construction, in order to leave non-throwing works to the destructor.
Arguments captured by value are destroyed after resetting.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3897 | C++23 | the destructor did not update a raw pointer to the null value | it does |

