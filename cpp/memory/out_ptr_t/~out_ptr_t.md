---
title: std::out_ptr_t::~out_ptr_t
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/out_ptr_t/~out_ptr_t
---

ddcla|since=c++23|constexpr=c++26|
~out_ptr_t();
Resets the adapted `Smart` object by the value of modified `Pointer` object (or the `void*` object if `operator void**()` has been called) and the captured arguments.
Let
* `s` denotes the adapted `Smart` object,
* `args` denotes the captured arguments,
* `p` denotes the value of stored `Pointer`, or `static_cast<Pointer>(*operator void**())` if `operator void**` has been called,
* `SP` be
** `Smart::pointer`, if it is valid and denotes a type, otherwise,
** `Smart::element_type*`, if `Smart::element_type` is valid and denotes a type, otherwise,
** `std::pointer_traits<Smart>::element_type*`, if `std::pointer_traits<Smart>::element_type` is valid and denotes a type, otherwise,
** `Pointer`.
If `s.reset(static_cast<SP>(p), std::forward<Args>(args)...)` is well-formed, the destructor performs
:`if (p) s.reset(static_cast<SP>(p), std::forward<Args>(args)...);`,
otherwise, if `std::is_constructible_v<Smart, SP, Args...>` is `true`, the destructor performs
:`1=if (p) s = Smart(static_cast<SP>(p), std::forward<Args>(args)...);`,
otherwise, the program is ill-formed.

## Notes

If `Smart` is a `std::shared_ptr` specialization, the implementation may allocate the storage for the new control block on construction, in order to leave non-throwing works to the destructor.
Arguments captured by value are destroyed after resetting.
