#!/usr/bin/env python
# -*- coding:utf8 -*-

nonce = (32 * 1024 ) * 1024 * 1024 / (256 * 1024)
nonce2 = (32 * 1024 -500) * 1024 * 1024 / (256 * 1024)
print(nonce)
print(nonce2)
print(nonce-nonce2)
