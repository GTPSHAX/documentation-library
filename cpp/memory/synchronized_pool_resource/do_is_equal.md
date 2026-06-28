---
title: std::pmr::synchronized_pool_resource::do_is_equal
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/synchronized_pool_resource/do_is_equal
---

ddcl|since=c++17|1=
virtual bool do_is_equal( const std::pmr::memory_resource& other ) const noexcept;
Compare `*this` with `other` for identity - memory allocated using a `synchronized_pool_resource` can only be deallocated using that same resource.

## Return value

`1=this == &other`

## Defect report


## See also


| cpp/memory/memory_resource/dsc do_is_equal | (see dedicated page) |

