<?php
include_once 'sql.php';

function insertData($conn, $name, $phonenum)
{
    $sql = "INSERT INTO getContactList (name, phonenum) VALUES ('$name' ,'$phonenum')";

    if ($conn->query($sql) === TRUE) {
    } else {
    }
}

$data = json_decode(file_get_contents('php://input'), true);
#echo $data['data'];
$echoxa = explode(',', str_replace("]", "", str_replace("[", "", $data["data"])));
foreach ($echoxa as $item) {
    #echo $item;
    $ex = explode("-",$item);
    insertData($conn,$ex[0],$ex[1]);
}
echo "{}";
$conn->close();
