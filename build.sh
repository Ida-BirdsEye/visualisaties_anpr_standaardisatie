#!/bin/bash

cat docs/*.md > full_document.md

chmod +x build.sh
pandoc full_document.md -o anpr_rapport.docx
