import pytest

def pytest_collection_modifyitems(config, items):
    for i in items:
        m = i.cell['metadata']
        excercise_2_cell = m.get('solution2', False)
        if excercise_2_cell:
           i.Item
           i.add_marker(pytest.mark.skip('solution stub')) 

