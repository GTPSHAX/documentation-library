---
title: std::fclose
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/fclose
---

ddcl|header=cstdio|
int fclose( std::FILE* stream );
Closes the given file stream and writes any unwritten data from `stream`'s buffer to the associated output device. Any unread buffered data are discarded.
Whether or not the operation succeeds, the stream is no longer associated with a file, and the buffer allocated by `std::setbuf` or `std::setvbuf`, if any, is also disassociated and deallocated if automatic allocation was used.
rrev|since=c++26|
If any data are written to an output device, returning from `std::fclose` establishes an observable checkpoint.
The behavior is undefined if the value of the pointer `stream` is used after `std::fclose` returns.

## Parameters


### Parameters

- `stream` - the file stream to close

## Return value

`0` on success, `EOF` otherwise.

## Example


## See also


| cpp/io/c/dsc fopen | (see dedicated page) |
| cpp/io/c/dsc freopen | (see dedicated page) |
| cpp/io/basic_filebuf/dsc close | (see dedicated page) |

