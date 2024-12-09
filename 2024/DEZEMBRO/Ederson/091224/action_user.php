<?php
session_start();
include ("connect.php");
// include ("verificacao.php");

$first_name = mysqli_real_escape_string($db, $_POST["first_name"]);

$last_name = mysqli_real_escape_string($db, $_POST["last_name"]);

$fone = mysqli_real_escape_string($db, $_POST["fone"]);

$address = mysqli_real_escape_string($db, $_POST["address"]);

$email = mysqli_real_escape_string($db, $_POST["email"]);

$sexo = mysqli_real_escape_string($db, $_POST["sexo"]);

$query_insert = "insert into clientes values (null, '{$first_name}','{$last_name}','{$sexo}','{$fone}','{$address}', '{$email}');";

echo $query_insert;
// $result_insert = mysqli_query($db,$query_insert);


If ($result_insert == ''){

    echo "<script language:'javascript'> window.alert('Não foi possível efetuar o cadastro');
    
    windows.location.href='user.php';</script>";
}
?>