---
title: std::basic_spanbuf::seekoff
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_spanbuf/seekoff
---

ddcl | since=c++23 | 1=
protected:
pos_type seekoff( off_type off, std::ios_base::seekdir dir,
std::ios_base::openmode which =
std::ios_base::in | std::ios_base::out ) override;
Repositions the next pointer to get and/or put area, if possible, to the position that corresponds to exactly `off` characters from beginning, end, or current position of the get and/or put area of the buffer.
Let `''n''` be the number of `CharT` elements in underlying buffer, or `0` when there is no underlying buffer, this function fails if
* the next pointer to the get and/or put area to reposition is null and the computed `''newoff''` (see below) is not zero, which may occur if there is no underlying buffer, or the `*this` is not opened in the mode required by `which`, or
* `dir` is `std::ios_base::cur` and both `std::ios_base::in` and `std::ios_base::out` are set in `which`, or
* the computed `''newoff''` is not representable in `off_type`, less than zero, or greater than `''n''`.
`''newoff''` is computed as below:
* If `dir` is `std::ios_base::beg`, `''newoff''` is `off`.
* If `dir` is `std::ios_base::cur`, `''newoff''` is
** `pptr() - pbase() + off` if `std::ios_base::out` is set in `which`, or
** `gptr() - eback() + off` if `std::ios_base::in` is set in `which`.
* If `dir` is `std::ios_base::end`, `''newoff''` is
** `pptr() - pbase() + off` if `std::ios_base::out` but not `std::ios_base::in` is set in the open mode of `*this`,
** otherwise, `off + n`.
This function repositions the next pointer to get and/or put area to `pbuf + newoff` on success if `std::ios_base::in` and/or `std::ios_base::out` is correspondingly set in `which`, where `''pbuf''` is the pointer to the beginning of the underlying buffer, or the null pointer value if there is no underlying buffer.

## Parameters


### Parameters


## Return value

`pos_type(newoff)` on success, `pos_type(off_type(-1))` on failure.

## Example

