#!/bin/bash

# Set errors var
errors="false"

# Check for credentials in expected location
if [ -f ~/.aws/credentials ]; then
    echo "Credentials found"
else
    echo "NO CREDENTIALS FOUND"
    errors="true"
fi

# Check for aws binary on path
if which aws >/dev/null; then
    echo "aws binary found"
else
    echo "NO AWS BINARY FOUND"
    errors="true"
fi

# Check for remote S3 chrisdunaj.com bucket successful connection
if aws s3 ls s3://chrisdunaj.com >/dev/null; then
    echo "Connection to AWS and S3 chrisdunaj.com bucket successful"
else
    echo "CONNECTION TO \"chrisdunaj.com\" BUCKET OR AWS UNSUCCESSFUL"
    errors="true"
fi

# Check for local chrisdunaj.com directory in current directory
if [ -d ./chrisdunaj.com ]; then
    echo "Directory chrisdunaj.com found"
else
    echo "NO \"chrisdunaj.com\" DIRECTORY FOUND";
    errors="true"
fi

# Check for errors, and run sync if none found
if [ errors == "false" ]; then
    echo "Please fix above errors and try again"
    exit 1
else
    echo -e "\n\n === COPYING chrisdunaj.com TO s3://chrisdunaj.com === \n\n"
    aws s3 sync chrisdunaj.com s3://chrisdunaj.com
fi
