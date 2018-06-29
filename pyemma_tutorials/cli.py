

def main():
    from notebook.notebookapp import main as main_
    from .util import notebook_location, configs_location

    # main eats, argv list and kwargs
    notebook_cfg, notebook_cfg_json = configs_location()

    argv = ['--config=%s' % notebook_cfg, '--config=%s' % notebook_cfg_json ]
    print('arguments:', argv)
    main_(argv=argv)


if __name__ == '__main__':
    main()
