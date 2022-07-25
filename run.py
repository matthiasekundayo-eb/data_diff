import logging
logging.basicConfig(level=logging.INFO)

import sys
# from data_diff.diff_tables import TableDiffer #, connect_to_table
from data_diff import diff_tables, connect_to_table
import data_diff.__init__

class CompareTables:
    """
    
    """
    def __init__(self, presto_uri, snow_uri, schema, table_name, time_col):
        self.presto_uri = presto_uri
        self.snow_uri = snow_uri
        self.table_name = table_name
        self.time_col = time_col
        self.schema = schema
        self.schema_table = (schema+'.'+table_name).upper()

    def main(self):
        table1 = connect_to_table(self.presto_uri, self.table_name, "id")
        table2 = connect_to_table(self.snow_uri, self.schema_table, "ID")

        for different_row in diff_tables(table1, table2):
            plus_or_minus, columns = different_row
            print(plus_or_minus, columns)

if __name__ == '__main__':
    PRESTO_EB=****
    SNOWFLAKE_EB=****

    compare_obj = CompareTables(PRESTO_EB, SNOWFLAKE_EB, schema='EB', table_name='api_debounce', time_col='created')
    compare_obj.main()
