def car_info(manufacturer, model, **aditional_info):
    """Takes all the parameters and puts them in dictionary."""

    result = {}
    result['manufacturer'] = manufacturer
    result['model'] = model

    for key, value in aditional_info.items():
        result[key] = value

    return result

