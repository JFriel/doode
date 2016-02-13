<?php
$phone = $_POST["answer"];
$text = "$phone"
 $file = fopen("edin_nums.txt","w");
 fwrite($file, $text);
 fclose($file);

?>
