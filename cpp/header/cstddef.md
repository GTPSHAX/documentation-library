---
title: cstddef
type: Standard headers
source: https://en.cppreference.com/w/cpp/header/cstddef
---

This header is part of the utility library.


| cpp/types/dsc NULL | (see dedicated page) |
| cpp/types/dsc offsetof | (see dedicated page) |
| cpp/types/dsc size_t | (see dedicated page) |
| cpp/types/dsc ptrdiff_t | (see dedicated page) |
| cpp/types/dsc nullptr_t | (see dedicated page) |
| cpp/types/dsc max_align_t | (see dedicated page) |
| cpp/types/dsc byte | (see dedicated page) |
| cpp/types/byte/dsc to_integer | (see dedicated page) |


## Synopsis


```cpp
namespace std {
  using ptrdiff_t = /* see description */;
  using size_t = /* see description */;
  using max_align_t = /* see description */;
  using nullptr_t = decltype(nullptr);

  enum class byte : unsigned char {};

  // byte type operations
  template<class IntType>
    constexpr byte& operator<<=(byte& b, IntType shift) noexcept;
  template<class IntType>
    constexpr byte operator<<(byte b, IntType shift) noexcept;
  template<class IntType>
    constexpr byte& operator>>=(byte& b, IntType shift) noexcept;
  template<class IntType>
    constexpr byte operator>>(byte b, IntType shift) noexcept;
  constexpr byte& operator{{!=
```

constexpr byte operator|(byte l, byte r) noexcept;
constexpr byte& operator&=(byte& l, byte r) noexcept;
constexpr byte operator&(byte l, byte r) noexcept;
constexpr byte& operator^=(byte& l, byte r) noexcept;
constexpr byte operator^(byte l, byte r) noexcept;
constexpr byte operator~(byte b) noexcept;
template<class IntType>
constexpr IntType to_integer(byte b) noexcept;
}
#define NULL /* see description */
#define offsetof(P, D) /* see description */

## Notes

* `NULL` is also defined in the following headers:
**
**
**
**
**
**
* `std::size_t` is also defined in the following headers:
**
**
**
**
**  <sup>(C++17)</sup>
