from git import Repo
import os, sys
import importlib
import shutil

def importvers(repo_path, module_name, vers, tmp_path='.'):
    tmp_path = os.path.abspath(tmp_path)

    # add worktree for the version in question for this test
    repo = Repo(repo_path)
    repo.git.worktree('add', tmp_path+'/.tmp', vers)

    # import path
    try:
        module = importpath(tmp_path+'/.tmp', module_name)
    except:
        # if import fails, prune working tree before returning exception
        shutil.rmtree(tmp_path+'/.tmp')
        repo.git.worktree('prune')
        raise

    # switch repository back
    shutil.rmtree(tmp_path+'/.tmp')
    repo.git.worktree('prune')

    return module


def importpath(path, module):
    # import local file
    sys.path.append(path)

    # import path
    return importlib.import_module(module)