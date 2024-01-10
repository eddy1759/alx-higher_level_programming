#!/bin/bash
# Get the response body for a given URL for 200 status code response
curl -sX GET "$1" -L 200
