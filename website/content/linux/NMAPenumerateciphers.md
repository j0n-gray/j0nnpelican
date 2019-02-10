Title: Using NMAP to enumerate ciphers and find vulnerabilities
Date: 2018-05-26 13:00
tags: linux, security

in an ideal world we are all using TLS 1.2 with strong ciphers for application layer internet
facing  protocols such as HTTPS and SMTP. With NMAP we can quickly discover if this is the case:

    sudo nmap -Sv --script ssl-enumerate-ciphers -p 443 localhost << replace as needed

example output:
 
	PORT    STATE SERVICE REASON
	443/tcp open  https   syn-ack
	| ssl-enum-ciphers:
	|   TLSv1.0:
	|     ciphers:
	|       TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA (secp256r1) - A
	|       TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA (secp256r1) - A
	|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (secp256r1) - A
	|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (secp256r1) - A
	|       TLS_RSA_WITH_AES_128_CBC_SHA (rsa 2048) - A
	|       TLS_RSA_WITH_AES_256_CBC_SHA (rsa 2048) - A
	|       TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA (secp256r1) - C
	|       TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA (secp256r1) - C
	|       TLS_RSA_WITH_3DES_EDE_CBC_SHA (rsa 2048) - C
	|       TLS_ECDHE_ECDSA_WITH_RC4_128_SHA (secp256r1) - C
	|       TLS_ECDHE_RSA_WITH_RC4_128_SHA (secp256r1) - C
	|       TLS_RSA_WITH_RC4_128_SHA (rsa 2048) - C
	|       TLS_RSA_WITH_RC4_128_MD5 (rsa 2048) - C
	|     compressors:
	|       NULL
	|     cipher preference: server
	|     warnings:
	|       64-bit block cipher 3DES vulnerable to SWEET32 attack
	|       Broken cipher RC4 is deprecated by RFC 7465
	|       Ciphersuite uses MD5 for message integrity
	|       Weak certificate signature: SHA1


3DES and RC4 ciphers are especially dangerous to look out for - they are
very insecure. also you *really* should be using TLS1.2 only but if there
are compatibility issues with older browsers in corporate environments
(which to me isnt a good enough excuse) then you should at the *very least* not be using SSL anymore.

### sources / further reading:

1. [nmap documentation](https://nmap.org/nsedoc/scripts/ssl-enum-ciphers.html)
2. [sweet32](https://sweet32.info/)

























































