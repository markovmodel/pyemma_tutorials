from glob import glob

import pytest
import os

executed_notebooks = set()

notebook_groups = [
    ('msm-estimation',
     'msm-analysis',
     'pcca-tpt',
     ),
]

@pytest.fixture(scope='session')
def no_progress_bars():
    """ disables progress bars during testing """
    import pyemma
    pyemma.config.show_progress_bars = False
    yield


### execution timing ##########################################################
from collections import defaultdict
timings = defaultdict(int)


def pytest_runtest_logreport(report):
    if report.when == "call":
        key = report.location[0]
        timings[key] += report.duration


def pytest_terminal_summary(terminalreporter, exitstatus):
    terminalreporter.section('Notebook timings')
    s = sorted(timings.items(), key=lambda x: x[1])
    for nb, total in s:
        terminalreporter.write_line('%s took %.1f seconds' % (nb, total))

###############################################################################


#### Circle CI parallel execution #############################################
def pytest_collection_modifyitems(session, config, items):
    for i in items:
        m = i.cell['metadata']
        excercise_2_cell = m.get('solution2_first', False)
        skip = m.get('skip', False)
        if excercise_2_cell or skip:
            i.add_marker(pytest.mark.skip('solution stub'))

    circle_node_total, circle_node_index = read_circleci_env_variables()
    if circle_node_total > 1:
        by_parents = defaultdict(list)
        for index, item in enumerate(items):
            by_parents[item.parent].append(item)

        # merge grouped parents
        for n in notebook_groups:
            items_to_group = []
            keys_to_merge = []
            for p in by_parents:
                for nb in n:
                    if nb in p.name:
                        items_to_group.extend(by_parents[p])
                        keys_to_merge.append(p)
            for k in keys_to_merge:
                del by_parents[k]
            by_parents[tuple(keys_to_merge)] = items_to_group

        deselected = []
        # round robbin: by notebook file and ci node index
        for i, p in enumerate(by_parents.keys()):
            if i % circle_node_total != circle_node_index:
                deselected.extend(by_parents[p])
        for d in deselected:
            items.remove(d)
        executed_notebooks = [nb.name for nb in
                              set(x.parent for x in set(items) - set(deselected))]
        print('Notebooks to execute:', [x[0] for x in executed_notebooks])
        config.hook.pytest_deselected(items=deselected)


def read_circleci_env_variables():
    """Read and convert CIRCLE_* environment variables"""
    circle_node_total = int(os.environ.get(
        "CIRCLE_NODE_TOTAL", "1").strip() or "1")
    circle_node_index = int(os.environ.get(
        "CIRCLE_NODE_INDEX", "0").strip() or "0")

    if circle_node_index >= circle_node_total:
        raise RuntimeError("CIRCLE_NODE_INDEX={} >= CIRCLE_NODE_TOTAL={}, should be less".format(
            circle_node_index, circle_node_total))

    return circle_node_total, circle_node_index


def pytest_report_header(config):
    """Add CircleCI information to report"""
    circle_node_total, circle_node_index = read_circleci_env_variables()
    return "CircleCI total nodes: {}, this node index: {}".format(circle_node_total, circle_node_index)

###############################################################################


def pytest_runtest_protocol(item, nextitem):
    executed_notebooks.add(item.parent)


def pytest_sessionfinish(session, exitstatus):
    """ we store all notebooks in variable 'executed_notebooks' to a given path and convert them to html """
    import nbformat as nbf
    import tempfile
    out_dir = os.getenv('NBVAL_OUTPUT', tempfile.mkdtemp(
        prefix='pyemma_tut_test_output'))
    print('write html output to', os.path.abspath(out_dir))
    out_files = []
    assert executed_notebooks
    for ipynbfile in executed_notebooks:
        out_file = os.path.join(out_dir, os.path.basename(ipynbfile.name))
        with open(out_file, 'x') as fh:
            nbf.write(ipynbfile.nb, fh)
        out_files.append(out_file)

    import subprocess
    import sys

    cmd = [sys.executable, '-m', 'jupyter',
           'nbconvert', '--to=html'] + out_files
    print('converting via cmd:', cmd)
    subprocess.check_output(cmd)

    # delete source output notebooks
    # for f in out_files:
    #    os.unlink(f)
