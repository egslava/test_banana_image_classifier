source venv/bin/activate

# checking PyTorch -> onnx converter
cd _2_convert_to_onnx
python convert_to_onnx.py
python -m unittest

# let's check w/o Docker
cd ..
python server.py &
pid=$(echo $!)
sleep 5
python test.py
kill $pid

# let's check the server inside Docker
docker run -p 8000:8000 $(docker build -q .) &
pid=$(echo $!)
sleep 5
python test.py
kill $pid