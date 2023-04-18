clickhouse client --query "create database tpc"
clickhouse client --query "create database tpcm"
clickhouse client -d tpc --multiquery < tpch_ch_schema.sql
clickhouse client -d tpcm --multiquery < memory.sql
