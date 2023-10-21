#!/bin/bash

# Set errors var
errors="false"

default_creds="~/.aws/credentials"

while getopts ":s:b:c:" opt; do
  case $opt in
    s)
      SOURCE="$OPTARG"
      ;;
    b)
      BUCKET="$OPTARG"
      ;;
    c)
      CREDS="$OPTARG"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

if [[ -z "${SOURCE}" ]] || [[ -z "${BUCKET}" ]]; then
    echo "The following arguments are required: -s <SOURCE> -b <BUCKET>"
    exit 1
fi

# Check for credentials in expected location
if [ -f ${CREDS} ]; then
    echo "Credentials found"
    export AWS_CONFIG_FILE=${CREDS}
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

# Check for remote S3 ${BUCKET} bucket successful connection
if aws s3 ls s3://${BUCKET}/ >/dev/null; then
    echo "Connection to AWS and S3 ${BUCKET} bucket successful"
else
    echo "CONNECTION TO \"${BUCKET}\" BUCKET OR AWS UNSUCCESSFUL"
    errors="true"
fi

# Check for local ${SOURCE} directory in current directory
if [ -d ./${SOURCE} ]; then
    echo "Directory ${SOURCE} found"
else
    echo "NO \"${SOURCE}\" DIRECTORY FOUND";
    errors="true"
fi

# Check for errors, and run sync if none found
if [ errors == "false" ]; then
    echo "Please fix above errors and try again"
    exit 1
else
    echo -e "\n\n === COPYING ${SOURCE} TO s3://${BUCKET} === \n\n"
    aws s3 sync ${SOURCE} s3://${BUCKET}
fi
