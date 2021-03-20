# Packaging Documentation

## Testing 
Create a account on `https://test.pypi.org/` and generate a token, make sure you copy the token and keep it safe.
Now we need to build and upload the project. Let's first install build dependencies:

```bash
python3 -m pip install --upgrade build
python3 -m pip install --user --upgrade twine
```

Now we first build our project:
```bash
python3 -m build
```

We can now upload the package to `test pypi` by using:
```bash
python3 -m twine upload --repository testpypi dist/*
```
This will ask you for username which would be `__token__` and password which needs to be the token you generated earlier. After the upload is done, you'll get the url you can visit to test the package.
