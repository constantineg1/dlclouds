pip uninstall -y dlclouds
python setup.py build
python setup.py install
pip install .
dlclouds deploy
