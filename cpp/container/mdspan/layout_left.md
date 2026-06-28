---
title: std::layout_left
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/layout_left
---

ddcl|header=mdspan|since=c++23|
struct layout_left;
`layout_left` is a *LayoutMappingPolicy* which provides a layout mapping where the leftmost extent has stride 1, and strides increase left-to-right as the product of extents.
rev|until=c++26|
`layout_left` is a *TrivialType*.
rev|since=c++26|
`layout_left` is *TriviallyCopyable*, and `std::is_trivially_default_constructible_v<layout_left>` is `true`.

## Nested class templates


| cpp/container/mdspan/layout_left/dsc mapping | (see dedicated page) |


## See also


| cpp/container/mdspan/dsc layout_left_padded | (see dedicated page) |
| cpp/container/mdspan/dsc layout_right | (see dedicated page) |
| cpp/container/mdspan/dsc layout_stride | (see dedicated page) |

