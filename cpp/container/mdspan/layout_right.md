---
title: std::layout_right
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/layout_right
---

ddcl|header=mdspan|since=c++23|
struct layout_right;
`layout_right` is a *LayoutMappingPolicy* which provides a layout mapping where the rightmost extent has stride 1, and strides increase right-to-left as the product of extents.
rev|until=c++26|
`layout_right` is a *TrivialType*.
rev|since=c++26|
`layout_right` is *TriviallyCopyable*, and `std::is_trivially_default_constructible_v<layout_right>` is `true`.
It is the default layout mapping policy used by `std::mdspan` if no user-specified layout is provided.

## Nested class templates


| cpp/container/mdspan/layout_right/dsc mapping | (see dedicated page) |


## See also


| cpp/container/mdspan/dsc layout_right_padded | (see dedicated page) |
| cpp/container/mdspan/dsc layout_left | (see dedicated page) |
| cpp/container/mdspan/dsc layout_stride | (see dedicated page) |

