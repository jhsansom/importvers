from git import Repo
import os, sys
import importlib
import shutil
import copy
import numpy as np

def importvers(repo_path, module_name, vers, tmp_path=None):
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

    # modified module name that will end up in sys.modules
    modified_name = module_name+'_'+vers

    # if a package is already imported under the same module name,
    # importvers reorganizes it during runtime
    flag = module_name in sys.modules.keys()
    if flag:
        sys.modules[module_name+'_control'] = sys.modules[module_name]
        sys.modules.pop(module_name)

    # snapshot of modules before any importing occurs
    orig_modules = np.array(list(sys.modules.keys()))

    # finds the absolute path of tmp_path
    if tmp_path is None:
        tmp_path = './.tmp'
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
    module.__name__ = modified_name

    # renames module to unique name
    sys.modules[modified_name] = module

    # removes module with undifferentiated name so another version can be loaded if necessary
    sys.modules.pop(module_name)

    # remove additional names of modules imported with primary module.
    # Because they are named the same as the original module (module_name), 
    # they create conflicts between different commits
    now_modules = np.array(list(sys.modules.keys()))
    diff = np.setdiff1d(now_modules, orig_modules)
    for elem in diff:
        if module_name in elem and elem != modified_name:
            sys.modules.pop(elem)
    
    # re-adds original module if it is there
    if flag:
        sys.modules[module_name] = sys.modules[module_name+'_control']
        sys.modules.pop(module_name+'_control')

    return module


def importpath(path, module_name):
    # import local file
    sys.path.append(path)

    # import path
    module = importlib.import_module(module_name)

    # removes from path b/c no longer necessary
    sys.path.remove(path)

    return module