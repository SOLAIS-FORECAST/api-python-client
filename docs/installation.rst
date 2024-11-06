.. _installation:

Installation
============

Pip installation
----------------

Calibsunapi is available from the Python Package Index (PyPI) and can be installed using pip in any environment.

.. code-block:: console

    $ pip install calibsunapi


Conda installation
----------------

Calibsunapi can be installed into a conda environment by installing the package from the conda-forge channel. If you do not already have access to a conda installation, we recommend installing miniconda for the smallest and easiest installation.

The commands below will use -c conda-forge to make sure packages are downloaded from the conda-forge channel. Alternatively, you can tell conda to always use conda-forge by running:


.. code-block:: console

    $ conda config --add channels conda-forge


From a new environment
^^^^^^^^^^^^^^^^^^^^^^

We recommend creating a separate environment for your work with Satpy. To create a new environment and install Satpy all in one command you can run:

.. code-block:: console

    $ conda create-c conda-forge -n calibsunapi calibsunapi

You must then activate the environment so any future python or conda commands will use this environment.

.. code-block:: console

    $ conda activate calibsunapi


In an existing environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ conda install -c conda-forge calibsunapi