---
title: std::hash<std::type_index>
type: Utilities
source: https://en.cppreference.com/w/cpp/types/type_index/hash
---

ddcl | header=typeindex | since=c++11 | 1=
template<> struct hash<std::type_index>;
The template specialization of `std::hash` for `std::type_index` allows users to obtain hashes of objects of type `std::type_index`.
The member `operator()` effectively returns the same value as `hash_code()`.

## See also

de:cpp/types/type index/hash
es:cpp/types/type index/hash
fr:cpp/types/type index/hash
it:cpp/types/type index/hash
ja:cpp/types/type index/hash
pt:cpp/types/type index/hash
ru:cpp/types/type index/hash
zh:cpp/types/type index/hash
