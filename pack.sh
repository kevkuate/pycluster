OUT=pipeline_150_ui.tar

if [[ -f "${OUT}" ]]; then
	rm $OUT
fi
if [[ -f "${OUT}.gz" ]]; then
	rm ${OUT}.gz
fi

GZIP='-9'
tar --exclude="*.pyc" --dereference --hard-dereference --check-links                                            -cvf $OUT ../ui/db ../ui/lib ../ui/techs ../ui/setup.json
tar --exclude="*.pyc" --exclude='../ui/db' --exclude='../ui/lib' --exclude='../ui/techs' --exclude="setup.json" -rvf $OUT ../ui

pigz -9 $OUT
