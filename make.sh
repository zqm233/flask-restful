#python -m grpc_tools.protoc -I common/grpc/demo \
#--python_out= common/grpc/demo \
#common/grpc/demo/demo.proto

SRC_DIR=common/grpc/demo
DST_DIR=common/grpc/demo
python -m grpc_tools.protoc -I=$SRC_DIR --python_out=$DST_DIR --grpc_python_out=$DST_DIR $SRC_DIR/demo.proto