---
title: std::collate_byname
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/collate_byname
---

ddcl|header=locale|
template< class CharT >
class collate_byname : public std::collate<CharT>;
`std::collate_byname` is a `std::collate` facet which encapsulates locale-specific collation (comparison) and hashing of strings. Just like `std::collate`, it can be imbued in `std::regex` and applied, by means of , directly to all standard algorithms that expect a string comparison predicate.

## Specializations

The standard library is guaranteed to provide the following specializations:


| locale | |


## Member functions


| cpp/locale/byname/dsc constructor|collate_byname | (see dedicated page) |
| cpp/locale/byname/dsc destructor|collate_byname | (see dedicated page) |


## Notes


## Example


## See also


| cpp/locale/dsc collate | (see dedicated page) |
| cpp/string/byte/dsc strcoll | (see dedicated page) |
| cpp/string/wide/dsc wcscoll | (see dedicated page) |
| cpp/locale/locale/dsc operator() | (see dedicated page) |

