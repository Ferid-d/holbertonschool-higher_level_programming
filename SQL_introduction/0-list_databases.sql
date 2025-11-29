#!/bin/bash

USER="root"
PASS="password123"

mysql -u "$USER" -p"PASS" -e "SHOW DATABASES;"
