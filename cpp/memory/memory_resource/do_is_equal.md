---
title: std::pmr::memory_resource::do_is_equal
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/memory_resource/do_is_equal
---

ddcl|since=c++17|1=
virtual bool do_is_equal( const std::pmr::memory_resource& other ) const noexcept = 0;
Compares `*this` for equality with `other`.
Two `memory_resource`s compare equal if and only if memory allocated from one `memory_resource` can be deallocated from the other and vice versa.

## Notes

The most-derived type of `other` may not match the most derived type of `*this`. A derived class implementation therefore must typically check whether the most derived types of `*this` and `other` match using `cpp/language/dynamic_cast|dynamic_cast`, and immediately return `false` if the cast fails.

## See also


| cpp/memory/memory_resource/dsc is_equal | (see dedicated page) |

