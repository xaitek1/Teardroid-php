<?php
	include_once 'sql.php';

$sql = "SELECT text FROM text";

$result = mysqli_query($conn, $sql);  
$json_array = array();  
while($row = mysqli_fetch_assoc($result))  
{  
    $json_array[] = $row;
    
}
print_r(json_encode($json_array));
?> 
