source venv/bin/activate

cd _2_convert_to_onnx
python convert_to_onnx.py
python -m unittest

cd ..
python server.py &
pid=$(echo $!)
sleep 5
python test.py
kill $pid