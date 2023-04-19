cd tables/
./dbgen -s 1 -v
cd ..
bash create_tables.sh
bash import.sh
bash memory.sh

