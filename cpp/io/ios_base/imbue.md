---
title: std::ios_base::imbue
type: Input/output
source: https://en.cppreference.com/w/cpp/io/ios_base/imbue
---

ddcl|
std::locale imbue( const std::locale& loc );
Sets the associated locale of the stream to `loc`. Before returning, each function, registered by `register_callback()` is called with `imbue_event` as a parameter.

## Parameters


### Parameters

- `loc` - new locale to associate the stream to

## Return value

The locale object associated with the stream before the operation.

## Example


## Defect reports


## See also


| cpp/io/ios_base/dsc getloc | (see dedicated page) |

