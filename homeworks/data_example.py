import pandas as pd

wells_df = pd.DataFrame({
    'well_id': [1, 1, 2, 2],
    'well_row': ['A', 'A', 'B', 'B'],
    'well_column': [1, 1, 2, 2],
    'property_name': ['concentration', 'concentration_unit', 'concentration', 'concentration_unit'],
    'property_value': [5.0, 'mM', 7.0, 'mM'],
    'plate_id': [1, 1, 2, 3]
})

plates_df = pd.DataFrame({
    'plate_id': [1, 2, 3, 4],
    'plate_name': ['Plate 1', 'Plate 2', 'Plate 3', 'Plate 4'],
    'experiment_id': [101, 101, 102, 103],
    'property_name': ['plate_property_1', 'plate_property_2', 'plate_property_1', 'plate_property_2'],
    'property_value': ['value1', 'value2', 'value3', 'value4']
})

experiments_df = pd.DataFrame({
    'experiment_id': [101, 102, 103, 104],
    'experiment_name': ['Experiment A', 'Experiment B', 'Experiment C', 'Experiment D'],
    'property_name': ['channel', 'channel_order', 'experiment_property', 'experiment_property'],
    'property_value': ['blue', 'order_1', 'experiment_value1', 'experiment_value2']
})