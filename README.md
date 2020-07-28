# LinOTP Command-Line Administration Client

LinOTP - the Open Source solution for multi-factor authentication

Copyright © 2010-2019 KeyIdentity GmbH  
Coypright © 2019- arxes-tolina GmbH

## About LinOTP

LinOTP is truly open in two ways. Its modules and components are
licensed under the AGPLv3 and give you a complete working open-source
solution for strong multi-factor authentication.

But LinOTP also uses an open and modular architecture. LinOTP aims not
to lock you into any particular authentication method or protocol or
user information storage.

LinOTP accommodates many different OTP algorithms using a modular
approach. This includes the OATH standards such as HMAC (RFC 4226) and
time-based HMAC. But LinOTP's design makes it easy to create your own
tokens with different algorithms, including challenge-response tokens,
tokens based on QR codes, and tokens based on push-type messages.

Other components like the LinOTP authentication modules or the LinOTP
administration clients make it easy to integrate strong multi-factor
authentication into your environment.

This package contains the LinOTP Command-Line Administration Client,
which lets you manage a LinOTP server from the command line. It is
supremely uninteresting unless you have a LinOTP server running on
your network.

**IMPORTANT:** This program has been around for a while and hasn't
been looked at a lot in recent days. Stuff may work but then again it
may not. USE AT YOUR OWN RISK.

## Installation

1. Installation from PyPI: Use the
   ```terminal
   $ pip install LinOTPAdminClientCLI
   ```
   command.

2. Installation from source: Download the source code from
   https://github.com/linotp-adminclient-cli and, in the top-level
   directory of the source code distribution, say
   ```
   $ python setup.py install
   ```
   (You may wish to do this in a virtualenv.)

## Usage

Refer to the man page, linotpadm(1), or try
```
$ linotpadm     # no arguments
```

