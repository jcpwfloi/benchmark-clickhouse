clickhouse client --format_csv_delimiter="|" -d tpc -q "INSERT INTO region FORMAT CSV " < tables/region.tbl
clickhouse client --format_csv_delimiter="|" -d tpc -q "INSERT INTO nation FORMAT CSV " < tables/nation.tbl
clickhouse client --format_csv_delimiter="|" -d tpc -q "INSERT INTO customer FORMAT CSV " < tables/customer.tbl
clickhouse client --format_csv_delimiter="|" -d tpc -q "INSERT INTO supplier FORMAT CSV " < tables/supplier.tbl
clickhouse client --format_csv_delimiter="|" -d tpc -q "INSERT INTO part FORMAT CSV " < tables/part.tbl
clickhouse client --format_csv_delimiter="|" -d tpc -q "INSERT INTO partsupp FORMAT CSV " < tables/partsupp.tbl
clickhouse client --format_csv_delimiter="|" -d tpc -q "INSERT INTO orders FORMAT CSV " < tables/orders.tbl
clickhouse client --format_csv_delimiter="|" -d tpc -q "INSERT INTO lineitem FORMAT CSV " < tables/lineitem.tbl
