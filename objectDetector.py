import subprocess

test_file = input("image file name: ")
command = 'darknet_no_gpu.exe detector test data/obj.data yolo-obj.cfg backup/yolo-obj_4000.weights {} -ext_output -dont_show'.format(test_file)
subprocess.call(command, shell=False)