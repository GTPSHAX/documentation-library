---
title: std::bit_cast
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/bit_cast
---

ddcl|since=c++20|header=bit|
template< class To, class From >
constexpr To bit_cast( const From& from ) noexcept;
Obtain a value of type `To` by reinterpreting the object representation of `From`. Every bit in the value representation of the returned `To` object is equal to the corresponding bit in the object representation of `from`. The values of padding bits in the returned `To` object are unspecified.
If there is no value of type `To` corresponding to the value representation produced, the behavior is undefined. If there are multiple such values, which value is produced is unspecified.
A bit in the value representation of the result is ''indeterminate'' if it
* does not correspond to a bit in the value representation of `From` (i.e. it corresponds to a padding bit), or
* corresponds to a bit <sup>(until C++26)</sup> of an object that<sup>(since C++26)</sup> for which the smallest enclosing object is not within its , or
* has an indeterminate value.
rrev|since=c++26|
A bit in the value representation of the result is ''erroneous'' if it corresponds to a bit for which the smallest enclosing object has an erroneous value.
rev|until=c++26|
For each bit in the value representation of the result that is indeterminate, the smallest object containing that bit has an indeterminate value; the behavior is undefined unless that object is of an uninitialized-friendly type.
The result does not otherwise contain any indeterminate values.
rev|since=c++26|
For each bit `b` in the value representation of the result that is indeterminate or erroneous, let `u` be the smallest object enclosing `b`:
* If `u` is of uninitialized-friendly type, `u` has an indeterminate value if any of the bits in its value representation are indeterminate, or otherwise has an erroneous value.
* Otherwise, if `b` is indeterminate, the behavior is undefined.
* Otherwise, the behavior is erroneous, and the result is as specified above.
The result does not otherwise contain any indeterminate or erroneous values.
.
This function template is `constexpr` if and only if each of `To`, `From` and the types of all subobjects of `To` and `From`:
* is not a union type;
* is not a pointer type;
* is not a pointer to member type;
* is not a volatile-qualified type; and
* has no non-static data member of reference type.

## Parameters


### Parameters

- `from` - the source of bits for the return value

## Return value

An object of type `To` whose value representation is as described above.

## Possible implementation

To implement `std::bit_cast`, ignoring the fact that it's , `std::memcpy` can be used, when it is needed, to interpret the object representation as one of another type:

```cpp
template<class To, class From>
std::enable_if_t<
    sizeof(To) == sizeof(From) &&
    std::is_trivially_copyable_v<From> &&
    std::is_trivially_copyable_v<To>,
    To>
// constexpr support needs compiler magic
bit_cast(const From& src) noexcept
{
    static_assert(std::is_trivially_constructible_v<To>,
        "This implementation additionally requires "
        "destination type to be trivially constructible");

    To dst;
    std::memcpy(&dst, &src, sizeof(To));
    return dst;
}
```


## Notes

`cpp/language/reinterpret_cast` (or equivalent ) between pointer or reference types shall not be used to reinterpret object representation in most cases because of the type aliasing rule.

## Example


### Example


**Output:**
```
std::bit_cast<std::uint64_t>(19880124.000000) == 0x4172f58bc0000000
std::bit_cast<double>(0x3fe9000000000000) == 0.781250
```


## Defect reports


## See also


| cpp/memory/dsc start_lifetime_as | (see dedicated page) |

