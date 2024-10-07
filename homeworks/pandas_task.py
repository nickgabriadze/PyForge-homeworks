import pandas as pd
from data_example import wells_df, plates_df, experiments_df

wells_pivot = wells_df.pivot_table(index=['well_id', 'well_row', 'well_column', 'plate_id'],
                                   columns='property_name',
                                   values='property_value',
                                   aggfunc='first').reset_index()

plates_pivot = plates_df.pivot_table(index=['plate_id', 'experiment_id'],
                                     columns='property_name',
                                     values='property_value',
                                     aggfunc='first').reset_index()

experiments_pivot = experiments_df.pivot_table(index='experiment_id',
                                               columns='property_name',
                                               values='property_value',
                                               aggfunc='first').reset_index()

merged_wells_plates = wells_pivot.merge(plates_pivot, how='left', on='plate_id')

final_df = merged_wells_plates.merge(experiments_pivot, how='left', on='experiment_id')


print(final_df)
