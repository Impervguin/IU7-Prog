test_dir=./tests
shell_file=./comparator3.sh
echo "Start testing"
echo "Test 1"
echo "test with empty files"
$shell_file $test_dir/test1/file1 $test_dir/test1/file2 -v
if [ $? -eq 0 ]; then
    echo "Test passed"
else
    echo "Test failed"
fi
echo

echo "Test 2"
echo "test if one of files does not exist"
$shell_file $test_dir/test2/file1 $test_dir/test2/file2 -v
if [ $? -eq 3 ]; then
    echo "Test passed"
else
    echo "Test failed"
fi
echo

echo "Test 3"
echo "test with incorrect input"
$shell_file $test_dir/test3/file2 -v
if [ $? -eq 2 ]; then
    echo "Test passed"
else
    echo "Test failed"
fi
echo

echo "Test 4"
echo "standard test"
$shell_file $test_dir/test4/file1 $test_dir/test4/file2 -v
if [ $? -eq 1 ]; then
    echo "Test passed"
else
    echo "Test failed"
fi
echo

echo "Test 5"
echo "\n difference"
$shell_file $test_dir/test5/file1 $test_dir/test5/file2 -v
if [ $? -eq 0 ]; then
    echo "Test passed"
else
    echo "Test failed"
fi
echo

echo "Test 6"
echo "test with same file"
$shell_file $test_dir/test6/file1 $test_dir/test6/file1 -v
if [ $? -eq 0 ]; then
    echo "Test passed"
else
    echo "Test failed"
fi
echo

echo "Test 7"
echo ""
$shell_file $test_dir/test7/file1 $test_dir/test7/file2 -v
if [ $? -eq 0 ]; then
    echo "Test passed"
else
    echo "Test failed"
fi
echo

echo "Test 8"
echo "test with integers"
$shell_file $test_dir/test8/file1 $test_dir/test8/file2 -v
if [ $? -eq 1 ]; then
    echo "Test passed"
else
    echo "Test failed"
fi
echo
