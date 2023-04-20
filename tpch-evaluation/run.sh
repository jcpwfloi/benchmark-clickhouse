for lmb in $(seq 1.8 -0.1 1.8); do
	echo "Running lambda=$lmb"
	python3 tpch.py $lmb &> $lmb.csv
done
