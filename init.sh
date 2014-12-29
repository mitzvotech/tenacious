#!/bin/bash
echo "Thank you for using djangoskeleton!"

echo Enter the project name
read NAME

# create a virtualenv
echo Python Version: 2.7?
read PYTHONVER

if [[ "$PYTHONVER" = "2.7" ]]; then
	echo Setting up virtualenv with Python2.7
	virtualenv -p 2.7 env
else
	echo Setting up virtualenv with Python 3.4
	virtualenv env
fi

# Change the file directory
mv djangoskeleton $NAME

# Change the file contents
find ./ -name '*.py' -type f -exec sed -i "" "s/djangoskeleton/$NAME/g" {} +

# Install dependencies
source env/bin/activate
pip install -r requirements.txt

# Start the git repository where this will be housed
rm -rf .git
git init

# Rewrite the readme file
rm readme.md
echo "# $NAME" >> readme.md 