---
title: std::hash<std::shared_ptr>
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/shared_ptr/hash
---


# hashsmall|<std::shared_ptr>

ddcl|since=c++11|1=
template< class T >
struct hash<std::shared_ptr<T>>;
The template specialization of `std::hash` for `std::shared_ptr<T>` allows users to obtain hashes of objects of type `std::shared_ptr<T>`.
For a given `1=std::shared_ptr<T> p`, this specialization ensures that `1=std::hash<std::shared_ptr<T>>()(p) == std::hash<decltype(p.get())>()(p.get())`.

## Example


## See also


| cpp/utility/dsc hash | (see dedicated page) |

