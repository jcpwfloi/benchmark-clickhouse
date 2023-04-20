for file in ch*.sql; do
	echo $file `cat $file | wc -m`
done
