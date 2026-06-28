---
title: std::hash<std::string_view>
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/hash
---


# hashsmall|<std::string_view>

|hash|hash|hash|hash

```cpp
**Header:** `<`string_view`>`
dcl|since=c++17|
template<> struct hash<std::string_view>;
dcl|since=c++17|
template<> struct hash<std::wstring_view>;
dcl|since=c++20|
template<> struct hash<std::u8string_view>;
dcl|since=c++17|
template<> struct hash<std::u16string_view>;
dcl|since=c++17|
template<> struct hash<std::u32string_view>;
```

Template specializations of `std::hash` for the various view classes for hashing views.
These hashes equal the hashes of corresponding `std::basic_string` classes: If S is one of the standard basic_string types, SV is the corresponding string view type, and s is an object of type S, then `std::hash<S>()(s) .

## Example


### Example


**Output:**
```
"A"   #: 6919333181322027406
L"B"  #: 11959850520494268278
u8"C" #: 12432341034569643010
u"D"  #: 312659256970442235
U"E"  #: 18073225910249204957
Arcturus Vega Capella Rigel
```


## See also


| cpp/utility/dsc hash | (see dedicated page) |


| cpp/string/basic_string/dsc hash | (see dedicated page) |

