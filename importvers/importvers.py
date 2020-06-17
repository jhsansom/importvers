from git import Repo
import os, sys
import importlib
import shutil
import copy

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
    tmp_path = os.path.abspath(tmp_path+'_'+vers)

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

    # rename to differentiate modules from one another
    module.__name__ = module_name+'_'+vers

    # renames module to unique name
    sys.modules[module_name+'_'+vers] = module

    # removes module with undifferentiated name so another version can be loaded if necessary
    sys.modules.pop(module_name)

    return module


def importpath(path, module_name):
    # import local file
    sys.path.append(path)

    # import path
    module = importlib.import_module(module_name)

    # removes from path b/c no longer necessary
    sys.path.remove(path)

    return module