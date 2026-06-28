---
title: std::basic_ostream::tellp
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ostream/tellp
---

ddcl |
pos_type tellp();
Returns the output position indicator of the current associated `streambuf` object.
rev | since=c++11 |
Behaves as *UnformattedOutputFunction* (except without actually performing output). After constructing and checking the sentry object,
If `1=fail()==true`, returns `pos_type(-1)`. Otherwise, returns `rdbuf()->pubseekoff(0, std::ios_base::cur, std::ios_base::out)`.

## Parameters

(none)

## Return value

current output position indicator on success, `pos_type(-1)` if a failure occurs.

## Example


## See also

