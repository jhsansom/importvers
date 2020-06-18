# ImportVers

ImportVers allows you to easily import the same file from multiple versions of a git repository. Here are a couple use cases:

1. If you have multiple ideas, you can create different branches within your repository. ImportVers allows you to import all of them into one Python script for easy comparison. 
2. If you would like to compare a new commit to an older one to locate a bug, you can import both and compare them in one Python script. This is particularly useful when the bug produces incorrect data rather than an error code.
3. If you are running scripts that depend on a source code repository, ImportVers will allow you to keep track of which version your scripts used. If you decide you would like to run a script on a newer version, ImportVers allows you to do this easily and document the change.
4. You can save these test scripts (or Jupyter Notebooks) into your repository for later reference. Any user in the future will be able to easily reproduce results without having to manually use `git checkout` to access multiple versions of the source code.

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
path_to_repository = '..'
module_to_import = 'example.sample_func'
version_or_tag = '9f9906b'
func_new = importvers(path_to_repository, module_to_import, version_or_tag)

# import an older version of the module
func_old = importvers('..', 'example.sample_func', 'c8bc3ec')
```

To view commit hashes, navigate to your repository and run the command `git log --oneline`. To tag a particular commit, use `git checkout` and `git tag` as follows:

```Bash
git checkout <hash>
git tag -a "<tag>"
git checkout -
```

## Additional Comments

This package is incredibly small (under 100 lines), and I only made it because I needed it for other work I was doing. I am not an expert in git or Python, but I couldn't find anything similar to this online, so I decided to quickly transform it into a package. If you have any comments or suggestions, please just shoot me an email or create a pull request!
