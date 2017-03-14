#!/bin/bash

echo "aws lambda delete-function --function-name lambda1"
aws lambda delete-function --function-name lambda1 >& /dev/null

echo "remove zip, result file"
/bin/rm -f lambda1.zip result.txt


