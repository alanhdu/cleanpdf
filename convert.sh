#!/bin/bash

convert           \
   -verbose       \
   -limit memory 4.5GiB \
   -density 600   \
   -trim          \
    test.pdf      \
   -quality 100   \
   -sharpen 0x1.0 \
    out/%d.jpg
