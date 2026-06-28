---
title: std::pmr::memory_resource::is_equal
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/memory_resource/is_equal
---

ddcl|since=c++17|
bool is_equal( const memory_resource& other ) const noexcept;
Compares `*this` for equality with `other`. Two `memory_resource`s compare equal if and only if memory allocated from one `memory_resource` can be deallocated from the other and vice versa.
Equivalent to `return do_is_equal(other);`.

## See also


| cpp/memory/memory_resource/dsc do_is_equal | (see dedicated page) |

