import pytest, os, hashlib

def pytest_collection_modifyitems(session, config, items):
    for i in items:
        m = i.cell['metadata']
        excercise_2_cell = m.get('solution2_first', False)
        skip = m.get('skip', False)
        if excercise_2_cell or skip:
           i.add_marker(pytest.mark.skip('solution stub'))

    circle_node_total, circle_node_index = read_circleci_env_variables()
    deselected = []
    # round robbin:
    # first group by parent, then skip by ci node index
    from collections import defaultdict
    by_parents = defaultdict(list)
    for index, item in enumerate(items):
        by_parents[item.parent].append(item)
    for i, p in enumerate(by_parents.keys()):
        if i % circle_node_total != circle_node_index:
            deselected.extend(by_parents[p])
    config.hook.pytest_deselected(items=deselected)


class CircleCIError(Exception):
    """Raised for problems running the CirleCI py.test plugin"""


def read_circleci_env_variables():
    """Read and convert CIRCLE_* environment variables"""
    circle_node_total = int(os.environ.get("CIRCLE_NODE_TOTAL", "1").strip() or "1")
    circle_node_index = int(os.environ.get("CIRCLE_NODE_INDEX", "0").strip() or "0")

    if circle_node_index >= circle_node_total:
        raise CircleCIError("CIRCLE_NODE_INDEX={} >= CIRCLE_NODE_TOTAL={}, should be less".format(circle_node_index, circle_node_total))

    return circle_node_total, circle_node_index


def pytest_report_header(config):
    """Add CircleCI information to report"""
    circle_node_total, circle_node_index = read_circleci_env_variables()
    return "CircleCI total nodes: {}, this node index: {}".format(circle_node_total, circle_node_index)

