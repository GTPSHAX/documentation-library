---
title: std::basic_filebuf::close
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_filebuf/close
---

ddcl|
std::basic_filebuf<CharT, Traits>* close();
If a put area exist (e.g. file was opened for writing), first calls `overflow(Traits::eof())` to write all pending output to the file, including any unshift sequences.
If the most recently called function, out of , , , and , was , then calls , perhaps multiple times, to determine the unshift sequence according to the imbued locale, and writes that sequence to file with `overflow(Traits::eof())`.
Then, closes the file as if by calling `std::fclose()`, regardless of whether any of the preceding calls succeeded or failed.
If any of the function calls made, including the call to `std::fclose()`, fails, returns a null pointer. If any of the function calls made throws an exception, the exception is caught and rethrown after closing the file. If the file is already closed, returns a null pointer right away.
In any case, updates the private member variable that is accessed by `is_open()`.

## Parameters

(none)

## Return value

`this` on success, a null pointer on failure.

## Notes

`close()` is typically called through the destructor of `std::basic_filebuf` (which, in turn, is typically called by the destructor of `std::basic_fstream`.

## Example


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-622 | C++98 | it was unclear how to handle the<br>exception thrown during closing | it is rethrown after closing the file |


## See also


| cpp/io/basic_filebuf/dsc is_open | (see dedicated page) |
| cpp/io/basic_filebuf/dsc ~basic_filebuf | (see dedicated page) |

