---
title: Error numbers
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/errno_macros
---


# Error numbers

Each of the macros defined in  expands to integer constant expressions with type `int`, each with a positive value, matching most of the [https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/errno.h.html POSIX error codes]. The following constants are defined (the implementation may define more, as long as they begin with `'E'` followed by digits or uppercase letters).
All values are required to be unique except that the values of `EOPNOTSUPP` and `ENOTSUP` may be identical and the values of `EAGAIN` and `EWOULDBLOCK` may be identical.

## Example


### Example


**Output:**
```
Known error codes/messages:

          E2BIG: Argument list too long
         EACCES: Permission denied
     EADDRINUSE: Address already in use
  EADDRNOTAVAIL: Cannot assign requested address
   EAFNOSUPPORT: Address family not supported by protocol
         EAGAIN: Resource temporarily unavailable
       EALREADY: Operation already in progress
          EBADF: Bad file descriptor
        EBADMSG: Bad message
          EBUSY: Device or resource busy
      ECANCELED: Operation canceled
         ECHILD: No child processes
   ECONNABORTED: Software caused connection abort
   ECONNREFUSED: Connection refused
     ECONNRESET: Connection reset by peer
        EDEADLK: Resource deadlock avoided
   EDESTADDRREQ: Destination address required
           EDOM: Numerical argument out of domain
         EEXIST: File exists
         EFAULT: Bad address
          EFBIG: File too large
   EHOSTUNREACH: No route to host
          EIDRM: Identifier removed
         EILSEQ: Invalid or incomplete multibyte or wide character
    EINPROGRESS: Operation now in progress
          EINTR: Interrupted system call
         EINVAL: Invalid argument
            EIO: Input/output error
        EISCONN: Transport endpoint is already connected
         EISDIR: Is a directory
          ELOOP: Too many levels of symbolic links
         EMFILE: Too many open files
         EMLINK: Too many links
       EMSGSIZE: Message too long
   ENAMETOOLONG: File name too long
       ENETDOWN: Network is down
      ENETRESET: Network dropped connection on reset
    ENETUNREACH: Network is unreachable
         ENFILE: Too many open files in system
        ENOBUFS: No buffer space available
        ENODATA: No data available
         ENODEV: No such device
         ENOENT: No such file or directory
        ENOEXEC: Exec format error
         ENOLCK: No locks available
        ENOLINK: Link has been severed
         ENOMEM: Cannot allocate memory
         ENOMSG: No message of desired type
    ENOPROTOOPT: Protocol not available
         ENOSPC: No space left on device
          ENOSR: Out of streams resources
         ENOSTR: Device not a stream
         ENOSYS: Function not implemented
       ENOTCONN: Transport endpoint is not connected
        ENOTDIR: Not a directory
      ENOTEMPTY: Directory not empty
ENOTRECOVERABLE: State not recoverable
       ENOTSOCK: Socket operation on non-socket
        ENOTSUP: Operation not supported
         ENOTTY: Inappropriate ioctl for device
          ENXIO: No such device or address
     EOPNOTSUPP: Operation not supported
      EOVERFLOW: Value too large for defined data type
     EOWNERDEAD: Owner died
          EPERM: Operation not permitted
          EPIPE: Broken pipe
         EPROTO: Protocol error
EPROTONOSUPPORT: Protocol not supported
     EPROTOTYPE: Protocol wrong type for socket
         ERANGE: Numerical result out of range
          EROFS: Read-only file system
         ESPIPE: Illegal seek
          ESRCH: No such process
          ETIME: Timer expired
      ETIMEDOUT: Connection timed out
        ETXTBSY: Text file busy
    EWOULDBLOCK: Resource temporarily unavailable
          EXDEV: Invalid cross-device link
```


## See also


| cpp/error/dsc errc | (see dedicated page) |
| cpp/error/dsc errno | (see dedicated page) |
| cpp/io/c/dsc perror | (see dedicated page) |
| cpp/string/byte/dsc strerror | (see dedicated page) |

