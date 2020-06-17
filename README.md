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


```Python
from importvers import importvers

# import and use files from a newer commit
fmtrack_new = importvers('../../fmtrack', 'fmtrack', '698f04c')
tracker = fmtrack_new.FMTracker()
tracker.save_all('./test')


# import and use files from an older commit
fmtrack_old = importvers('../../fmtrack', 'fmtrack', '8e4a0c2')
tracker = fmtrack_old.FMTracker()
tracker.save_all()
```