<?php
// exec("python3.7 /home/bigpenguin/code/php/php_py_test.py",$output);
// var_dump($output[0]);
$url="192.168.0.107:8000";
$response=curl_init($url);
$ret=curl_exec($response);
echo $ret;
?>