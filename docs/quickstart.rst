.. _quickstart:

Quickstart
==========

Right after installing the package, you can start using the API.

Try the API with the demo endpoints
-----------------------------------

If you don't have any credentials, you can use the demo endpoints.

You can for example check out the full output of the demo plant available to everyone.

.. code-block:: python

    from calibsunapi import CalibsunApiClient, Targets

    client = CalibsunApiClient()
    output = client.get_latest_forecast_demo(target=Targets.GTI)


This should retrieve the latest GTI forecast for the demo plant. 
If you're using a data processing framework like pandas, you can easily convert the output to a DataFrame like that :

.. code-block:: python

    import pandas as pd

    df = pd.DataFrame(output)
    df.head()

Which should display the first 5 rows of the forecast data :

.. code-block:: console

                            Date  Quantile 5  Quantile 10  Quantile 15  Quantile 20  ...  Clear Sky  satellite  nwp  measures  warning message
    0  2024-11-06T13:50:00+00:00       51.67        63.99        76.18        84.85  ...     451.17          1    1         1                 
    1  2024-11-06T13:55:00+00:00       44.34        56.74        67.29        78.06  ...     438.85          1    1         1                 
    2  2024-11-06T14:00:00+00:00       39.69        50.84        61.22        72.38  ...     426.14          1    1         1                 
    3  2024-11-06T14:05:00+00:00       35.07        47.09        57.09        66.70  ...     413.05          1    1         1                 
    4  2024-11-06T14:10:00+00:00       32.52        45.06        54.69        64.12  ...     399.59          1    1         1   


Try the API with credentials
-----------------------------------

If you have credentials, make sure to export it in environment variables OR to pass it to the client constructor.

.. code-block:: python

    from calibsunapi import CalibsunApiClient

    client = CalibsunApiClient(calibsun_client_id="your_client_id", calibsun_client_secret="your_client_secret")

.. note::
    
    If you don't have any plants, you can `create an account <https://www.calibsun.com/fr/sign-up>`_ and then a free trial plant that will last 14 days in the Calibsun dashboard.


Then, you can start to discover the plants you have access to.


.. code-block:: python
    plants = client.list_plants()
    plant = plants[0]
    print(plant)

This should display the first plant object you have access to.

.. code-block:: console
    Plant(Signes)

Then, you can directly use the plant object to get the latest forecast.

.. code-block:: python

    output = plant.get_latest_forecast()

    import pandas as pd

    df = pd.DataFrame(output)
    df.head()

Full example, iterating over all your plants and getting the latest forecast :

.. code-block:: python

    from calibsunapi import CalibsunApiClient, Targets

    client = CalibsunApiClient(calibsun_client_id="your_client_id", calibsun_client_secret="your_client_secret")

    for plant in client.list_plants():
        output = plant.get_latest_forecast(Targets.GTI)


Send measurement data to Calibsun
-----------------------------------

If you need to send your measurement data to calibsun, just as before, you can use the plant object JSON-serializable data.

.. code-block:: python

    from calibsunapi import CalibsunApiClient

    client = CalibsunApiClient(calibsun_client_id="your_client_id", calibsun_client_secret="your_client_secret")

    for plant in client.list_plants():
        data = get_my_plant_data(plant.site_id)
        plant.push_measurements(data=data)

You can also directly point to a data file and send any data you'd like in any known format. For example, with csv : 

.. code-block:: python

    from calibsunapi import CalibsunApiClient, UploadMeasurement

    client = CalibsunApiClient(calibsun_client_id="your_client_id", calibsun_client_secret="your_client_secret")

    for plant in client.list_plants():
        filepath = get_my_plant_data(plant.site_id)
        plant.push_measurements(format=UploadMeasurementsFormat.CSV, filename=filepath)