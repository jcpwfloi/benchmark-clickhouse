for lmb in $(seq 6.4 -0.2 5.0); do
	echo "Running lambda=$lmb"
	python3 tpch.py $lmb &> $lmb.csv
done
