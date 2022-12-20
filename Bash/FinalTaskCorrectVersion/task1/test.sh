echo "Start testing"
echo "Test 1"
echo "test with empty files"
./comparator1.sh tests/test1/file1 tests/test1/file2 -v
if [ $? -eq 0 ]; then
    echo "Test passed"
else
    echo "Test failed"
fi
echo

echo "Test 2"
echo "test if one of files does not exist"
./comparator1.sh tests/test2/file1 tests/test2/file2 -v
if [ $? -eq 3 ]; then
    echo "Test passed"
else
    echo "Test failed"
fi
echo

echo "Test 3"
echo "test with incorrect input"
./comparator1.sh tests/test3/file2 -v
if [ $? -eq 2 ]; then
    echo "Test passed"
else
    echo "Test failed"
fi
echo

echo "Test 4"
echo "test for \n numbers"
./comparator1.sh tests/test4/file1 tests/test4/file2 -v
if [ $? -eq 1 ]; then
    echo "Test passed"
else
    echo "Test failed"
fi
echo

echo "Test 5"
echo "test for numbers with symbols inside"
./comparator1.sh tests/test5/file1 tests/test5/file2 -v
if [ $? -eq 1 ]; then
    echo "Test passed"
else
    echo "Test failed"
fi
echo

echo "Test 6"
echo "test with same file"
./comparator1.sh tests/test6/file1 tests/test6/file1 -v
if [ $? -eq 0 ]; then
    echo "Test passed"
else
    echo "Test failed"
fi
echo

echo "Test 7"
echo "test with big files"
./comparator1.sh tests/test7/file1 tests/test7/file2 -v
if [ $? -eq 1 ]; then
    echo "Test passed"
else
    echo "Test failed"
fi
echo

echo "Test 8"
echo "test with very big files"
./comparator1.sh tests/test8/file1 tests/test8/file2 -v
if [ $? -eq 1 ]; then
    echo "Test passed"
else
    echo "Test failed"
fi
echo
