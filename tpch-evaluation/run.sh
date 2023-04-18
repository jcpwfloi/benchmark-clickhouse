for lmb in $(seq 2.4 -0.3 0.3); do
	echo "Running lambda=$lmb"
	python3 tpch.py $lmb &> $lmb.csv
done
