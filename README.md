# ImportVers

ImportVers is a tool that allows scientific programmers to easily document experiments using git. It allows you to save source code in a single repository and import files from different working trees into one Python script. It can be useful for the following:

1. If you have multiple ideas, you can create different branches within your repository. ImportVers allows you to import all of them into one Python script for easy comparison.
2. If you would like to compare the latest commit to an older one, you can import both and compare them in one Python script.
3. You can save these test scripts or Jupyter Notebooks into your repository for later reference. Any user in the future will be able to easily reproduce results without having to manually add working trees for comparison.

## Installation

Simply use the following command:

```Bash
pip install importvers
```

## Usage

For a helpful usage example, please refer to the [example folder](example). Sample code is displayed below.

```Python
from importvers import importvers

# import a newer version of the module
func_new = importvers('..', 'example.sample_func', '9f9906b')

# import an older version of the module
func_old = importvers('..', 'example.sample_func', 'c8bc3ec')
```

To view commit hashes, navigate to your repository and run the command `git log --oneline`. To tag a particular commit, use `git checkout` and `git tag` as follows:

```Bash
git checkout <hash>
git tag -a "<tag>"
git checkout master
```