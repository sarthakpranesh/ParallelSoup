# How to release the Package

## Test.pypi
- `python3 -m build`: to build the upto date dist files
- get the api token for the project
- `python3 -m twine upload --repository testpypi dist/*`: will ask for username: `__token__` and password will be the copied api token

## pypi
- `python3 -m build`: to build the upto date dist files
- get the api token for the project
- `python3 -m twine upload dist/*`
