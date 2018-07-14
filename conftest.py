import pytest
import os


notebook_groups = [
    ('msm-estimation',
     'msm-analysis',
     'pcca-tpt',
     ),
]

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
def cell_skipped(cell_metadata):
    excercise_2_cell = cell_metadata.get('solution2_first', False)
    skip = cell_metadata.get('skip', False)
    if excercise_2_cell or skip:
        return True
    return False

#### Circle CI parallel execution #############################################
def pytest_collection_modifyitems(session, config, items):
    for i in items:
        if cell_skipped(i.cell['metadata']):
            i.add_marker(pytest.mark.skip('solution stub or metadata["skip"]=True'))

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
        print('Notebooks to execute:', executed_notebooks)
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

cells_per_notebook = defaultdict(list)


def pytest_runtest_call(item):
    cells_per_notebook[item.parent].append(item)


def pytest_sessionfinish(session, exitstatus):
    """ we store all notebooks in variable 'executed_notebooks' to a given path and convert them to html """
    import nbformat as nbf
    import tempfile
    out_dir = os.getenv('NBVAL_OUTPUT', tempfile.mkdtemp(
        prefix='pyemma_tut_test_output'))
    print('write html output to', os.path.abspath(out_dir))
    out_files = []
    ipynbfiles = set(i.parent for i in session.items)
    for ipynbfile in ipynbfiles:
        out_file = os.path.join(out_dir, os.path.basename(ipynbfile.name))
        # map output cells
        cells_with_non_skipped_output = (c for c in ipynbfile.nb.cells if hasattr(c, 'outputs') and not cell_skipped(c.metadata))
        for cell, ipynbcell in zip(cells_with_non_skipped_output, cells_per_notebook[ipynbfile]):
            print(cell, ipynbcell)
            cell.outputs = ipynbcell.test_outputs

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
    for f in out_files:
        os.unlink(f)
