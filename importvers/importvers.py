from git import Repo
import os, sys
import importlib
import shutil

def importvers(repo_path, module_name, vers, tmp_path='./.tmp'):
    """Returns working tree version

	Parameters
	----------
	repo_path : str
        Filepath to repository (relative or absolute)
    module_name : str
        Using normal Python import syntax, this is the module you wish to import from the package
    vers : str
        Either the hash or tag of the commit
    tmp_path : str
        Path to the temporary folder created for the working tree

	Returns
	----------
	module

	"""

    # finds the absolute path of tmp_path
    tmp_path = os.path.abspath(tmp_path)

    # add worktree for the version in question for this test
    repo = Repo(repo_path)
    repo.git.worktree('add', tmp_path, vers)

    # import path
    try:
        module = importpath(tmp_path, module_name)
    except:
        # if import fails, prune working tree before returning exception
        shutil.rmtree(tmp_path)
        repo.git.worktree('prune')
        raise

    # switch repository back
    shutil.rmtree(tmp_path)
    repo.git.worktree('prune')

    return module


def importpath(path, module):
    # import local file
    sys.path.append(path)

    # import path
    return importlib.import_module(module)